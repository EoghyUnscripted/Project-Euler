"""
Project Euler Archive Practice
https://projecteuler.net/problem=9

Problem 9 - Pythagorean Triplet
SOLVED & VERIFIED VIA PROJECT EULER

A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc
"""

def pythagoreanTriplet(n):

   for a in range(1, n): # Iterate A from 1 - n
        for b in range(1, n): # Iterate B from 1 - n
        
            c = (n - a) - b # Set value of C by subtracting A and B from n
        
            if a < b < c: # Checks if A is smaller than B is smaller than C
            
                if a**2 + b**2 == c**2: # Check if a^2 + b^2 = c^2
                    total = a+b+c
                    message = print(f"{a} + {b} + {c} = {total},\nAnd the product of abc is {a*b*c}.")
                    return message

pythagoreanTriplet(3000) # Call function