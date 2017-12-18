#!/bin/env python

def main():
    lines = ['ab cde','x yz qwerty','abc x cde abc d er']
    collector = []
    for l in lines:
        collector.extend(l.split(' '))
        print(collector)
main()
