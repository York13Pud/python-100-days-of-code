def filereader(file):
  """Read file and remove newline tag"""
  with open(file) as file:
    read_file = file.readlines()
    f = [int(item.strip("\n")) for item in read_file]
    return f

file_one = filereader("file1.txt")
file_two = filereader("file2.txt")

result = [number for number in file_one if number in file_two]

# Write your code above 👆

print(result)


