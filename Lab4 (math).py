# Python Math library
# 1. Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904
import math
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", radian)


# 2. Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
import math
height = float(input("Height: "))
firstbase = float(input("Base, first value: "))
secondbase = float(input("Base, second value: "))
area = ((firstbase + secondbase) / 2) * height
print("Expected Output: ", area)


# 3. Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
import math
sides = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = sides * (length ** 2) / (4 * math.tan(math.pi / sides))
print("The are of the polygon is: ", area)
print()

# 4. Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
import math
length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = length * height
print("Expected Output: ", area)
