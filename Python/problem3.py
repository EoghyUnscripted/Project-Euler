# Project Euler Archive Practice
# https://projecteuler.net/problem=3

# Problem 3 - Largest Prime Factor
# SOLVED & VERIFIED VIA PROJECT EULER

# The prime factors of 13195 are 5, 7, 13 and 29 
# What is the largest prime factor of the number 600851475143?

def largestPrimeFactor(n):

    factor = 1 # Variable to store current highest factor in loop
    i = 2 # Variable to iterate through all numbers to test for primes

    while i <= n / i: # While iteration is less than input divided by current number
        if n % i == 0: # If number can be divided into the current number without remainders
            factor = i # Set current iteration number as highest factor
            n /= i  # Divides n by i to get current highest factor to print
        else:
            i += 1 # Iterate to next number to test

    if factor < n: # Checks that highest factor is less than input for validation
        factor = n # Set current n value to factor variable as highest factor

    return print(int(factor)) # Print the largest factor
    
largestPrimeFactor(600851475143) # Call function