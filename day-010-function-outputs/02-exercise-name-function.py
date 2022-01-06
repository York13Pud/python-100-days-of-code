# Define a function with two parameters for the first name and last name to be converted to title case:
def format_name(f_name,l_name):
    # You can use multiple returns in a function if they are inside of (for example) an if statement:
    if f_name == "" or l_name == "":
        return "You didn't enter your full name"
    else:
        # Convert the two names to title case:
        first_name_formatted = f_name.title()
        last_name_formatted = l_name.title()
        
        # Return the two formatted names as one string. It looks similar to a print function:
        return f"{first_name_formatted} {last_name_formatted}"

# Call the format_name function as a variable:
formatted_name = format_name(f_name=input("Please enter your first name: "),l_name=input("Please enter your last name: "))

# Print out the value of formatted_name:
print(formatted_name)

# Alternatively, you could just put the function call into the print function:
# print(format_name(f_name=input("Please enter your first name: "),l_name=input("Please enter your last name: ")))