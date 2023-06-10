import json
from google_custom_module import *
from notionClient import NotionAPI


# API token and database ID
secret = json.load(open("secret.json"))
integration_token = secret["notion_token"]
database_id = secret['databases']['members']

# sync the database with the data from the Google Sheet
def sync_database():
    # get the data from the Google Sheet
    data = send_dict('New Onboarding - The Supreme Coders (Responses)', 'The Crusaders')
    # create a notion client
    notion = NotionAPI(integration_token)
    r = 2
    for row in data[1:]:
        # create properties
        # properties = notion.create_properties_object(database_id, **row)
        row['Scholar Number'] = int(row['Scholar Number'])
        # check if the 'Notion Page ID' column is empty
        if row['Notion Page ID'] == '':
            # create a new page
            new_page = notion.create_page(database_id, **row).replace('-', '')
            row['Notion Page ID'] = new_page
            # new_page = notion.create_page(database_id, Scholar_Number=row['Scholar Number'], Batch = row['Batch'], Email=row['Email Address'])
        else:
            # notion.update_page(database_id, page_id = row['Notion Page ID'], Scholar_Number=row['Scholar Number'], Batch = row['Batch'], Email=row['Email Address'])
            notion.update_page(database_id, row['Notion Page ID'], **row)
        # update the 'Notion Page ID' column with the new page's ID
        update_cell('New Onboarding - The Supreme Coders (Responses)', 'The Crusaders',f'M{r}', f'{row["Notion Page ID"]}')
        r += 1

sync_database()