def is_leap(year):
  """This will take the argument of year and check if the year is a leap year and return True or False."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # Is a leap year.
        return True
      else:
        # Is not a leap year.
        return False
    else:
      # Is a leap year.
      return True
  else:
    # Is not a leap year.
    return False



def days_in_month(year,month):
    """Check if the month is a leap year or not and output the correct number of days for the given month:
    Calls the is_leap function to check if it is a leap year and then if the month is 2,
    take 28 from the month_days list and add 1 (29)"""
    
    # Check if the month number entered is valid:
    if month > 12 or month < 1:
        return "You entered an invalid month"
    # Create a list with the days of each month:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    # Take the month entered and deduct on to match the month in the month_days list:
    month_pointer = month - 1
    
    # Perform the month check:
    if is_leap(year) == True and month_pointer == 1:
        total_month_days = month_days[month_pointer] + 1
        return total_month_days
    else:
        # For any other month than February (2), find the month in the month_days list and return it.
        return month_days[month_pointer]
  
# Ask the user for a year and a month:
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Called the days_in_month function:
days = days_in_month(year, month)

# Print the total days for the month:
print(days)
