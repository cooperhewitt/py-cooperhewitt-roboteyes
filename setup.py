#!/usr/bin/env python

from setuptools import setup

setup(
    name='cooperhewitt.roboteyes',
    version='0.1',
    description='Meta package to install all the Cooper Hewitt computer vision libraries',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes',
    install_requires=[
        'cooperhewitt.roboteyes.atkinson'
        'cooperhewitt.roboteyes.shannon',
        'cooperhewitt.roboteyes.opencv'
    ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson/archive/v0.1.tar.gz#egg=cooperhewitt.roboteyes.atkinson-0.1',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-shannon/archive/v0.1.tar.gz#egg=cooperhewitt.roboteyes.shannon-0.1',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-opencv/archive/v0.1.tar.gz#egg=cooperhewitt.roboteyes.opencv-0.21',
      ],
    packages=[]
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes/releases/tag/v0.1',
    license='BSD')
