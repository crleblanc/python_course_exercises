#from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize
# build with python setup.py build_ext --inplace

setup(
  name = 'Mandelbrot example',
  ext_modules = cythonize("mandelbrot_cython.pyx"),
)