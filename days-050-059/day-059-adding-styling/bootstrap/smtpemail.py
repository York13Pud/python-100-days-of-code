import smtplib

# --- Define variables for the required setting for the mail server.
# --- Change the settings to meet your server and mail user details:

def send_email(to_email, email_subject, email_message):
    smtp_server = ""
    smtp_port = "25"
    sender_username = ""
    sender_password = ""
    sender_email = ""
    # --- Create an SMTP connection object to a mail provider:
    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        # --- Make the connection secure:
        connection.starttls()
        # --- Login to the SMTP Server:
        connection.login(user=sender_username, password=sender_password)
        # --- Send a message.
        # --- Note: \n\n after the subject is required to separate the subject and message body.
        connection.sendmail(from_addr=sender_email,
                            to_addrs=to_email,
                            msg=f"Subject:{email_subject} \n\n{email_message}")