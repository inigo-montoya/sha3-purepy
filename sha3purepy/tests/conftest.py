# -*- coding: utf-8 -*-
# conftest.py

import pytest

@pytest.fixture
def abc():
    vector_abc = {
                  'value': 'abc',
                  '224': 'e642824c3f8cf24a d09234ee7d3c766f c9a3a5168d0c94ad 73b46fdf',
                  '256': '3a985da74fe225b2 045c172d6bd390bd 855f086e3e9d525b 46bfe24511431532',
                  '384': 'ec01498288516fc9 26459f58e2c6ad8d f9b473cb0fc08c25 96da7cf0e49be4b2 98d88cea927ac7f5 39f1edf228376d25',
                  '512': 'b751850b1a57168a 5693cd924b6b096e 08f621827444f70d 884f5d0240d2712e 10e116e9192af3c9 1a7ec57647e39340 57340b4cf408d5a5 6592f8274eec53f0'
                  }
    return vector_abc


@pytest.fixture
def empty_string():
    vector_empty_string = {
                  'value': '',
                  '224': '6b4e03423667dbb7 3b6e15454f0eb1ab d4597f9a1b078e3f 5b5a6bc7',
                  '256': 'a7ffc6f8bf1ed766 51c14756a061d662 f580ff4de43b49fa 82d80a4b80f8434a',
                  '384': '0c63a75b845e4f7d 01107d852e4c2485 c51a50aaaa94fc61 995e71bbee983a2a c3713831264adb47 fb6bd1e058d5f004',
                  '512': 'a69f73cca23a9ac5 c8b567dc185a756e 97c982164fe25859 e0d1dcc1475c80a6 15b2123af1f5f94c 11e3e9402c3ac558 f500199d95b6d3e3 01758586281dcd26'
                  }
    return vector_empty_string


@pytest.fixture
def small_string_length():
    vector_abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq = {
                  'value': 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq',
                  '224': '8a24108b154ada21 c9fd5574494479ba 5c7e7ab76ef264ea d0fcce33',
                  '256': '41c0dba2a9d62408 49100376a8235e2c 82e1b9998a999e21 db32dd97496d3376',
                  '384': '991c665755eb3a4b 6bbdfb75c78a492e 8c56a22c5c4d7e42 9bfdbc32b9d4ad5a a04a1f076e62fea1 9eef51acd0657c22',
                  '512': '04a371e84ecfb5b8 b77cb48610fca818 2dd457ce6f326a0f d3d7ec2f1e91636d ee691fbe0c985302 ba1b0d8dc78c0863 46b533b49c030d99 a27daf1139d6e75e'
              }
    return vector_abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq


@pytest.fixture
def medium_string_length():
    vector_abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu= {
                  'value': 'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu',
                  '224': '543e6868e1666c1a 643630df77367ae5 a62a85070a51c14c bf665cbc',
                  '256': '916f6061fe879741 ca6469b43971dfdb 28b1a32dc36cb325 4e812be27aad1d18',
                  '384': '79407d3b5916b59c 3e30b09822974791 c313fb9ecc849e40 6f23592d04f625dc 8c709b98b43b3852 b337216179aa7fc7',
                  '512': 'afebb2ef542e6579 c50cad06d2e578f9 f8dd6881d7dc824d 26360feebf18a4fa 73e3261122948efc fd492e74e82e2189 ed0fb440d187f382 270cb455f21dd185'
              }
    return vector_abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu

@pytest.fixture
def long_string_length():
    vector_million_a= {
                  'value': (lambda: 'a' * 1000000),
                  '224': 'd69335b93325192e 516a912e6d19a15c b51c6ed5c15243e7 a7fd653c',
                  '256': '5c8875ae474a3634 ba4fd55ec85bffd6 61f32aca75c6d699 d0cdcb6c115891c1',
                  '384': 'eee9e24d78c18553 37983451df97c8ad 9eedf256c6334f8e 948d252d5e0e7684 7aa0774ddb90a842 190d2c558b4b8340',
                  '512': '3c3a876da14034ab 60627c077bb98f7e 120a2a5370212dff b3385a18d4f38859 ed311d0a9d5141ce 9cc5c66ee689b266 a8aa18ace8282a0e 0db596c90b0a7b87'
              }
    return vector_million_a
