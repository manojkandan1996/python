import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'manojkandan1996@gmail.com'
SENDER_PASSWORD = 'ltzy xytc jowi owzq'  # Use App Password if 2FA is enabled

# Load contacts
contacts = pd.read_csv('contacts.csv')

# Email content
subject = "Welcome to Our Newsletter"
body_template = "Hi {name},\n\nThank you for subscribing!\n\nBest,\nRamya"

# Set up SMTP connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# Send emails
for index, row in contacts.iterrows():
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = row['Email']
    msg['Subject'] = subject

    body = body_template.format(name=row['Name'])
    msg.attach(MIMEText(body, 'plain'))

    try:
        server.sendmail(SENDER_EMAIL, row['Email'], msg.as_string())
        print(f"✅ Sent to {row['Email']}")
    except Exception as e:
        print(f"❌ Failed to send to {row['Email']}: {e}")

server.quit()