# Create a dictionary with the students name and their score
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}

# Add the grades to student_grades with the appropriate grading from their score.
for student in student_scores:
    if student_scores[student] in range(91,100):
        student_grades[student] = "Outstanding"
    elif student_scores[student] in range(81,90):
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] in range(71,80):
        student_grades[student] = "Acceptable"
    elif student_scores[student] in range(0,70):
        student_grades[student] = "Fail"

# Print out the contents of the student_grades.
print(f"{student_grades}\n")

# Let's make that a little cleaner:
for student in student_grades:
    print(f"{student}: {student_grades[student]}")