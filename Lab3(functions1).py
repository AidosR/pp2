#1.A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def Ounces(x):
    return x * 28.3495231
grams = float(input())
ounces = Ounces(grams)
print(ounces)



#2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def Convert_to_C(x):
    return (5 / 9) * (x - 32)
F = float(input())
C = Convert_to_C(F)
print(C)

#3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if (2 * j + 4 * i) == numlegs:
            return i, j
    return None

heads = 35
legs = 94
result = solve(heads, legs)
if result is not None:
    rabbits, chickens = result
    print("Number of rabbits:", rabbits)
    print("Number of chickens:", chickens)
else:
    print("No solution found.")

# 4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
from math import sqrt
def filter_prime(nums):
    primes = []
    isPrime = True
    for num in nums:
        for div in range(2, int(sqrt(num))):
            if num % div == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
        isPrime = True
    return primes
nums = list(map(int, input().split()))
print(filter_prime(nums))
print()

# 5. Write a function that accepts string from user and print all permutations of that string.
import itertools
def f(s):
    s1=itertools.permutations(s)
    for i in s1:
     i = "".join(i)
     print(i)
s = input()
f(s)
print()

# 6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def f(a):
    b = a[::-1]
    c = " ".join(b)
    print(c)

a = input().split()
f(a)
print()

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False 
'''
def has_33():
    a=input().split()
    cnt=0
    for i in range(len(a)-1):
        if(a[i]=="3" and a[i+1]=="3"):
            cnt+=1
    if (cnt=="0"):
        print("False")
    else:
         print("True")
has_33()
print()

# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
'''
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''
def f(a):
    b=[]
    for i in a:
        if(i == "0"):
            b.append(i)
        elif (i == "7"):
            b.append(i)
    if(len(b)>=3):
        if(b[0]=="0" and b[1]=="0" and b[2]=="7"):
            print("True")
    else:
        print("False")
a = input().split()
f(a)

# 9. Write a function that computes the volume of a sphere given its radius.
pi = 3.142
radius = 6
r = radius ** 3
v = (4 / 3) * pi * r
print(v)

# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique(a):
    numbers = []
    for b in a:
        if b not in numbers:
            numbers.append(b)
    return numbers
print(unique([2, 3, 5, 5, 8, 11, 11, 11, 11, 45, 32, 2]))

# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
string = input()
reverse = ""
for i in string:
    reverse = i + reverse
if(string == reverse):
    print("palindrome")
else:
    print("not palindrome")

# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# ******
def histogram(a):
    for n in a:
        out = ""
        times = n
        while(times > 0):
            out += '*'
            times = times - 1
        print(out)
histogram([4, 9, 7])

# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
'''
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''

import random
name = input("Hello! What is your name?")
print("Well, KBTU, I am thinking of a number between 1 and 20.")
guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break

