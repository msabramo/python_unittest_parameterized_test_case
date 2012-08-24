#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = open(os.path.join(this_dir, 'README.md')).read()

setup(
    name='parameterizedtestcase',
    version='0.0.0',
    description="""Parameterized tests for Python's unittest module""",
    long_description=long_description,
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='https://github.com/msabramo/python_unittest_parameterized_test_case',
    py_modules=['parameterizedtestcase'],
    test_suite='tests',
    use_2to3=True,
    license='MIT',
)
