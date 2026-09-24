#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
str1=input("Enter first line: ")
str2=input("Enter second line: ")

# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
if len(str1)>len(str2):
    print("Line 1 is longer than Line 2.")
elif len(str2)>len(str1):
    print("Line 2 is longer than Line 1.")
else:
    print("Line 1 and Line 2 are equal.")