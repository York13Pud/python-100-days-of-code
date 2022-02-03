# --- Import the required modules:
import datetime as dt
import pandas as pd
import random
import smtplib

# --- Define a variable to get the current date and time:
current_time = dt.datetime.now()

# --- Define two variables, one for the current month and the other for the current day:
current_month = current_time.month
current_day = current_time.day

# --- Create a dataframe from the birthdays.csv file:
birthdays = pd.read_csv("./birthdays.csv")

# --- Change the index to name. I had an issue that when I called name, it returned the index number.
# --- This resolved that issue:
birthdays = birthdays.set_index('name')


# --- Define a function that will take a name and an email address, process them with a letter template
# --- and then send an email to the person who's birthday it is:
def send_email(name, email):
    # --- Required variables for sending an email
    my_email = ""
    to_email = email
    smtp_server = ""
    sender_username = ""
    sender_password = ""
        
    # --- Read the contents of the letter template and assign the contents to the variable named letter_to_use:
    try:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_template_file:
            letter_to_use = letter_template_file.read()
    except FileNotFoundError:
        print(f"\033[1;31;40m**** WARNING **** Email template not found ****\033[0;37;40m ")
    else:
        pass
    
    # --- Define a variable that will take the contents of letter_to_use and replace [NAME] with the persons name:
    birthday_letter = letter_to_use.replace("[NAME]", name.capitalize())
    
    # --- Proceed to send the email:
    with smtplib.SMTP(smtp_server, port=25) as connection:
        # Make the connection secure:
        connection.starttls()
        # Login to the SMTP Server:
        connection.login(user=sender_username,password=sender_password)
        # Send a message.
        # Note: \n\n after the subject is required to separate the subject and message body.
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Happy Birthday \n\n{birthday_letter}")

# --- Go through each row in the dataframe and find out if any match todays date:
for (index, row) in birthdays.iterrows():
    # --- Check the row to see if the month is the same as todays date:
    if row.month == current_month:
        # --- If it matches, check the row to see if the day is the same as todays date:
        if row.day == current_day:
            # --- If it matches, call the send email function and pass in the persons name and email as arguments:
            send_email(name = row.name, email = row.email)        
    
    # --- if the month doesn't match todays date, display a message to indicate there are no birthdays:
    else:
        print("It is no-one's birthday today.")