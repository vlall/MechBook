#!/usr/bin/env python

NAME         = 'MechBook'
DESCRIPTION  = 'Anonymous Identifier using Mechanize on Facebook'
AUTHOR       = 'Vlall'
URL          = 'http://github.com/vlall/MechBook'
LICENSE      = 'GPLv3'
VERSION      = '0.1'

if __name__ == "__main__":

    import os

    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    from setuptools import setup, find_packages
    
    setup(
          install_requires = ['numpy>=1.8.0', # 1.8 implements broadcasting in numpy.linalg
                              'mechanize>=0.2.5',
                              ],
          
          packages         = find_packages(),
          name             = NAME,
          version          = VERSION,
          author           = AUTHOR,
          description      = DESCRIPTION,
          license          = LICENSE,
          url              = URL,
          long_description = read('README.md'),
          keywords         =
            [
              'mechanize facebook',

            ],
          classifiers =
            [ 
              'Programming Language :: Python',
              'Topic :: Scientific/Engineering :: Information Analysis'
            ]
          )
