#!/usr/bin/env python

from __future__ import print_function
import argparse
import collections

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
    parser.add_argument( '-i', '--input', dest='input_file', required=True, type=str, help='Input file to be scanned')
    args = parser.parse_args()
    return args

def count_words(input_file):
    # a dictionary with key:value pairs of word:count.
    word_count = {}

    with open(input_file, 'r') as file_obj:
        # loop over each line, in case the file is too big to fit in RAM using .read().
        # The following is the same as .readlines():
        for line in file_obj:

            # replace dashes with whitespace
            line = line.replace('-', ' ')

            # split on whitespace
            words = line.split()

            for word in words:
                # filter out non alphabetical characters using filter.
                word = filter(str.isalpha, word)

                # different approach with same result:
                #words = ''.join(x for x in words if x.isalpha)

                if len(word) == 0:
                    continue

                # make all words lowercase for easy comparison
                word = word.lower()

                # Check to see if the key exists already and increment.
                # Otherwise create a new key and set to one.
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Counter is a generator, so we loop over this object to get it's results
    return collections.Counter(word_count).most_common()


if __name__ == '__main__':

    # A simple alternative to argparse is to parse sys.argv, but this requires more error handling.
    args = command_line_args()

    for word, count in count_words(args.input_file):
        print(word, count)
