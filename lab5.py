#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

string = input("Enter a string: ")
pattern = r'a[b]*'

if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")

#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

string = input("Enter a string: ")
pattern = r'a[b]{2,3}'

if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

string = input("Enter a string: ")
pattern = r'[a-z]+(_[a-z]+)*'

matches = re.findall(pattern, string)

for match in matches:
    print(match)

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

string = input("Enter a string: ")
pattern = r'[A-Z][a-z]*'

matches = re.findall(pattern, string)

for match in matches:
    print(match)

#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

string = input("Enter a string: ")
pattern = r'a.*b$'

if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")

#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

string = input("Enter a string: ")
pattern = r'[ ,.]'

new_string = re.sub(pattern, ':', string)

print(new_string)

#7. Write a python program to convert snake case string to camel case string.
import re

string = input("Enter a string in snake case: ")
pattern = r'_([a-z])'

new_string = re.sub(pattern, lambda match: match.group(1).upper(), string)

print(new_string)

#8. Write a Python program to split a string at uppercase letters.
import re

string = input("Enter a string: ")
pattern = r'[A-Z][a-z]*'

matches = re.findall(pattern, string)

for match in matches:
    print(match)

#9. Write a Python program to insert spaces between words starting with capital letters.
import re

string = input("Enter a string: ")
pattern = r'[A-Z][a-z]*'

new_string = re.sub(pattern, lambda match: ' ' + match.group(0), string)

print(new_string)

#10. Write a Python program to convert a given camel case string to snake case.
import re

string = input("Enter a string in camel case: ")
pattern = r'(?<!^)(?=[A-Z])'

new_string = re.sub(pattern, '_', string).lower()

print(new_string)
