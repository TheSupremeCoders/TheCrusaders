import gspread
from oauth2client.service_account import ServiceAccountCredentials

import requests

# API token and database ID
integration_token = 'secret_yF378kdYlxCbn9pzTH70s7eXVQ3DqHy6Q8vchQLztv6'
database_id = '1a1f07a01c2443718ac283ddab53dec9'

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('New Onboarding - The Supreme Coders (Responses)').sheet1

# Get all values from the Google Sheet
values = sheet.get_all_values()

# header = ['Timestamp', 'Email Address', 'Name', 'Scholar Number', 'Gender', 'Profile Picture', 'Batch', 'Codeforces ID', 'Codechef ID', 'Leetcode ID', 'GFG ID', 'Notion Page ID', 'Codeforces URL', 'Codechef URL', 'Leetcode URL', 'GFG URL']

# API endpoint URL
url = f'https://api.notion.com/v1/databases/{database_id}'

# Request headers
headers = {
    'Authorization': f'Bearer {integration_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

def create_notion_page(database_id, properties):
    # API endpoint for creating a new page
    url = "https://api.notion.com/v1/pages"

    # Authorization token for Notion API
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    # Create a new page with the specified properties
    data = {
        "parent": {
            "database_id": database_id
        },
        "properties": properties
    }

    # Send POST request to create the page
    response = requests.post(url, headers=headers, json=data)
    if(response.status_code == 200):
        print("Page created successfully")
    else:
        print("Error creating page")
        print(response.json())
    
    # return the page ID of the newly created page
    return response.json()["id"]


create_page_url = "https://api.notion.com/v1/pages"
# Iterate over the rows in the Google Sheet
for row in values[1:]:
    email = row[1]
    name = row[2]
    scholar_number = int(row[3])
    gender = row[4]
    profile_picture = row[5]

    # download the profile picture and upload it to Notion

    batch = row[6]
    codeforces_id = row[7]
    codechef_id = row[8]
    leetcode_id = row[9]
    gfg_id = row[10]
    whatsapp_number = row[11]

    # Create a new page in Notion
    data = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Email": {
                "email": email
            },
            "Scholar Number": {
                "number": scholar_number
            },
        }
    }

    # Send POST request to create the page
    response = requests.post(create_page_url, headers=headers, json=data)
    if(response.status_code == 200):
        print("Page created successfully")
    else: 
        print("Error creating page")
        print(response.json())
