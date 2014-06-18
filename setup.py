#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = open(os.path.join(this_dir, 'README.rst')).read()

setup(
    name='parameterizedtestcase',
    version='0.1.0',
    description="""Parameterized tests for Python's unittest module""",
    long_description=long_description,
    keywords='unittest',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='https://github.com/msabramo/python_unittest_parameterized_test_case',
    packages=['parameterizedtestcase'],
    test_suite='parameterizedtestcase.tests',
    use_2to3=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ]
)
