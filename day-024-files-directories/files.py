import os
from turtle import home
home_dir = os.path.expanduser("~")
print(home_dir)

# To read a file, you first need to open it in Python (this will not open it in an app):
file_to_use = open("my_file.txt")

# We then read the contents of the file as a variable:
contents = file_to_use.read()

# Then, you can display the contents of the file by calling the variable that read it:
print(contents)

# Once you are done with the file, close it to free up resources:
file_to_use.close()

# ----------------------------------------------------------------------------------------

# Another method to read a file is to use with. The benefir of doing this is that it will
# close the file automatically:

with open(f"{home_dir}/Desktop/my_file.txt") as file_to_use:
    contents = file_to_use.read()
    print(contents)

# Read a file that is one level up:
with open("../README.md") as file_to_use:
    contents = file_to_use.read()
    print(contents)
    
# Read a file that is stored on the desktop but usable for any user:
with open(f"{home_dir}/Desktop/my_file.txt") as file_to_use:
    contents = file_to_use.read()
    print(contents)

# ----------------------------------------------------------------------------------------
# To write to a file:

# mode = "w" will open the file up as writable as read-only is the default.
# Note: If the file does not exist, it will create it for both w and a.
with open("my_file1.txt", mode="w") as file_to_use:
    file_to_use.write("Hello")

# To append to a file, use mode = "a":
with open("my_file1.txt", mode="a") as file_to_use:
    file_to_use.write("\nWorld")

    
with open("my_file1.txt") as file_to_use:
    contents = file_to_use.read()
    print(contents)
