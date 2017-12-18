#!/bin/env python

from __future__ import print_function
import sys

def main():
    L = ['blue','green','yellow','white']
    number = int(raw_input("enter a number[1,2,3,4]: "))
    if number >= 0 or number <= 4:
        print(L[number - 1])
    else: 
        print("enter a number from 1 to 4") 
main()
