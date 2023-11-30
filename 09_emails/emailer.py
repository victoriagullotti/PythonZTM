from smtplib import SMTP
import json
from email.mime.text import MIMEText

def send_email(to, subject, body):
    sender = 'myemail@gmail.com'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    # Gmail credentials
    username = "myemail@gmail.com"
    password = "!Q2w3e4r"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, to, msg.as_string())
    server.quit()


# Get email list from a JSON file
with open('email_list.json') as json_file:
    email_list = json.load(json_file)

for recipient in email_list:
    send_email(recipient, 'Subject', 'Email text')
