from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Data to inject
data = {
    'subject': 'Welcome to Manoj’s Newsletter!',
    'name': 'KANDAN',
    'message': 'Thanks for signing up. Stay tuned for updates!',
    'sender': 'Mano'
}

# Render the email content
html_content = template.render(data)

# Email setup
msg = MIMEMultipart()
msg['From'] = 'manojkandan1996@gmail.com'
msg['To'] = 'manojmca643@gmail.com'
msg['Subject'] = data['subject']
msg.attach(MIMEText(html_content, 'html'))

# Send email (use app password if Gmail)
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('manojkandan1996@gmail.com', 'qowv qdky zovi hkfv')
    server.send_message(msg)

print("✅ Email sent successfully!")