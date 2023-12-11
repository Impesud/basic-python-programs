# https://github.com/Impesud/basic-python-programs
# Write a Python program to solve quadratic equation
'''
The values of the roots depend on the term (b2 - 4ac) which is known as the discriminant (D). 
We have three cases of discriminant as given below:

Case 1: D > 0 (b*b > 4*a*c)

    Roots are real and different
    The roots are {-b + √(b2 - 4ac)}/2a and {-b - √(b2 - 4ac)}/2a
    For example, roots of x2 - 7x - 12 are 3 and 4

Case 2: D < 0 (b*b < 4*a*c)

    Roots are complex (not real)
    The discriminant can be written as (-1 * -D).
    As D is negative, -D will be positive.
    The roots are {-b ± √(-1*-D)} / 2a = {-b ± i√(-D)} / 2a = {-b ± i√-(b2 - 4ac)}/2a where i = √-1.
    For example roots of x2 + x + 1, roots are -0.5 + i1.73205 and -0.5 - i1.73205

Case 3: D = 0 (b*b == 4*a*c)

    Roots are real and equal
    The roots are (-b/2a)
    For example, roots of x2 - 2x + 1 are 1 and 1
'''

import math
# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Calculate the discriminant
discriminant = b*b - 4*a*c
# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (a*a)
    root2 = (-b - math.sqrt(discriminant)) / (a*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (a*a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (a*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
