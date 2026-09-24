#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO:
import math
while True:
    num=input("Please type in a number: ")
    if not num.strip():
        continue
    num=float(num)
    if num<0:
        print("Invalid number.\n")
        continue
    elif num==0:
        print("Existing...")
        break
    result=math.sqrt(num)
    print(f"{result}\n")