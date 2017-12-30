# -*- coding: utf-8 -*-
# test_sha3_512.py

import pytest
from sha3purepy import Sha3PurePy

def test_sha3_512_abc(abc):
    target = Sha3PurePy.sha3_512(abc['value']).hexdigest()
    assert target == abc['512'].replace(' ', '')


def test_sha3_512_empty_string(empty_string):
    target = Sha3PurePy.sha3_512(empty_string['value']).hexdigest()
    assert  target == empty_string['512'].replace(' ', '')


def test_sha3_512_small_string(small_string_length):
    target = Sha3PurePy.sha3_512(small_string_length['value']).hexdigest()
    assert  target == small_string_length['512'].replace(' ', '')


def test_sha3_512_medium_string(medium_string_length):
    target = Sha3PurePy.sha3_512(medium_string_length['value']).hexdigest()
    assert  target == medium_string_length['512'].replace(' ', '')


# def test_sha3_512_long_string(long_string_length):
#     target = Sha3PurePy.sha3_512(long_string_length['value']()).hexdigest()
#     assert  target == long_string_length['512'].replace(' ', '')