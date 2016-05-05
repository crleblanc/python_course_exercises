#from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize
# build with python setup.py build_ext --inplace

setup(
  name = 'Totals example',
  ext_modules = cythonize("total.pyx"),
)
