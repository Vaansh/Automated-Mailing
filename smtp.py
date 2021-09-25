import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(user: str, password: str, headers: dict, subject: str, signature: str) -> None:
    message = MIMEMultipart("mixed")
    message["Subject"] = subject
    message["From"] = user
    message["To"] = headers["email"]

    body = "Hi " + headers["recipient name"] + ",\n" + "body\n" + "Best,\n" + headers["contact name"]
    body_of_message = MIMEText(body, "plain")
    signature_of_message = MIMEText(signature, "html")

    # attach body and signature
    message.attach(body_of_message)
    message.attach(signature_of_message)

    # attach pdf sponsorship package
    with open(headers["package path"], "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(str(headers["package path"])))
    message.attach(attach)

    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.ehlo()
    mail.starttls()

    mail.login(user, password)
    mail.sendmail(user, headers["email"], message.as_string())
    mail.quit()
