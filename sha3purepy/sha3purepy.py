#! /usr/bin/env python
# coding: utf-8

# The Keccak sponge function was designed by Guido Bertoni, Joan Daemen,
# Michaël Peeters and Gilles Van Assche. For more information, feedback or
# questions, please refer to their website: http://keccak.noekeon.org/
#
# Based on the implementation by David Leon Gil
# https://github.com/coruus/py-keccak
#
# This is the FIPS202 compliant SHA3 functions
#
# Modified by Joshua Lederman to test against FIPS vectors
#
# To the extent possible under law, the implementer has waived all copyright
# and related or neighboring rights to the source code in this file.
# http://creativecommons.org/publicdomain/zero/1.0/


import keccak


class Sha3PurePy:
    """Wrapper class for ease of use and naming
    """
    @staticmethod
    def sha3_224(data=None):
        """
        Generate the SHA3 224 hash

        :param data: String to be hashed
        :return: Keccack object
        """
        return keccak.Sha3_224(data)

    @staticmethod
    def sha3_256(data=None):
        """
        Generate the SHA3 256 hash

        :param data: String to be hashed
        :return: Keccack object
        """
        return keccak.Sha3_256(data)

    @staticmethod
    def sha3_384(data=None):
        """
        Generate the SHA3 384 hash

        :param data: String to be hashed
        :return: Keccack object
        """
        return keccak.Sha3_384(data)

    @staticmethod
    def sha3_512(data=None):
        """
        Generate the SHA3 512 hash

        :param data: String to be hashed
        :return: Keccack object
        """
        return keccak.Sha3_512(data)
