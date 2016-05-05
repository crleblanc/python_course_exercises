# Cython version of simple Python total function

def total_cython(n):
    '''Calculate the sum of all numbers up to n'''
    cdef int a = 0        # Declare the type of a as integer
    cdef int i            # Declare the type of i as integer
    for i in range(n):    # Now loop through all the numbers
        a += i            # ... and add them
    return a