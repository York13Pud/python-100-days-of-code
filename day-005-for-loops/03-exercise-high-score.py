# Ask the user for the scores:
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Create a variable to hold the highest score:
max_score = 0

# Cycle through the student_scores list and find the highest value.
# Replace max_score's value when a value that is higher than it is found.
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score

print(f"The highest score in the class is: {max_score}")

# Create a variable to hold the lowest score:
low_score = 1000

# Cycle through the student_scores list and find the lowest value.
# Replace max_score's value when a value that is higher than it is found.
for student_score in student_scores:
    if student_score < max_score:
        low_score = student_score

print(f"The lowest score in the class is: {low_score}")
