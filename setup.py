# -*- coding: utf-8 -*-
# setup.py


from setuptools import setup

setup(
    name='sha3purepy',
    version='0.1',
    description='pure python implementation of keccak sha3 hashing',
    url='https://github.com/inigo-montoya/sha3-pure-py',
    author='Joshua Lederman',
    author_email='joshuab.lederman@gmail.com',
    license='GNU',
    packages=['sha3_purepy'],
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False)

