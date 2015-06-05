NAME         = 'MechBook'
DESCRIPTION  = 'Anonymous Identifier using Mechanize on Facebook'
AUTHOR       = 'Vlall'
URL          = 'http://github.com/vlall/MechBook'
LICENSE      = 'GPLv3'
VERSION      = '0.1'

if __name__ == "__main__":

    from setuptools import setup, Extension, find_packages
    #from distutils.core import setup, Extension
    
    setup(
          install_requires = ['numpy>=1.7.1', # 1.7.0 contains a memory leak bug fixed in 1.7.1
                              'scipy>=0.11.0',
                              #'scikits.sparse>=0.1', # required for sparse GPs only
                              'matplotlib>=1.2.0',
                              'h5py'],

          cmdclass = {'build_ext': build_ext},
          ext_modules = [sparse_distance],
          
          packages = find_packages(),
                      ['MechBook',
                       'MechBook.demos',
                       'MechBook.nodes',
                       'bayespy.plot',
                       'MechBook.utils',
                       'MechBook.utils.tests',

          name             = NAME,
          version          = VERSION,
          author           = AUTHOR,
          description      = DESCRIPTION,
          license          = LICENSE,
          url              = URL,
          long_description = LONG_DESCRIPTION,
          classifiers =
            [ 
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Development Status :: 2 - Pre-Alpha',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Scientific/Engineering',
              'Topic :: Scientific/Engineering :: Information Analysis'
            ]
          )

