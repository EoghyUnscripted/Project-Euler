"""
Project Euler Archive Practice
https://projecteuler.net/problem=6

Problem 6 - Sum Square Difference
SOLVED & VERIFIED VIA PROJECT EULER

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 
3025 − 385 = 2640

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

def sumSquareDifference():

    sumSquares = [] # Create blank list for storing product of summed squares
    total = 0 # Set default for variable to store total sums

    for x in range(1,101): # Loop 1-100
        sqrt = x * x # Square each number
        sumSquares.append(sqrt) # Append each squared number to the list
        sumSqrs = sum(sumSquares) # Get the total sum of squared numbers from list

    for y in range(1,101): # Loop 1-100
        total += y # Add all numbers from 1-100
        sqrdSums = total * total # Square the total sum to get product

    # Check for larger number
    if sqrdSums > sumSqrs:
        return print(sqrdSums - sumSqrs) # Return the difference
    else:
        return print(sumSqrs - sqrdSums) # Return the difference

sumSquareDifference() # Call function