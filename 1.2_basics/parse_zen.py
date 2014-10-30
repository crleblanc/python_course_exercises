#!/usr/bin/env python
# Note: the line above tells the shell how to run this file.  Not mandatory but recommended.

# Exercise: Parse each word in the string called zen (already created below as a multiline string)
# and print out all words that start with the letter "i" or "I".
#
# Hints: Use string.split() to split each word, and use a for 
# loop to loop over them testing the first character of each word.

zen="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# One possible answer.  Splitting on whitespace:
for word in zen.split():
    #if word[0] == 'i' or word[0] == 'I':
    #if word[0] in ('i', 'I'):
    word_lowercase = word.lower()
    if word_lowercase.startswith('i'):
        print word

# Another way using list comprehension
print [x for x in zen.split() if x.startswith('i')]

# reading from a file, reading line by line:
with open('zen.txt', 'r') as zen_file:
    for line in zen_file.readlines():
        for word in line.split():
            word_lowercase = word.lower()
            if word_lowercase.startswith('i'):
                print word