#!/usr/bin/env python

from setuptools import setup

setup(
    name='cooperhewitt.roboteyes',
    version='0.11',
    description='Meta package to install all the Cooper Hewitt computer vision libraries',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes',
    install_requires=[
        'cooperhewitt.roboteyes.atkinson',
        'cooperhewitt.roboteyes.colors',
        'cooperhewitt.roboteyes.opencv',
        'cooperhewitt.roboteyes.shannon',
    ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson/tarball/master#egg=cooperhewitt.roboteyes.atkinson-0.1',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-colors/tarball/master#egg=cooperhewitt.roboteyes.colors-0.1',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-opencv/tarball/master#egg=cooperhewitt.roboteyes.opencv-0.21',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-shannon/tarball/master#egg=cooperhewitt.roboteyes.shannon-0.1',
      ],
    packages=[]
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes/releases/tag/v0.11',
    license='BSD')
