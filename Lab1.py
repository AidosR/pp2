"""
Python Intro
Python User Input
Python Get Started
Python Syntax
Python Comments
Python Variables
Python Data Types
Python Numbers
Python Casting
Python Strings
Python String Formatting
Python Booleans
Python Operators
Python If...Else
Git
"""
#Python Intro
print("Hello, World!")

#Python User Input
print("Hello, World!")
exit() #To quit python

#Python Syntax
"""
DO NOT
if 5>2:
print("Five is greater than two")
"""
#DO
if 5>2:
    print("Five is greater than two")
#Python Comments
"""That is comment"""
#That is comment too

#Python Variables
x = 5
y = "Aidos"
print(x)
print(y)

#1
carname = "Volvo"

#2
x = 50

#3
x = 5
y = 10
print(x+y)

#4
x = 5
y = 10
z = x+y
print(z)

#5 (Remove the illegal characters in the variable name: 2my-first_name = "John")
myfirst_name = "John"

#6
x = y = z = "Orange"

#7
def myfunc():
    global x
    x = "fantastic"

#Python Data Types

#int
x = 5

#string
x = "Hello World"

#float
x = 20.5

#list
x = ["apple", "banana", "cherry"]

#tuple
x = ("apple", "banana", "cherry")

#dictionary
x = {"name" : "John", "age" : 36}

#bool
x = True

#Python Numbers

#1
x = 5
x = float(x)

#2
x = 5.5
x = int(x)

#3
x = 5
x = complex(x)

#Python Casting

#Integers
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

#Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Python Strings

#1
x = "Hello World"
print(len(x))

#2
txt = "Hello World"
x = txt[0]

#3
txt = "Hello World"
x = txt[2:5]

#4
txt = " Hello World "
x = txt.strip()

#5
txt = " Hello World
txt = txt.upper()

#6
txt = " Hello World
txt = txt.lower()

#7
txt = " Hello World
txt = txt.replace("H", "J")

#8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Python String Formatting
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#Python Booleans

#1
print(10 > 9) #Answer is true

#2
print(10 == 9) #Answer is false

#3
print(10 < 9) #Answer is false

#4
print(bool("abc")) #Answer is true

#5
print(bool(0)) #Answer if false

#Python Operators

#Multiply
print(10 * 5)

#Divide
print(10 / 5)

#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits: #Answer is in
  print("Yes, apple is a fruit!")

#Is not equal
if 5 != 10:
  print("5 and 10 is not equal")

#Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#Python If...Else

#Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
    print("Hello World")

#Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
    print("Hello World")

#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("No")

#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

#Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
  print("Hello")

#Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
  print("Hello")














