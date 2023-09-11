#TODO - see how to send via gmail api

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs import email, parola

print(email)
print(parola)

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = email
smtp_password = parola

# Set up the email message
sender = email
recipient = "constantin.copaceanu@gmail.com"
subject = "Test email"
body = "This is a test email sent from Python SDA52"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, msg.as_string())