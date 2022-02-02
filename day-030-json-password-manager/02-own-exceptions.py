# An example of raising your own exception is when something seems unrealistic. For example, a persons height:

height = float(input("Please enter your height (m): "))

# In this case, if the hight entered is over 3m's, it will provide an error. If it's below, print the value:
if height > 3:
    raise ValueError("Please check the height you entered.")
else:
    print(height)