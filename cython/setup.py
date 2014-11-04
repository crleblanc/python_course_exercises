#from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize

setup(
  name = 'Mandelbrot example',
  ext_modules = cythonize("mandelbrot_cython.pyx"),
)