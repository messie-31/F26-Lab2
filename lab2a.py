#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
x=input("Enter a number: ")
type(x)
x=int(x)
if x>=6:
    print("x is greater than 6!")
else:
    print("x is lesser than 6!")

if x>=4 and x<12:
    print("x lies in the range of 4 and 12!")