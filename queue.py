#!/bin/env python

from __future__ import print_function

def main():
    L = []
    i = 0
    while True:

        name = raw_input(": ")
        if name == 'n':
           if i == len(L):
               print("the queue is empty")
           else:
               print(L[i])
               i = i + 1      
        else:
            L.append(name)
        print(L)
            
main()
