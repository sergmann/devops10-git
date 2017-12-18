#!/bin/env python

from __future__ import print_function, division
import sys

def calc(a, b, c):
	if c == '+':
		res = a+b

        elif c == '-':
                res = a-b

        elif c == '/':
                res = a*b

        elif c == '*':
                res = a/b
        else:
		print("Invalid operator!")
                exit()   
        print(res)    
def main():
	calc(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])

main()
