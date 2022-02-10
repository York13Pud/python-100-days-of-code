# Request the persons height and weight:

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Perform the BMI calculation and store the result as an integer:
bmi_result = int(float(weight) / float(height)**2)

# Display what the result means:
if bmi_result < 18.5:
    print(f"Your BMI is: {bmi_result} You are underweight.")
elif bmi_result < 25:
    print(f"Your BMI is: {bmi_result} Your weight is normal")
elif bmi_result < 30:
    print(f"Your BMI is: {bmi_result} You are overweight")
elif bmi_result < 35:
    print(f"Your BMI is: {bmi_result} You are obese")
else:
    print(f"Your BMI is: {bmi_result} You are clinically obese.")
