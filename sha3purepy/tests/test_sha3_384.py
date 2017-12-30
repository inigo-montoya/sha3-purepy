# -*- coding: utf-8 -*-
# test_sha3_384.py

import pytest
from sha3purepy import Sha3PurePy

def test_sha3_384_abc(abc):
    target = Sha3PurePy.sha3_384(abc['value']).hexdigest()
    assert target == abc['384'].replace(' ', '')


def test_sha3_384_empty_string(empty_string):
    target = Sha3PurePy.sha3_384(empty_string['value']).hexdigest()
    assert  target == empty_string['384'].replace(' ', '')


def test_sha3_384_small_string(small_string_length):
    target = Sha3PurePy.sha3_384(small_string_length['value']).hexdigest()
    assert  target == small_string_length['384'].replace(' ', '')


def test_sha3_384_medium_string(medium_string_length):
    target = Sha3PurePy.sha3_384(medium_string_length['value']).hexdigest()
    assert  target == medium_string_length['384'].replace(' ', '')


# def test_sha3_384_long_string(long_string_length):
#     target = Sha3PurePy.sha3_384(long_string_length['value']()).hexdigest()
#     assert  target == long_string_length['384'].replace(' ', '')