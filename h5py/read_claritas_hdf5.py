#!/usr/bin/env python
#
# Read in a Claritas format HDF5 file and see what's there.  GLOBE Claritas
# uses HDF5 for it's internal data format.  Open an example file and look at the
# data and trace headers.

from __future__ import print_function
import numpy as np
import h5py
import pandas as pd
from matplotlib import pyplot as plt


def main():
    with h5py.File('test_shot.h5', 'r') as h5file:

        # quick access to objects that act like NumPy arrays, but only read from disk when necessary
        trace_data = h5file['/TRACE_DATA/DEFAULT/data_array']
        trace_headers = h5file['/TRACE_DATA/DEFAULT/trace_headers']

        # Make a Pandas object out of the 'record array' like object from h5py
        headers_dframe = pd.DataFrame(np.array(trace_headers))

        print(headers_dframe)

        # display the amplitudes
        trace_array = np.array(trace_data)

        fig = plt.figure(figsize=(20, 10))
        plt.imshow(trace_array.T, cmap=plt.cm.gray, aspect=0.01)
        plt.show()

if __name__ == '__main__':
    main()