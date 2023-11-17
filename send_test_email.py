import os
from dotenv import load_dotenv
load_dotenv()
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content,From

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email('rpsureka2003@gmail.com') # Change to your verified sender
to_email = To('varunapriya333@gmail.com')  # Change to your recipient
subject = "You have a visitor"
content = Content("text/plain", "Your webcam recognizes someone.")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)