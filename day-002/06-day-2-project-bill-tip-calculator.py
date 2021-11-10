# Tip calculator.

print('''
###################################
#                                 #
#  Welcome to the tip calculator  #
#                                 #
###################################''')

# Request the details of the bill, tip percentage and the number of people to split the bill between:
bill_amount = float(input("What was the total bill? "))
tip_amount = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Work out the maths required to the required variables:
tip_percentage = (bill_amount * (tip_amount / 100))
total_bill = (tip_percentage + bill_amount)
bill_per_person = round(total_bill / number_of_people, 2)

# This will format the bill to enforce showing two decimal places as python will not show a zero if it is the second decimal place.
bill_per_person_formatted = "{:.2f}".format(bill_per_person)

# Display the results:
print(f"Each person should pay: ${bill_per_person_formatted}")
