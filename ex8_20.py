#!/bin/env python

from __future__ import print_function
import sys
import random
def game():
	b = random.randint(1,21)
	i = 1
	while i < 5:
        	i +=1
		a = int(input("Enter a number: "))
		print("user's number {}".format(a))
		print("generated number {}".format(b))
                
                
		if a > b:
			print("your number is bigger.")
                
		elif a < b:
			print("your number is smaller.")
                
		else:
                	print("you guessed")
                	exit()
                game()
game()
