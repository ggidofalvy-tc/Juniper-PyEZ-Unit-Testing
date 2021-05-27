#!/usr/bin/python

from setuptools import setup, find_packages

version = '0.4'

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(name='pyez_mock',
      version=version,
      author='Christian Giese',
      author_email='cgiese@juniper.net',
      url='https://github.com/GIC-de/Juniper-PyEZ-Unit-Testing',
      license='MIT License',
      description='PyEZ Device Mock',
      long_description=open('README.md').read(),
      packages=find_packages(exclude=['tests']),
      keywords=['juniper', 'pyez', 'pytest'],
      zip_safe=True,
      requirements=True,
      install_requires=install_requires
      )
