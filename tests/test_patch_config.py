# -*- coding: utf-8 -*-


def test_name_option(testdir):
  testdir.makepyfile("""
    import pytest

    @pytest.fixture
    def names(pytestconfig):
      return pytestconfig.getoption('module_names')

    def test_names(names):
      assert names.split(',') == ['wat', 'ermelon']
  """)

  assert testdir.runpytest('--module-names=wat,ermelon').ret == 0


def test_name_ini(testdir):
  testdir.makeini("""
    [pytest]
    module_names = wat ermelon
  """)

  testdir.makepyfile("""
    import pytest

    @pytest.fixture
    def names(pytestconfig):
      return pytestconfig.getini('module_names')

    def test_names(names):
      assert names == ['wat', 'ermelon']
  """)

  assert testdir.runpytest().ret == 0


def test_path_option(testdir):
  testdir.makepyfile("""
    import pytest

    @pytest.fixture
    def path(pytestconfig):
      return pytestconfig.getoption('test_paths')

    def test_path(path):
      assert path.split(',') == ['tests.unit', 'tests.e2e']
  """)

  assert testdir.runpytest('--test-paths=tests.unit,tests.e2e').ret == 0


def test_path_ini(testdir):
  testdir.makeini("""
    [pytest]
    test_paths = tests.unit tests.e2e
  """)

  testdir.makepyfile("""
    import pytest

    @pytest.fixture
    def path(pytestconfig):
      return pytestconfig.getini('test_paths')

    def test_path(path):
      assert path == ['tests.unit', 'tests.e2e']
  """)

  assert testdir.runpytest().ret == 0
