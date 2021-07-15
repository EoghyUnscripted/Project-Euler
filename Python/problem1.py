# Project Euler Archive Practice
# https://projecteuler.net/problem=1

# Problem 1 - Multiples of 3 and 5
# SOLVED & VERIFIED VIA PROJECT EULER

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def summingMultiples():

    multiples = [] # Create a blank list to store values

    for x in range(0, 1000): # Loop through numbers 0-1000

        if x % 3 ==0 or x % 5 == 0: # Check if each number is divisible by 3 or 5

            multiples.append(x) # Add number to list

    return print(sum(multiples)) # Return the sum of the list elements

summingMultiples() # Call function