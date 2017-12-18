#!/bin/env python

def main():
    numbers = [123, 1256, 3456, 98]
    count = [0] * 10
    print(count)
    print(numbers)
    for n in numbers:
        for d in str(n):
            count[int(d)] += 1
    for d in range(0,10):
        print("{}   {}".format(d,count[d]))        
main()
