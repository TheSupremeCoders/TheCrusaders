import notionClient
import os
import json

secret = json.load(open("secret.json"))
notion_token = secret["notion_token"]

# create a new Notion client
client = notionClient.NotionAPI(notion_token)
members_database_id = secret['databases']['members']['id']

# get the properties object from create_properties_object function
template_properties = client.retrieve_database(members_database_id)["properties"]
# check if there exists a page in the hash table for the given scholar number

page_id = secret['databases']['members']['hash_map'].get("222120031")
if(page_id != None):
    properties = client.create_properties_object(template_properties=template_properties, Name="Arnav", Codechef_ID="arnav", Scholar_Number=222120031)
    client.update_page(page_id, properties)