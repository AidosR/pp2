# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class string():
    def __init__(self):
        self.strs = ""

    def get_String(self):
        self.strs = input()

    def print_String(self):
        print(self.strs.upper())


strs = string()
strs.get_String()
strs.print_String()
print()


# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


squared = Square(5)
print(squared.area())  # prints 25 as given argument
print(Square().area())  # prints zero as default area
print()


# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rect = Rectangle(3, 6)
print(rect.area())
print()

# 4. Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


p1 = Point(2, 3)
p2 = Point(3, 3)
p1.show()
p2.show()
p1.move(5, -4)
p1.show()
p1.dist(p2)


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# class Account:
# pass
class Account:
    owner = " "
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return "Deposit Accepted"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return "Withdrawl Accepted:"
        return "Funds Unavailable!"


