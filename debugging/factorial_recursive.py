#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert it to an integer,
# and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)