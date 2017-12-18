#!/bin/env python
#int(input())
def rec(n):
    print(n)
    if n < 4:
        rec(n+1)
        print(n)        
rec(1)
