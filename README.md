# Email_sender
## Purpose:
This Python script sends an email using Gmail's SMTP (Simple Mail Transfer Protocol) server.

Import statements:

~~~Python
import smtplib
from email.message import EmailMessage
~~~
smtplib: This module provides functions for interacting with SMTP servers.
EmailMessage: This class is used to create email messages with various headers and content.
Creating an email message:

~~~Python
email = EmailMessage()
email['from'] = 'Sender_user_name'
email['to'] = 'reciever_user_gmail_address'
email['subject'] = 'Email project'
email.set_content('I am doing a project to send email through this code without using the browser')
~~~
email = EmailMessage(): Creates a new email message object.
Setting headers:
email['from']: Sets the sender's email address.
email['to']: Sets the recipient's email address.
email['subject']: Sets the subject of the email.
Setting content:
email.set_content(): Sets the body of the email.
Connecting to Gmail's SMTP server and sending the email:

~~~Python
with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
    smtp.login('your_gmail_address', 'your_app_password')
    smtp.send_message(email)
    print('congrats all good!!!')
~~~
with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
Establishes a secure connection to Gmail's SMTP server using SSL (Secure Sockets Layer) on port 465.
Creates a context manager (smtp) to automatically handle connection closing.
smtp.login('your_gmail_address', 'your_app_password'):
Logs in to the SMTP server using your Gmail address and app password.
smtp.send_message(email):
Sends the created email message using the SMTP connection.
print('congrats all good!!!'):
Prints a message indicating that the email was sent successfully.
## Note:

Replace 'Sender_user_name', 'reciever_user_gmail_address', 'your_gmail_address', and 'your_app_password' with your actual values.
Ensure you have enabled 2-Step Verification for your Gmail account and generated an app password for use with scripts.
## How to use code

Create a new Python file: Save the provided code as a .py file (e.g., email_sender.py).
remember donot create a pyhton file with name of email.py as it my give error
Replace placeholders:
Sender's email address: Replace 'Sender_user_name' with your actual Gmail address.
Recipient's email address: Replace 'reciever_user_gmail_address' with the email address of the person you want to send the email to.
Gmail address and app password: Replace 'your_gmail_address' and 'your_app_password' with your Gmail address and the corresponding app password.
Run the script:
Open a terminal or command prompt and navigate to the directory where you saved the send_email.py file.
Run the script using the following command:
~~~Bash
py send_email.py
~~~





