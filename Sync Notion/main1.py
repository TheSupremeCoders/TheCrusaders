import os
import gspread
from notion.client import NotionClient

# Set up the Google Sheets API
google_creds_path = "google_credentials.json"

# Set up the Notion API
notion_token = ""
notion_database_id = ""

# Authenticate and authorize access to the Google Sheet
gc = gspread.service_account(filename=google_creds_path)

# Fetch data from the Google Sheet
data = sheet.get_all_records()
# Open the Google Sheet
sheet = client.open('New Onboarding - The Supreme Coders (Responses)').sheet1

# Connect to the Notion API
client = NotionClient(token_v2=notion_token)
database = client.get_collection_view(notion_database_id)

# Iterate over the fetched data and create pages in the Notion database
for row in data:
    new_page = database.collection.add_row()
    new_page.title = row["Name"]
    new_page.set_property("Email Address", row["Email Address"])
    new_page.set_property("Scholar Number", row["Scholar Number"])
    new_page.set_property("Gender", row["Gender"])
    new_page.set_property("Batch", row["Batch"])
    # Set other properties based on the column names and corresponding values

    # Get the created Notion page ID and update the 'Notion Page ID' column in the Google Sheet
    notion_page_id = new_page.id
    row_index = data.index(row) + 2  # Add 2 to account for the header row and 0-based indexing
    sheet.update(f"N{row_index}", notion_page_id)

print("Data has been populated to the Notion database and 'Notion Page ID' column in the Google Sheet has been updated.")
