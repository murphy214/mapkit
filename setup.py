#!/usr/bin/env python

from setuptools import setup, find_packages
import os
setup(name='mapkit',
      version='1.0',
      description='A Python library for map integration.',
      author='Bennett Murphy',
      author_email='murphy214@live.marshall.edu',
      url='https://github.com/murphy214/mapkit',
      packages=['mapkit'],
      #dependency_links=['http://github.com/murphy214/nlgeojson/tarball/master#egg=package-1.0'],#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']

      install_requires = ['future',
      						'geopandas',
      						'numpy',
      						'pandas',
      						'python-geohash >= 0.8.5',
                                          'ipython < 6.0',
                                          "mercantile",
                                          "psycopg2",
                                          "simplejson",
                                          "enum",
                                          'shapely',
                                          'mercantile',
                                          'sqlalchemy'
      						],
      dependency_links = ['http://github.com/murphy214/nlgeojson/tarball/master#egg=nlgeojson-1.1.0',
      'http://github.com/murphy214/pipeleaflet/tarball/master#egg=pipeleaflet-1.1.0',
     'http://github.com/murphy214/pipegls/tarball/master#egg=pipegls-1.0.0',
     'http://github.com/murphy214/pipevts/tarball/master#egg=pipevts-1.0.0',
     'http://github.com/murphy214/pipegeohash/tarball/master#egg=pipegeohash-1.2.0',
     'http://github.com/murphy214/smalltalk/tarball/master#egg=smalltalk-1.0.0'],

      scripts = ['bin/myfreeport'],
      #dependency_links=['http://github.com/murphy214/nlgeojson.git#egg=nlgeojson-1.0']#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']

      )

# delete this better for use locally
#os.system('pip install -r requirements.txt')
