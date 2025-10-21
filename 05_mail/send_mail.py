import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def connect_to_smtp():
    pass


def add_recipients(
    msg: MIMEMultipart,
    all_recipients: list[str],
    cc_emails: list[str] | None = None,
    bcc_emails: list[str] | None = None,
):
    if cc_emails:
        msg["Cc"] = ", ".join(cc_emails)
        all_recipients.extend(cc_emails)
    if bcc_emails:
        all_recipients.extend(bcc_emails)
    return all_recipients


def add_attachment():
    pass


def send_mail(
    server: str,
    sender_email: str,
    subject: str,
    messsage: str,
    to_emails: list[str],
    cc_emails: list[str] | None = None,
    bcc_emails: list[str] | None = None,
    attachments: list[str] | None = None,
    message_mime_type: str = "plain",
):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(to_emails)

    all_recipients = to_emails.copy()
    all_recipients = add_recipients(msg, all_recipients, cc_emails, bcc_emails)

    msg.attach(MIMEText(messsage, message_mime_type))
