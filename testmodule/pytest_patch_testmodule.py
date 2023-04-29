#!/usr/bin/env python

from mock import sentinel


def callee():
  return sentinel.callee


def caller():
  return callee()


def boolean():
  return bool(5)
