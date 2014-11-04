# Cython implementation shamelessly ripped from http://www.vallis.org/salon/summary-10.html

import numpy as N
cimport numpy as N      # this Cython-side numpy import is needed
                        # to declare the types and dimensions of arrays

x0, x1 = -2.0, 1.0
y0, y1 = -1.0, 1.0

def mandel_cython(int n=400,int maxi=512):
    # declare the type and dimension of numpy arrays
    # (and create them in the same line, C-style)
    cdef:
        N.ndarray[double,ndim=1] xs = N.linspace(x0,x1,n)
        N.ndarray[double,ndim=1] ys = N.linspace(y0,y1,n)

        N.ndarray[int,ndim=2] escape = N.empty((n,n),'int32')

        # declare integer counters
        int i,j,it,esc

        # declare complex variables
        double complex z,c

    for i in range(n):
        for j in range(n):
            z = 0 + 0j
            c = xs[i] + 1j * ys[j]

            esc = maxi
            for it in range(maxi):
                z = z*z + c

                # let's allow ourselves one hand-tuned optimization,
                # which avoids the sqrt implicit in abs
                if z.real*z.real + z.imag*z.imag > 4:
                    esc = it
                    break

            escape[j,i] = esc

    return escape
