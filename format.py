#!/bin/env python
from __future__ import print_function

a = 1
b = 'another'

c = "A template with " + str(a) + " and " + b + " value."
print(c)  # A template with 1 and another value.

d = "A template with {} and {} value.".format(a,b)
print(d)
