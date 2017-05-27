#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mapkit',
      version='1.0',
      description='A Python library for map integration.',
      author='Bennett Murphy',
      author_email='murphy214@live.marshall.edu',
      url='https://github.com/murphy214/mapkit',
      packages=['mapkit'],
      install_requires = [#'nlgeojson',
      						'pipeleaflet',
      						'pipevts',
      						'pipegls',
      						'future',
      						'geopandas',
      						'numpy',
      						'pandas',
      						'python-geohash >= 0.8.5'
      						],

      scripts = ['bin/myfreeport'],
      dependency_links=['http://github.com/murphy214/nlgeojson/tarball/master#egg=package-1.0']

      )