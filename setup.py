#!/usr/bin/env python

from distutils.core import setup

setup(name='cooperhewitt-roboteyes',
      version='0.1',
      description='Meta package to install all the Cooper Hewitt computer vision libraries',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes',
      requires=[
        'cooperhewitt.roboteyes.atkinson'
        'cooperhewitt.roboteyes.shannon',
        'cooperhewitt.roboteyes.opencv'
        ],
      packages=[]
      scripts=[],
      download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes/releases/tag/v0.1',
      license='BSD')
