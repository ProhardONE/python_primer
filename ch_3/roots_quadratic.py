# Exercise 3.3
# Author: Noah Waterfield Price
# Modified : Ahmed Wahba

def roots(a, b, c):
     const = (b * b - 4 * a * c)
    if const < 0:
    	from cmath import sqrt
    else:
    	from math import sqrt
    
    q = sqrt(const)
    x1 = (-b + q) / (2 * a)
    x2 = (-b - q) / (2 * a)
    return x1, x2

print roots(1, 3, 2)
print roots(1, -2, 3)

"""
Sample run:
python roots_quadratic.py
(-1, -2)
((1+1.4142135623730951j), (1-1.4142135623730951j))
"""
