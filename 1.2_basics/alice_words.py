#!/usr/bin/env python

from __future__ import print_function
import argparse

# Exercise: Write a python program that accepts a command line argument
# for a filename (alice_in_wonderland.txt).  Create a function that opens this
# file and counts the number of unique words (lowercase) without punctuation.
# Finally print the word and the number of times it occurs, ordered from most
# common to least common.
#
# Hint: Look into collections.Counter() for a time saving feature:
# https://docs.python.org/2/library/collections.html#counter-objects
#
# Note: alice_in_wonderland.txt freely available from http://www.gutenberg.org

# Some help in getting started.  Using argparse to parse command line args
def command_line_args():
    parser = argparse.ArgumentParser( description='Unique words in Alice in Wonderland')
    parser.add_argument( '-i', '--input', dest='input_file', type=str, help='Input file to be scanned')
    args = parser.parse_args()
    return args



if __name__ == '__main__':

    # A simple alternative to argparse is to use sys.argv, but this requires more error handling.
    args = command_line_args()

    print('argparse input_file:', args.input_file)
