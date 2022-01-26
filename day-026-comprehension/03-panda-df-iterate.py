import pandas

# Define a dictionary that has the student names and their scores, both in separate lists:
student_dict = {
    "student": ["Bob", "Sam", "Alexis"],
    "score": [56, 76, 98]
}

# Create a data frame from the student dict:
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# Loop through each of the rows using the iterrows method that is part of pandas:
for (index, row) in student_data_frame.iterrows():
    if row.student == "Alexis":
        print(f"{row.student}'s Score is: {row.score}")
    else:
        print(f"{row.student} : {row.score}")