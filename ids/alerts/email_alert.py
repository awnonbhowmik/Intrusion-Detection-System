import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    from_email = "your_email@example.com"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(from_email, "your_password")
            server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email} with subject: {subject}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
