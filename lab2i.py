#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# TO DO 1: 
# Follow the specific instructions given in the README.md file.
pin=input("Please type in your PIN: ")
while pin!= "1234":
    print("Incorrect guess, try again...")
    pin=input("Please type in your PIN: ")

print("Correct PIN, you can enter!")