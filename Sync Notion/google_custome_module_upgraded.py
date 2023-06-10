from __future__ import print_function
import gspread
import requests
import urllib.parse
from oauth2client.service_account import ServiceAccountCredentials

import io
import json

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

# create a google client
class GoogleClient:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)


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

# find a cell in a Google Sheet with a given primary key of a row and column name
def find_cell(file_name, sheet_name, primary_key, primary_key_value, column_name):
    # Set up Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet 
    sheet = client.open(file_name).worksheet(sheet_name)

    # Get all values from the Google Sheet
    values = sheet.get_all_values()

    # Get the index of the column with the given column name
    column_index = values[0].index(column_name)

    # Find the row with the given primary key value
    for row in values:
        if row[values[0].index(primary_key)] == primary_key_value:
            return row[column_index]

    return None

# write a function to update a cell in a Google Sheet
def update_cell(file_name, sheet_name, cell, value):
    # Set up Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet 
    sheet = client.open(file_name).worksheet(sheet_name)

    # Update the cell
    sheet.update(cell, value)

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