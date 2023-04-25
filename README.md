# Pytest Patch

An automagic replacement for `monkeypatch` or `unittest.mock.patch` that can be
used on objects either directly or by name.

![tests](https://github.com/megawidget/pytest-patch/actions/workflows/python-package.yml/badge.svg)

## Usage Examples

### patching objects directly

```
from pytest import fixture

from mymodule import callee, caller


@fixture
def callee_mock(patch):
  return patch(callee)  # returns `MagicMock` by default


def test_caller(callee_mock):
  caller()
  assert callee_mock.called
```


### patching objects by name

```
from pytest import fixture

from mymodule import caller


@fixture
def callee_mock(patch):
  return patch('callee')  # assumes `callee` is in `mymodule`
```


### patching by full path

This behavior is similar to `unittest.mock.patch`.

```
@fixture
def callee_mock(patch):
  return patch('mymodule.callee')
```


## Configuration

By default, `pytest-patch` assumes the following repository structure:

```
mymodule/
  .git/
    ...
  mymodule/
    wat/
      ermelon.py
    ...
  tests/
    */  # e.g. unit/
      mymodule/
        wat/
          test_ermelon.py
    ...
```

No configuration is needed if your repository matches this structure where the
repository name is the same as the name of the module and your tests are in
their corresponding subdirectories mirroring your module's path structure.

If the above is not the case, e.g. you have a repository with a nonmatching
module name or a monorepo with multiple modules, you may specify the
corresponding flags either in the `pytest` command line or the ini file,
glob-style:

```
pytest --module-names=mymodule,othermodule --test-paths=tests.unit,tests.e2e.*
```

or (in `pytest.ini`)

```
[pytest]
module_names = mymodule othermodule
test_paths = tests.unit tests.e2e.*
```
