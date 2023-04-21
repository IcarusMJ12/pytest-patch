#!/usr/bin/env python

from pytest import fixture
from mock import MagicMock, sentinel

from pytest_patch_testmodule import boolean, caller, callee


@fixture
def callee_obj(patch):
  return patch(callee, MagicMock(return_value=sentinel.obj))


@fixture
def callee_name(patch):
  return patch('callee', MagicMock(return_value=sentinel.name))


@fixture
def callee_full(patch):
  return patch('pytest_patch_testmodule.callee',
               MagicMock(return_value=sentinel.full))


def test_callee():
  assert callee() == sentinel.callee


def test_caller_obj(callee_obj):
  assert caller() == sentinel.obj


def test_caller_name(callee_name):
  assert caller() == sentinel.name


def test_caller_full(callee_full):
  assert caller() == sentinel.full


def test_builtin(patch):
  patch('bool').return_value = sentinel.bool
  assert boolean() == sentinel.bool
