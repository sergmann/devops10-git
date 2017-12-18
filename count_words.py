#!/bin/env python
from __future__ import print_function

def main():
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    objects = ['Moon','Gas giant','Ateroid','Dwarf planet','Asteroid','Moon','Asteroid']
    for object in objects:
        if object == 'Moon':
           count_1 = count_1 + 1 

        elif object == 'Gas giant':
           count_2 = count_2 + 1

        elif object == 'Asteroid':
           count_3 = count_3 + 1

        elif object == 'Dwart planet':
           coount_4 = count_4 + 1

        else:
           pass
               print("Moon ", count_1)
               print("Gas giant  ", count_2)
               print("Asteroid  ", count_3)
               print("Dwarf planet ", count_4)
main()
