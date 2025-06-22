import os
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Manoj's Python SMS Notifier!",
    from_=os.getenv('TWILIO_PHONE_NUMBER'),
    to='+919965802143'
)

print(f"✅ Message sent! SID: {message.sid}")
