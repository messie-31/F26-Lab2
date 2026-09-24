#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys
num_argv=len(sys.argv)-1
if num_argv==2:
    print("Hello user, good job, your provided two arguments!")
elif num_argv==0:
    print("This script requires exactly two arguments. No arguments were provided!")
else:
    print(f"This script requires exactly two arguments. You provided {num_argv} arguments.")