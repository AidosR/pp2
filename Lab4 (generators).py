# 1. Create a generator that generates the squares of numbers up to some number N.
def square_numbers(N):
    for i in range(1, N+1):
        yield i**2
for n in square_numbers(5):
            print(n)

# 2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

even_nums = even_numbers(n)
result = ",".join(str(i) for i in even_nums)

print("Even numbers between 0 and", n, ":", result)

# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
number = int(input("enter number: "))
for i in range(0, number):
    if i % 12 == 0:
        print(i, end=" ")

# 4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(min, max):
    n = min
    while n <= max:
        yield n ** 2
        n += 1
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)

# 5. Implement a generator that returns all numbers from (n) down to 0.
def generator(start):
    n = start
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for i in generator(n):
    print(i)