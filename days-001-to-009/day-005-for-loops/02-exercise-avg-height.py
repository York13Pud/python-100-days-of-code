# Request the user input some heights:
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Determine the number of items in the list:
number_of_students = 0
for student in student_heights:
    number_of_students += 1

# Perform the addition of all the items in the list:
total = 0
for student_height in student_heights:
    total += student_height

# Display the average height:
print(round(total / number_of_students))
