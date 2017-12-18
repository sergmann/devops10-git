#!/bin/env python
from __future__ import print_function
a = int(input())
b = int(input())

if a <= 0 or b <= 0:
  	print("Error! a or b must be > 0")
        exit(1)        
else:
	res = a * b
print("Square is {}".format(res))

