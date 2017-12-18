#!/bin/env python
from __future__ import print_function

L1 = [ int(i) for i in input().split() ]
L2 = [ int(i) for i in input().split() 
L1 = set(L1)
L2 = set(L2)
L3 = L1&L2
L3 = list(L3)
print(L3)
