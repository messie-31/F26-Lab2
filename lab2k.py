#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.
total=0
for i in range(1,101):
    if i%2==0:
        total+=1
print(f"The sum of all even numbers from 1 to 100 is: {total}")