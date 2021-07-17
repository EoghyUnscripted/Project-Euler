# Project Euler Archive Practice
# https://projecteuler.net/problem=9

# Problem 9 - Pythagorean Triplet
# SOLVED & VERIFIED VIA PROJECT EULER

# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which, a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000
# Find the product abc

def pythagoreanTriplet(n):

    a, b, c = 1, 2, 3
    a2, b2, c2 = a**2, b**2, c**2
    triplet_Top = a2 + b2 + c2
    test = b**2
    triplet_List = []

    print(triplet_Top)

    while triplet_Top < n + 1:
        if triplet_Top == n:
            triplet_List.append(a)
            triplet_List.append(b)
            triplet_List.append(c)
            return print(triplet_List)
        elif triplet_Top < n:
            a += 1
            b += 1
            c += 1
            a2, b2, c2 = a**2, b**2, c**2
            triplet_Top = a2 + b2 + c2

            print(triplet_Top)
    
    print(triplet_List)

pythagoreanTriplet(1000) # Call function