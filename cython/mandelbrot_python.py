# Python/NumPy implementation shamelessly ripped from http://www.vallis.org/salon/summary-10.html

import numpy as N

x0, x1 = -2.0, 1.0
y0, y1 = -1.0, 1.0

def mandel_numpy(n=400,maxi=512):
    """Compute an n x n Mandelbrot matrix with maxi maximum iterations."""

    # get 2-d arrays for x and y, using numpy's convenience function 
    xs, ys = N.meshgrid(N.linspace(x0,x1,n), N.linspace(y0,y1,n))

    z = N.zeros((n,n),'complex128')     # a matrix of complex zeros
    c = xs + 1j*ys

    escape = N.empty((n,n),'int32')
    escape[:,:] = maxi                  # default result

    for i in range(1, maxi):
        mask = (escape == maxi)         # find out which points have not escaped
                                        # yet (results in a boolean array)

        z[mask] = z[mask]**2 + c[mask]  # run the Mandelbrot iteration only
                                        # on those points, using boolean indexing

        escape[mask & (N.abs(z) > 2)] = i   # if are just escaping now,
                                            # set the result to this iteration

    return escape

