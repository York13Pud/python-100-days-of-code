# Request the users age:
age = input("What is your current age?")

# Setup variables that we can use:
age_up_to = 90
weeks_per_year = 52
months_per_year = 12
days_per_year = 365.25

# Perform the maths needed to work out the remaining time:
remaining_years = (age_up_to - int(age))
remaining_weeks = (remaining_years * weeks_per_year)
remaining_months = (remaining_years * months_per_year)
remaining_days = (remaining_years * days_per_year)

# Display the remaining time in the various forms:
message = f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left."
print(message)
