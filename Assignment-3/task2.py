# Task 2: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
    # o   Square root of the number
    # o   Natural logarithm (log base e) of the number
    # o   Sine of the number (in radians)
# 3.   Displays the calculated results.


import math
n=int(input("Enter the number:"))

sqrt=math.sqrt(n)
print(f"The square root of the number {n} is {sqrt}")

log=math.log(n)
print(f"The logarithm of the number {n} is {log}")

sin=math.sin(n)
print(f"The sine of the number {n} is {sin}")
