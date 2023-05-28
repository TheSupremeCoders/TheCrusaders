import gspread
import re
import codechef
import codeforces
import leetcode
from problem import problem
from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm
from datetime import date

# ----- Gmail ---------
import os
import base64
import json
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#---------selenium and chrome driver ---------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re
import logging

def driversetup():
    # Set up logging to capture error messages
    logging.basicConfig(level=logging.ERROR)
    options = webdriver.ChromeOptions()
    #run Selenium in headless mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    #overcome limited resource problems
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("lang=en")
    #open Browser in maximized mode
    options.add_argument("start-maximized")
    #disable infobars
    options.add_argument("disable-infobars")
    #disable extension
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    return driver

# Set up the Chrome webdriver with headless mode turned on
driver = driversetup()
# Set the timezone on the webdriver
driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId': 'Asia/Kolkata'})

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gsheet.json', scope)
client = gspread.authorize(creds)

# Open the spreadsheet and select the "Form Responses 1" sheet
sheet = client.open('[DSA Group] Inviting More Members - Supreme Coders\' (Responses)').worksheet("Form Responses 1")

# get the column named as "Email Address" into a list
# email_list = sheet.col_values(2)[1:]

def unique_problems_set(problems): 
    return set([problem.name for problem in problems])

def print_problem(platform, problems, f):
    # extract only the problem name from the problem object
    problems = unique_problems_set(problems)
    if len(problems) != 0:
        f.write(f'{platform} - {len(problems)}\n')
        for problem in problems:
            f.write(f' ~ {problem}\n')


class Coder:
    leetcode_id = ""
    def __init__(self, timestamp, email, name, scholar_no, leetcode_id, gfg_id, codechef_id, codeforces_id):
        self.timestamp = timestamp.strip()
        self.email = email.strip()
        self.name = name.strip().title()
        self.scholar_no = scholar_no.strip()
        self.leetcode_id = leetcode_id.strip()
        self.gfg_id = gfg_id.strip()
        self.codechef_id = codechef_id.strip()
        self.codeforces_id = codeforces_id.strip()

        self.problems_leetcode = set()
        self.problems_gfg = set()
        self.problems_codeforces = set()
        self.problems_codechef = set()

        self.total_problems = 0

    def update_all(self):
        if self.leetcode_id != "" and re.match(r"https:\/\/leetcode\.com\/[a-zA-Z0-9_]+\/?", self.leetcode_id):
            print(f'Fetching Leetcode problems for {self.name}...')
            self.problems_leetcode = leetcode.get_problems_solved(driver, self.leetcode_id)
            self.total_problems += len(unique_problems_set( self.problems_leetcode ))

        if self.gfg_id != "" and re.match(r"https:\/\/auth\.geeksforgeeks\.org\/user\/[a-zA-Z0-9_]+\/practice\/?", self.gfg_id):
            print(f'Fetching gfg problems for {self.name}...')
            pass

        if self.codechef_id != "" and re.match(r"https:\/\/www\.codechef\.com\/users\/[a-zA-Z0-9_]+\/?", self.codechef_id):
            print(f'Fetching codechef problems for {self.name}...')
            self.problems_codechef = codechef.get_problems_solved(driver, self.codechef_id)
            self.total_problems += len(unique_problems_set( self.problems_codechef ))

        if self.codeforces_id != "" and re.match(r"https:\/\/codeforces\.com\/profile\/[a-zA-Z0-9_]+\/?", self.codeforces_id):
            print(f'Fetching codeforces problems for {self.name}...')
            self.problems_codeforces = codeforces.get_problems_solved(driver, self.codeforces_id)
            self.total_problems += len(unique_problems_set( self.problems_codeforces ))


# Get all the tuples and create Coder objects
coders = []
coders.clear()
tuples = sheet.get_all_values()[1:]  # exclude header row
ct = 1
for row in tuples:
    print(f'Processing row {ct}/{len(tuples)}...')
    ct += 1
    # Clean up the data
    row = [val.strip() for val in row]
    coder = Coder(*row)
    coder.update_all()
    coders.append(coder)

# close the driver
driver.quit()
# sort by number of problems solved
coders.sort(key=lambda x: x.total_problems, reverse=True)

from datetime import date

ref = date(2023, 4, 2)
tdy = date.today()
print()

cross = b'\xE2\x9D\x8C'
check = b'\xE2\x9C\x85'

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f'*DATE - {tdy.strftime("%d/%m/%Y")}*\n\n')
    for coder in coders:
        if coder.total_problems == 0:
            f.write(f'*{coder.name} - {cross.decode("utf-8")}*\n')
        else:
            f.write(f'*{coder.name} - {coder.total_problems} problems solved - {check.decode("utf-8")}*\n')
        print_problem('   _Leetcode_', coder.problems_leetcode, f)
        print_problem('   _Codeforces_', coder.problems_codeforces, f)
        print_problem('   _Codechef_', coder.problems_codechef, f)
        f.write('-------------------------------\n')

# Create the HTML content with inline styles
# Create the HTML content
html_content = f'''
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        table {{
            border-collapse: collapse;
            border-spacing: 0;
            width: 100%;
            border: 1px solid #ddd;
        }}

        th, td {{
            text-align: left;
            padding: 8px;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <table>
        <caption><h3>DATE - {tdy.strftime("%d/%m/%Y")}</h3></caption>
        <tr>
            <th>Name</th>
            <th>Leetcode Problems</th>
            <th>Codechef Problems</th>
            <th>Codeforces Problems</th>
        </tr>
'''

# Generate the table rows
for coder in coders:
    html_content += '<tr>\n'
    html_content += f'<td>{coder.name}</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_leetcode:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_codechef:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '<td>\n'
    for problem in coder.problems_codeforces:
        html_content += f'<span>{problem.html_str()}</span><br>\n'
    html_content += '</td>\n'
    html_content += '</tr>\n'

html_content += '''
    </table>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)


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

'''
# Define the email message
to = 'princesharma2899@gmail.com'
bcc = []
subject = 'DATE: ' + tdy.strftime("%d/%m/%Y") + ' - TheSupremeCoders'
html_body = open('output.html', 'r', encoding='utf-8').read()

message = f"""From: Your Email <your_email@example.com>
To: {to}
Bcc: {", ".join(bcc)}
Subject: {subject}
Content-Type: text/html; charset=utf-8

{html_body}"""


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
'''
# Define the email message
to = ['guptajirock176@gmail.com', 'princesharma2899@gmail.com',  'priyankasahu9350@gmail.com', 'aar9av@gmail.com']
bcc = []
subject = 'DATE: ' + tdy.strftime("%d/%m/%Y") + ' - TheSupremeCoders'
body = open('output.txt', 'r', encoding='utf-8').read()
message = f'To: {", ".join(to)}\nBcc: {", ".join(bcc)}\nSubject: {subject}\n\n{body}'

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