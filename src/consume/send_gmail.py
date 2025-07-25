import os
import ssl
import smtplib
from email.message import EmailMessage

def send_gmail(subject: str,
               body: str,
               to_addr: str,
               from_addr: str | None = None,
               app_password: str | None = None):
    """Send a simple text email via Gmail SMTP."""
    from_addr = from_addr or os.environ["GMAIL_USER"]
    app_password = app_password or os.environ["GMAIL_APP_PASS"]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(from_addr, app_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_gmail(
        subject="Foo",
        body="Bar",
        to_addr=""
    )