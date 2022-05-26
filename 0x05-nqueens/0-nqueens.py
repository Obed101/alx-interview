#!/usr/bin/python
"""This program solves the N-QUEENS problem"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

arg = sys.argv[1]

if type(arg) is not int:
    print("N must be a number")
    sys.exit(1)

if not (arg >= 4):
    print("N must be at least 4")
    sys.exit(1)


