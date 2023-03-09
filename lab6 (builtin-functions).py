#1. Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x*y, numbers)

print(product) # Output: 120

#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
string = "Hello World"

bolsh_count = sum(1 for char in string if char.isupper())
men_count = sum(1 for char in string if char.islower())

print(bolsh_count)
print(men_count)

#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not
string = "racecar"

if list(string) == list(reversed(string)):
    print("Palindrome")
else:
    print("Not Palindrome")

#4. Write a Python program that invoke square root function after specific milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math

number = 25100
milliseconds = 2123

time.sleep(milliseconds/1000)
result = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
my_tuple = (True, True, 1, 1)

if all(my_tuple):
    print("All elements are true")
else:
    print("At least one element is false")