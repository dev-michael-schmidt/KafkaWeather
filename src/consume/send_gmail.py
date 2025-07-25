import os
import ssl
import smtplib
from email.message import EmailMessage

def send_gmail(subject: str, body: str, to_addr: str, from_addr: str, app_password: str):
    host = os.environ['SMTP_HOST']
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=465, context=context) as smtp:
        smtp.login(from_addr, app_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_gmail(
        subject="Foo",
        body="Bar",
        to_addr=""
    )