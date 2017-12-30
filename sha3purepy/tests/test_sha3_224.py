# -*- coding: utf-8 -*-
# test_sha3_224.py

import pytest
from sha3purepy import Sha3PurePy

def test_sha3_224_abc(abc):
    target = Sha3PurePy.sha3_224(abc['value']).hexdigest()
    assert target == abc['224'].replace(' ', '')


def test_sha3_224_empty_string(empty_string):
    target = Sha3PurePy.sha3_224(empty_string['value']).hexdigest()
    assert  target == empty_string['224'].replace(' ', '')


def test_sha3_224_small_string(small_string_length):
    target = Sha3PurePy.sha3_224(small_string_length['value']).hexdigest()
    assert  target == small_string_length['224'].replace(' ', '')


def test_sha3_224_medium_string(medium_string_length):
    target = Sha3PurePy.sha3_224(medium_string_length['value']).hexdigest()
    assert  target == medium_string_length['224'].replace(' ', '')


# def test_sha3_224_long_string(long_string_length):
#     target = Sha3PurePy.sha3_224(long_string_length['value']()).hexdigest()
#     assert  target == long_string_length['224'].replace(' ', '')