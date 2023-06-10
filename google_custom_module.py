from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import io
import json

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import os
import base64
import json
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def send_dict(file_name, sheet_name):
    # Set up Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet 
    sheet = client.open(file_name).sheet1

    # Get all values from the Google Sheet
    values = sheet.get_all_values()

    to_return = []

    #return all values as a list of dictionaries
    for row in values:
        to_return.append(dict(zip(values[0], row)))
    
    return to_return

# write a function to update a cell in a Google Sheet
def update_cell(file_name, sheet_name, cell, value):
    # Set up Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('gsheet.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet 
    sheet = client.open(file_name).worksheet(sheet_name)

    # Update the cell
    sheet.update(cell, value)

def load_credentials():
    """Load credentials from a JSON file.
    Returns:
        Credentials object.
    """
    credentials = None
    credentials_file = 'google_credentials.json'  # Replace with your credentials file path

    try:
        with open(credentials_file, 'r') as f:
            credentials_info = json.load(f)
            credentials = service_account.Credentials.from_service_account_info(credentials_info)
    except FileNotFoundError:
        print('Credentials file not found.')
    except json.JSONDecodeError:
        print('Invalid credentials file format.')
    
    return credentials


def download_file(download_url, file_name):
    """Downloads a file.
    Args:
        real_file_id: ID of the file to download.
    Returns:
        File content as bytes.
    """
    creds = load_credentials()

    if creds is None:
        return None

    try:
        service = build('drive', 'v3', credentials=creds)

        file_id = download_url.split('=')[1]

        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download {:.0%}.'.format(status.progress()))
        # get the file name from the metadata
        file_name_org = service.files().get(fileId=file_id).execute()['name']
        ext = file_name_org.split('.')[-1]
        file_name = file_name + '.' + ext


        print('Downloaded file "{}".'.format(file_name))

        # save the file in the images folder
        with open('images/' + file_name, 'wb') as f:
            f.write(file.getvalue())

    except HttpError as error:
        print('An error occurred:', error)
        file = None

def get_sheet(file_name, sheet_name):
    # Set up Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet 
    sheet = client.open(file_name).worksheet(sheet_name)

    return sheet

def send_email(to, bcc, subject, body):
    message = f'To: {", ".join(to)}\nBcc: {", ".join(bcc)}\nSubject: {subject}\n\n{body}'
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