# Pytest Patch

An automagic replacement for `monkeypatch` or `unittest.mock.patch` that can be
used on objects either directly or by name.

## Usage Examples

### patching objects directly

```
from pytest import fixture

from mymodule import wat, ermelon


@fixture
def wat_mock(patch):
  return patch(wat)  # returns `MagicMock` by default


def test_ermelon(wat_mock):
  ermelon()
  assert wat_mock.called
```


### patching objects by name

```
from pytest import fixture

from mymodule import ermelon


@fixture
def wat_mock(patch):
  return patch('wat')  # assumes `wat` is in `mymodule`
```


### patching by full path

This behavior is similar to `unittest.mock.patch`.

```
@fixture
def wat_mock(patch):
  return patch('mymodule.wat')
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
      wat/
        test_ermelon.py
    ...
```

No configuration is needed if your repository matches this structure where the
repository name is the same as the name of the module and your tests are in
their corresponding subdirectories mirroring your module's path structure.

If the above is not the case, e.g. you have a repository with a nonmatching
module name or a monorepo with multiple modules, you may specify the
corresponding flags either in the `pytest` command line or the ini file:

```
pytest --module-names=wat,ermelon --test-paths=tests.unit,tests.e2e
```

or (in `pytest.ini`)

```
[pytest]
module_names = wat ermelon
test_paths = tests.unit tests.e2e
```
