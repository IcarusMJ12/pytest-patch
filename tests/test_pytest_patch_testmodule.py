#!/usr/bin/env python

from pytest import fixture
from mock import MagicMock

from pytest_patch_testmodule import a, _a


@fixture
def a_obj(patch):
  return patch(_a, MagicMock(return_value='obj'))


@fixture
def a_name(patch):
  return patch('_a', MagicMock(return_value='name'))


@fixture
def a_full(patch):
  return patch('pytest_patch_testmodule._a', MagicMock(return_value='full'))


def test_a():
  assert a('q') == 'q_a'


def test_a_obj(a_obj):
  assert a('q') == 'obj'


def test_a_name(a_name):
  assert a('q') == 'name'


def test_a_full(a_full):
  assert a('q') == 'full'
