# -*- coding: utf-8 -*-
# test_sha3_256.py

import pytest
from sha3purepy import Sha3PurePy

def test_sha3_256_abc(abc):
    target = Sha3PurePy.sha3_256(abc['value']).hexdigest()
    assert target == abc['256'].replace(' ', '')


def test_sha3_256_empty_string(empty_string):
    target = Sha3PurePy.sha3_256(empty_string['value']).hexdigest()
    assert  target == empty_string['256'].replace(' ', '')


def test_sha3_256_small_string(small_string_length):
    target = Sha3PurePy.sha3_256(small_string_length['value']).hexdigest()
    assert  target == small_string_length['256'].replace(' ', '')


def test_sha3_256_medium_string(medium_string_length):
    target = Sha3PurePy.sha3_256(medium_string_length['value']).hexdigest()
    assert  target == medium_string_length['256'].replace(' ', '')


# def test_sha3_256_long_string(long_string_length):
#     target = Sha3PurePy.sha3_256(long_string_length['value']()).hexdigest()
#     assert  target == long_string_length['256'].replace(' ', '')