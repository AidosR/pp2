#1. Write a Python program to list only directories, files and all directories, files in a specified path
import os

path = "/Users/mrbra/OneDrive/Рабочий стол"

dirs = []
files = []

# Перебираем элементы в пути
for item in os.listdir(path):
    item_path = os.path.join(path, item)
    # проверяем дерриктория ли это, если да то закинем в деррикторию
    if os.path.isdir(item_path):
        dirs.append(item)
    # а может быть это файл и это проверим, если да то закинем в фалы
    elif os.path.isfile(item_path):
        files.append(item)

print("Directories:", dirs)
print("Files:", files)

#2. Write a Python program to check for access to a specified path
import os

path = "/Users/mrbra/OneDrive/Рабочий стол"

# Проверим существование, читаемость, возможность записи и исполняемость пути
if os.access(path, os.F_OK):
    print("Path exists")
else:
    print("Path does not exist")

if os.access(path, os.R_OK):
    print("Path is readable")
else:
    print("Path is not readable")

if os.access(path, os.W_OK):
    print("Path is writable")
else:
    print("Path is not writable")

if os.access(path, os.X_OK):
    print("Path is executable")
else:
    print("Path is not executable")


#3. Test the existence, readability, writability and executability of the specified path
import os

path = "/Users/mrbra/OneDrive/Рабочий стол"

if os.path.exists(path):
    print("Path exists")
    filename = os.path.basename(path)
    print("Filename:", filename)
    directory = os.path.dirname(path)
    print("Directory:", directory)
else:
    print("Path does not exist")

#4. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
with open("/Users/mrbra/OneDrive/Рабочий стол/sda.txt") as file:
    line_count = sum(1 for line in file)
    print("Number of lines in file:", line_count)

#5. Write a Python program to count the number of lines in a text file
my_list = ["apple", "banana", "cherry"]

with open("/Users/mrbra/OneDrive/Рабочий стол/sda.txt", "w") as file:
    for item in my_list:
        file.write("%s\n" % item)

#6. Write a Python program to write a list to a file
import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write("This is file %s" % letter)

#7. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
with open("/Users/mrbra/OneDrive/Рабочий стол/sda.txt", "r") as source:
    with open("/Users/mrbra/OneDrive/Рабочий стол/sda2.txt", "w") as destination:
        destination.write(source.read())

#8. Write a Python program to copy the contents of a file to another file Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not
import os

path = "/Users/mrbra/OneDrive/Рабочий стол/sda2.txt"

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File not writable, cannot delete")
else:
    print("File does not exist, cannot delete")
