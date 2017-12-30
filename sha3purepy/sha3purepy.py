#! /usr/bin/env python
# coding: utf-8

# The Keccak sponge function was designed by Guido Bertoni, Joan Daemen,
# Michaël Peeters and Gilles Van Assche. For more information, feedback or
# questions, please refer to their website: http://keccak.noekeon.org/
#
# Based on the implementation by Renaud Bauvin,
# from http://keccak.noekeon.org/KeccakInPython-3.0.zip
#
# Modified by Moshe Kaplan to be hashlib-compliant
#
# To the extent possible under law, the implementer has waived all copyright
# and related or neighboring rights to the source code in this file.
# http://creativecommons.org/publicdomain/zero/1.0/


import keccak

class Sha3PurePy:

    @staticmethod
    def sha3_224(data=None):
        return keccak.Sha3_224(data)


    @staticmethod
    def sha3_256(data=None):
      return keccak.Sha3_256(data)

    @staticmethod
    def sha3_384(data=None):
      return keccak.Sha3_384(data)

    @staticmethod
    def sha3_512(data=None):
      return keccak.Sha3_512(data)
