# -*- coding: utf-8 -*-

from pytest_patch import _match_path


def test_match_path_valid():
  assert _match_path(('tests', 'unit', 'wat'), ('tests', '*')) is True


def test_match_path_invalid():
  assert _match_path(('tests', 'unit', 'wat'), ('tests', 'e2e')) is False
