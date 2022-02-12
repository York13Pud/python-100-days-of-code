import smtplib

# Define variables for the required setting for the mail server:
my_email = ""
to_email = ""
smtp_server = ""
sender_username = ""
sender_password = ""


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
                        msg="Subject:Hello \n\nHello again 6")