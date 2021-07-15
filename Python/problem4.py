# Project Euler Archive Practice
# https://projecteuler.net/problem=4

# Problem 4 - Largest Palindrome Product
# SOLVED & VERIFIED VIA PROJECT EULER

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindrome():

    palindromes = [] # Create blank list to store palindromes

    for x in range(100,1000): # Loop through 3 digit numbers for first number
        for y in range(100,1000): # Loop through 3 digit numbers for second number
            
            if str(x*y) == str(x*y)[::-1]: # Check if product is palindrome
                palindromes.append(x*y) # Append to palindrome list

    return print(max(palindromes)) # Output the largest palindrome from list

largestPalindrome() # Call function