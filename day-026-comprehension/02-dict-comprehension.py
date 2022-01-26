import random

# Define a list of names:
names = ["Bob", "Jason", "Sam", "Alexis"]

# Create a new dictionary using dictionary comprehension to loop through the names list
# using each name as a key and a random number as the value:
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# Create a new dictionary of students, with their scores that scored 60 or over:
passed_students_score = {student:"passed" for (student,score) in students_scores.items() if score >= 60}
print(passed_students_score)

# Instead of putting their score as the value, just put "passed":
passed_students = {student:"passed" for (student,score) in students_scores.items() if score >= 60}
print(passed_students)


#Exercise 1: Convert a sentence to a dictionary with the charecter count for each word as the value:
sentence = "What is the airspeed velocity of an unladen Swallow?"

# Create the dictionary with the charecter count for each word as the value (split creates a list of words):
result = {word:len(word) for (word) in sentence.split()}
print(result)

#Exercise 2: Convert temps in a dictionary from c to f:
#Define a dictionary with the temp in c for each day:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Convert the temp to f in a new dictionary:
weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
print(weather_f)