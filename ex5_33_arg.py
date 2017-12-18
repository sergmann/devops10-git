#!/bin/env python
from __future__ import print_function
import sys 
def param(a, b):
    if a <= 0 or b <= 0:
        print("Error! a or b must be > 0")
        exit(1)        
    else:
        res = a * b
        return print("Square is {}".format(res))

def main():
    param(int(sys.argv[1]),int(sys.argv[2]))

main()
