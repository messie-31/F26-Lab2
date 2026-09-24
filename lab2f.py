#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-09-23
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file
import sys
num_argv=len(sys.argv)-1
if num_argv<2:
    print("The script requires at least 2 arguments.")
else:
    name=sys.argv[1]
    age=sys.argv[2]
    if num_argv==2:
        print(f"Hi {name}, you are {age} years old and you provided exacltly two arguments!")
    else:
        print(f"Hi {name}, you are {age} years old and the script received {num_argv} arguments.")
