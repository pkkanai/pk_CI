from setuptools import setup, find_packages
import sys


setup(
    name = 'Hoge',
    version = '0.2',
    description='This is test codes for travis ci',
    packages = find_packages(),
    test_suite = 'testCi.suite'
)
