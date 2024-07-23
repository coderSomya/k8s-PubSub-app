import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(order):
    sender = os.getenv('SENDER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    recipient = order['email']
    subject = 'order confirmation'
    body = 'order is placed bro'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
      with smtplib.SMTP('smtp@gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    except Exception as e:
      print(f"Failed to send email: {e}")

