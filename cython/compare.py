#!/usr/bin/env python

# Comparison of Python/Numpy version of the mandelbrot versus a basic Cython implementation,
# more for a Cython demo than a performance comparison.

from __future__ import print_function
import time
from matplotlib import pylab as plt
from mandelbrot_python import mandel_numpy
from mandelbrot_cython import mandel_cython

def compare_runs():
    n_pixels = 500
    max_iterations = 100
    t1 = time.time()
    py_output = mandel_numpy(n_pixels, max_iterations)
    t2 = time.time()
    cy_output = mandel_cython(n_pixels, max_iterations)
    t3 = time.time()

    print("Time for python=%f second, %f for cython." % (t2-t1, t3-t2))

    # plot results
    f, axes = plt.subplots(2)
    axes[0].imshow(py_output)
    axes[1].imshow(cy_output)
    plt.show()

if __name__ == '__main__':
    compare_runs()

