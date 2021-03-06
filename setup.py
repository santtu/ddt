#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from ddt import __version__

setup(
    name='ddt',
    description='Data-Driven/Decorated Tests',
    long_description='A library to multiply test cases',
    version=__version__,
    author='Carles Barrobés',
    author_email='carles@barrobes.com',
    url='https://github.com/txels/ddt',
    py_modules=['ddt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ],
)

