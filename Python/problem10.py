"""
Project Euler Archive Practice
https://projecteuler.net/problem=10

Problem 10 - Summation of Primes
SOLVED & VERIFIED VIA PROJECT EULER

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million

NOTE: Unable to test for 1m or 2m output due to time to process
      the calculations - assuming based on correct ouput for the
      limits of 1000, 10000, 100000 that this program functions
      as expected to find and calculate correct sums of the primes.

      May be possible to enhance the program for optimum processing
      to be able to calculate for larger sums without the need of
      higher CPU capacity.

      Total time to compute sum all primes below 100000: 22 seconds
"""

def sumOfPrimes(count):

    primes = 0 # Create blank variable to sum all prime numbers
    n = 2 # Set variable to iterate and find the prime numbers

    while n < count: # While the primes_List length is less than 2m
        for i in range(2, n // 2 + 1):
            if n % i == 0: # Check for even numbers to skip
                break # Ends current loop
        else:
            primes += n # Appends prime number to list
        n += 1 # Increments to next number to test if prime

    return print(primes) # Print the sum of the primes

sumOfPrimes(1000) # Call functionß