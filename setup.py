# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

from version import get_version

setup(
    name='miss',
    version=get_version(),
    description='A collection of generic functions and classes',
    author='Changaco',
    author_email='changaco ατ changaco δοτ net',
    url='http://changaco.net/gitweb/?p=python-miss.git',
    license='LGPLv3+',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README')).read(),
)
