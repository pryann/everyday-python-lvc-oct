import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def connect_to_smtp(
    smtp_server: str, smtp_port: int, sender_email: str, sender_password: str
) -> smtplib.SMTP | None:
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        return server
    except Exception as error:
        print("Failed to connect to SMTP server.", error)
        return None


def add_recipients(
    msg: MIMEMultipart,
    all_recipients: list[str],
    cc_emails: list[str] | None = None,
    bcc_emails: list[str] | None = None,
) -> list[str]:
    if cc_emails:
        msg["Cc"] = ", ".join(cc_emails)
        all_recipients.extend(cc_emails)
    if bcc_emails:
        all_recipients.extend(bcc_emails)
    return all_recipients


def add_attachment(msg: MIMEMultipart, attachments: list[str] | None):
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    part = MIMEApplication(file.read())
                    part.add_header(
                        "Content-Disposition",
                        "attachment",
                        filename=os.path.basename(file_path),
                    )
                    msg.attach(part)


def send_mail(
    server: smtplib.SMTP,
    from_addr: str,
    subject: str,
    messsage: str,
    to_emails: list[str],
    cc_emails: list[str] | None = None,
    bcc_emails: list[str] | None = None,
    attachments: list[str] | None = None,
    message_mime_type: str = "plain",
) -> bool:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = ", ".join(to_emails)

    all_recipients = to_emails.copy()
    all_recipients = add_recipients(msg, all_recipients, cc_emails, bcc_emails)

    msg.attach(MIMEText(messsage, message_mime_type))
    add_attachment(msg, attachments)

    try:
        server.sendmail(from_addr, all_recipients, msg.as_string())
        print("Email sent successfully.")
        return True
    except Exception as error:
        print("Failed to send email.", error)
        return False


if __name__ == "__main__":
    # real life user a config file or environment variables
    smtp_server = ""
    smtp_port = 587
    smtp_email = ""
    smtp_password = ""

    server = connect_to_smtp(smtp_server, smtp_port, smtp_email, smtp_password)

    send_mail(
        server=server,
        from_addr=smtp_email,
        to_emails=["recipient@example.com"],
        subject="Test email",
        message="This is a test email sent from Python.",
        cc_emails=["cc@example.com"],
        bcc_emails=["bcc@example.com"],
        attachments=["./files/sample-attachment.txt"],
        message_mime_type="plain",
    )

    server.quit()
