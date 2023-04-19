# -*- coding: utf-8 -*-

import inspect
import os
from fnmatch import fnmatch

import pytest
from mock import MagicMock


NAMES = 'module_names'
TEST_PATHS = 'test_paths'


def pytest_addoption(parser):
    group = parser.getgroup('patch')

    help_ = 'comma-separated module names'
    group.addoption('--module-names', action='store', dest=NAMES,
                    default=None, help=help_)
    parser.addini(NAMES, help_, 'args')

    help_ = 'comma-separated test paths'
    group.addoption('--test-paths', action='store',
                    dest=TEST_PATHS, default=None, help=help_)
    parser.addini(TEST_PATHS, help_, 'args')


def _match_path(module, path):
  for idx, dirname in enumerate(path):
    if not fnmatch(module[idx], dirname):
      return False
  return True


def _patch_setattr(monkeypatch, module_names, test_paths, path, mock):
  if not module_names or not test_paths:
    dirs = inspect.getouterframes(inspect.currentframe())[2][1].split(os.sep)
    tests_index = dirs.index('tests')
    if not module_names:
      module_names = (dirs[tests_index - 1],)
    if not test_paths:
      test_paths = ('.'.join(dirs[tests_index:tests_index + 2]),)

  if hasattr(path, '__module__'):
    # object imported from tested module
    monkeypatch.setattr('.'.join((path.__module__, path.__name__)), mock)
    return
  elif any(path.startswith(i + '.') for i in module_names):
    # full path, e.g. `wat.ermelon.seeds`
    monkeypatch.setattr(path, mock)
  else:
    # object defined in tested module
    # due to how fixtures work, assume the test is two frames up the stack
    # and gets its path
    test_path = inspect.getouterframes(inspect.currentframe())[2][1]
    test_path = os.path.relpath(test_path)
    dirs, fn = os.path.split(test_path)
    # `test_wat.py` -> `wat`
    fn = os.path.splitext(fn)[0].replace('test_', '', 1)
    test_path = os.path.join(dirs, fn)
    # `tests/unit/wat` path -> `tests.unit.wat` module
    module = test_path.replace(os.path.sep, '.')
    module_split = module.split('.')
    # `tests.unit.ermelon` -> `ermelon`
    for test_path in test_paths:
      if _match_path(module_split, test_path.split('.')):
        module = module.replace(test_path + '.', '', 1)
        break
    try:
      monkeypatch.setattr('.'.join((module, path)), mock)
    except AttributeError:
      # maybe it's a builtin? e.g. `patch('open')`
      monkeypatch.setattr(f"builtins.{path}", mock)


@pytest.fixture
def patch(monkeypatch, pytestconfig):
  module_names = pytestconfig.getoption(NAMES) or pytestconfig.getini(NAMES)
  if isinstance(module_names, str):
    module_names = module_names.split(',')
  test_paths = (pytestconfig.getoption(TEST_PATHS)
                or pytestconfig.getini(TEST_PATHS))
  if isinstance(test_paths, str):
    test_paths = test_paths.split(',')

  def wrapper(path, mock=None):
    mock = mock if mock is not None else MagicMock()
    _patch_setattr(monkeypatch, module_names, test_paths, path, mock)
    return mock

  return wrapper
