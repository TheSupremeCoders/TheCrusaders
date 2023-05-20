import os
import base64
import json
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Set up the Gmail API client
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    with open('token.json', 'r') as token:
        creds_data = json.load(token)
        creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Define the email message
to = 'princesharma2899@gmail.com'
subject = 'Python Script Running'
body = 'This is a test email sent using the Gmail API.'

message = f'To: {to}\nSubject: {subject}\n\n{body}'

# Encode the message as base64
encoded_message = base64.urlsafe_b64encode(message.encode('utf-8')).decode('utf-8')

# Create the message object
message_object = {'raw': encoded_message}

# Send the message
try:
    message = (service.users().messages().send(userId="me", body=message_object).execute())
    print(f'The message was sent successfully! Message ID: {message["id"]}')
except HttpError as error:
    print(f'An error occurred: {error}')
    message = None
