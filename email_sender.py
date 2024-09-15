import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'sender_email_name'
email['to'] = 'recipient_email_name'
email['subject'] = 'subject_of_email'
email.set_content('content_of_email')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender_email_id','app_password or regular pass')
    smtp.send_message(email)
    print('congrats all good!!')