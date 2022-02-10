# Request the persons height and weight:

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Perform the BMI calculation and store the result as an integer:
bmi_result = int(float(weight) / float(height)**2)

# Display the BMI result:
print(bmi_result)
# or
print("Your BMI is: " + str(bmi_result))
