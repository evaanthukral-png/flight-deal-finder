from twilio.rest import Client
import os

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_SID"),os.environ.get("TWILIO_AUTH_TOKEN"))
    def send_sms(self, message):
        self.client.messages.create(
            body=message,
            from_=os.environ.get("TWILIO_VIRTUAL_NUMBER"),
            to=os.environ.get("TWILIO_VERIFIED_NUMBER")
)