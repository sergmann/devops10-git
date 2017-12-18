#!/bin/env python

from __future__ import print_function

f = open('numbers.txt')
lines_str = f.read()
L = lines_str.split(' ')
print(L)
print(lines_str)
print(len(lines_str))

