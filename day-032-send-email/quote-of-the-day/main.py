from calendar import day_name
import datetime as dt
import random
import smtplib

# --- Setup required email settings:

my_email = ""
to_email = ""
smtp_server = ""
sender_username = ""
sender_password = ""

# --- Get current day:

day_to_send_email = "Thursday"
current_time = dt.datetime.now()
current_day = current_time.today().strftime("%A")

# --- Import list of quotes to a list:
#list_of_quotes = []

with open("./quotes.txt") as quotes_file:
   list_of_quotes = quotes_file.readlines()

# --- Get a random quote:
quote_of_the_day = random.choice(list_of_quotes)

# --- Check to see if the day is equal to a particular day and if so, send an email with a random quote:
if day_to_send_email == current_day:
    # Create an SMTP connection object to a mail provider:
    with smtplib.SMTP(smtp_server, port=25) as connection:
        # Make the connection secure:
        connection.starttls()
        # Login to the SMTP Server:
        connection.login(user=sender_username,password=sender_password)
        # Send a message.
        # Note: \n\n after the subject is required to separate the subject and message body.
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Quote of the Day \n\n{quote_of_the_day}")