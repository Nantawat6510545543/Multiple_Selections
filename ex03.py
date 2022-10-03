import sys
from math import sqrt


def is_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


def is_right_triangle(x, y, z):
    return (sqrt(x ** 2 + y ** 2) == z) or (sqrt(x ** 2 + z ** 2) == y) or (
                sqrt(y ** 2 + z ** 2) == x)


def read_nonnegative(msg):
    number = float(input(msg))
    if number < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()
    else:
        return number


a = read_nonnegative("Enter 1st line's length: ")
b = read_nonnegative("Enter 2nd line's length: ")
c = read_nonnegative("Enter 3rd line's length: ")

if is_triangle(a, b, c):
    if is_right_triangle(a, b, c):
        print("It's a right triangle.")
    else:
        print("It's a triangle but not a right triangle.")
else:
    print("It's not a triangle.")
