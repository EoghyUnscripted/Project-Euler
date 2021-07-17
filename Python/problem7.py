"""
Project Euler Archive Practice
https://projecteuler.net/problem=7

Problem 7 - 10001st Prime
SOLVED & VERIFIED VIA PROJECT EULER

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def tenThousandOnePrime(count):

    primes_List = [] # Create blank list to store prime numbers
    n = 2 # Set variable to iterate and find the prime numbers

    while len(primes_List) != count: # While the primes_List length is less than 10002
        for i in range(2, n // 2 + 1):
            if n % i == 0: # Check for even numbers
                break # Ends current loop
        else:
            primes_List.append(n) # Appends prime number to list
        n += 1 # Increments to next number to test if prime

    return print(primes_List[10000]) # Return 10001st prime number

tenThousandOnePrime(10002) # Call function