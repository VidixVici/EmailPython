from email.message import EmailMessage
import ssl
import smtplib

# Email from which the message will be sent
email_sender = 'Email@gmail.com'
# Email App Password obtained from: http://myaccount.google.com/u/4/apppasswords
email_password = 'Placeholder Pass'
# Emails to which the Message will be sent
email_receiver = ['Email@gmail.com', 'Email2@gmail.com']

# Subject of the Email
subject =  'Placeholder Subject'

#Body of the Email
body = """
I am using this as a test
for the body of an email
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
