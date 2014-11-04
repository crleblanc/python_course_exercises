#!/usr/bin/env python
# Demo using f2py to call Fortran code from Python.
# Use "f2py -c -m fib3 fib3.f" to create the Python extension module.

import numpy as np
# the Fibonacci module created by f2py:
import fib3

def main():
    n_points = 500
    worker_array = np.zeros(n_points, dtype=np.double)

    # Fortran subroutine fib(a, n) expects a real*8 arrray 'a' with 'n' elements (optional, f2py knows this value).
    # It will modify this array in-place.
    fib3.fib(worker_array, worker_array.size)

    # Hopefully we see the fibonacci series output
    print worker_array

if __name__ == '__main__':
    main()