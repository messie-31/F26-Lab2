#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.
income=float(input("Enter your income: "))
status=input("Enter your status (single/married): ").strip().lower()

tax = 0.0

# Calculate tax using nested conditions based on status and income
if status == "single":
    if income <= 8000:
        tax = 0.10 * income
    elif income <= 32000:
        tax = 800 + 0.15 * (income - 8000)
    else:
        tax = 4400 + 0.25 * (income - 32000)

elif status == "married":
    if income <= 16000:
        tax = 0.10 * income
    elif income <= 64000:
        tax = 1600 + 0.15 * (income - 16000)
    else:
        tax = 8800 + 0.25 * (income - 64000)

else:
    print("Invalid status.")

print(f"Calculated Tax: {tax:.2f}")
