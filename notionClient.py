import requests
import json

class NotionAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.template_properties = {}

    def create_page(self, database_id, icon=None, **kwargs):
        properties = self.create_properties_object(database_id=database_id, **kwargs)
        url = f"{self.base_url}/pages"

        data = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties
        }

        # check if icon has '/' in it, if so, it's an external icon
        icon_type = None
        if icon is not None and icon.startswith("http"):
            icon_type = "external"
        else: 
            icon_type = "emoji"

        if icon and icon_type:
            if icon_type == "emoji":
                data["icon"] = {
                    "type": "emoji",
                    "emoji": icon
                }
            elif icon_type == "external":
                data["icon"] = {
                    "type": "external",
                    "external": {
                        "url": icon
                    }
                }
            else:
                raise Exception("Invalid icon type. Must be either 'emoji' or 'external'.")

        response = requests.post(url, headers=self.headers, json=data)
        if(response.status_code == 200):
            print("Page created successfully")
        else: 
            print("Error creating page")
            print(response.json())
        response.raise_for_status()
        # return the page ID of the newly created page
        return response.json()["id"]
    
    def get_pages_in_database(self, database_id, filter=None, sorts=None):
        url = f"{self.base_url}/databases/{database_id}/query"
        query_data = {}
        results = []
        if filter is not None: 
            query_data['filter'] = filter
        if sorts is not None:
            query_data['sorts'] = sorts
        else: 
            query_data['sorts'] = [
                {
                    "property": "Created time",
                    "direction": "ascending"
                }
            ]
        next_cursor = None
        while True:
            if next_cursor:
                query_data['start_cursor'] = next_cursor

            response = requests.post(url, headers=self.headers, json=query_data)
            data = response.json()

            results.extend(data.get('results', []))
            next_cursor = data.get('next_cursor')
            if not next_cursor:
                break

        # Extract page IDs
        page_ids = [page['id'] for page in results]
    
        return page_ids

    def retrieve_database(self, database_id):
        url = f"{self.base_url}/databases/{database_id}"

        response = requests.get(url, headers=self.headers)
        if(response.status_code == 200):
            print("Database retrieved successfully")
        else: 
            print("Error retrieving database")
            print(response.json())

        return response.json()

    def update_page(self, database_id, page_id, **kwargs):
        properties = self.create_properties_object(database_id=database_id, **kwargs)
        url = f"{self.base_url}/pages/{page_id}"

        data = {
            "properties": properties
        }

        response = requests.patch(url, headers=self.headers, json=data)
        if(response.status_code == 200):
            print("Page updated successfully")
        else:
            print("Error updating page")
            print(response.json())


    def delete_page(self, page_id):
        url = f"{self.base_url}/pages/{page_id}"

        response = requests.delete(url, headers=self.headers)

        if(response.status_code == 200):
            print("Page deleted successfully")
            return True
        else:
            print("Error deleting page")
            print(response.json())
            return False
    

    def create_properties_object(self,database_id, **kwargs):
        # check if self.template_properties[database_id] exists
        if database_id not in self.template_properties:
            self.template_properties[database_id] = self.retrieve_database(database_id)['properties']
        properties = {}
        for key, value in kwargs.items():
            if key in self.template_properties[database_id]:
                if self.template_properties[database_id][key]["type"] == "title": 
                    properties[key] = {
                        "title": [
                            {
                                "type": "text",
                                "text": {
                                    "content": value
                                }
                            }
                        ]
                    }
                elif self.template_properties[database_id][key]["type"] == "rich_text":
                    properties[key] = {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": value
                                }
                            }
                        ]
                    }
                elif self.template_properties[database_id][key]["type"] == "number":
                    properties[key] = {
                        "number": value
                    }
                elif self.template_properties[database_id][key]["type"] == "checkbox":
                    properties[key] = {
                        "checkbox": value
                    }
                elif self.template_properties[database_id][key]["type"] == "select":
                    properties[key] = {
                        "select": {
                            "name": value
                        }
                    }
                elif self.template_properties[database_id][key]["type"] == "date":
                    properties[key] = {
                        "date": {
                            "start": value
                        }
                    }
                elif self.template_properties[database_id][key]["type"] == "relation":
                    properties[key] = {
                        "relation": [{'id': page_id} for page_id in value]
                    }
                elif self.template_properties[database_id][key]["type"] == "url":
                    properties[key] = {
                        "url": value
                    }
                elif self.template_properties[database_id][key]["type"] == "created_time":
                    properties[key] = {
                        "created_time": value
                    }    
                elif self.template_properties[database_id][key]["type"] == "last_edited_time":
                    properties[key] = {
                        "last_edited_time": value
                    }
                elif self.template_properties[database_id][key]["type"] == "last_edited_by":
                    properties[key] = {
                        "last_edited_by": value
                    }
                elif self.template_properties[database_id][key]["type"] == "people":
                    properties[key] = {
                        "people": [
                            {
                                "object": "user",
                                "id": value
                            }
                        ]
                    }
                elif self.template_properties[database_id][key]["type"] == "files":
                    properties[key] = {
                        "files": [
                            {
                                "name": value,
                                "type": "external",
                                "external": {
                                    "url": value
                                }
                            }
                        ]
                    }
                elif self.template_properties[database_id][key]["type"] == "checkbox":
                    properties[key] = {
                        "checkbox": value
                    }
                elif self.template_properties[database_id][key]["type"] == "number":
                    properties[key] = {
                        "number": value
                    }
                elif self.template_properties[database_id][key]["type"] == "url":
                    properties[key] = {
                        "url": value
                    }
                elif self.template_properties[database_id][key]["type"] == "email":
                    properties[key] = {
                        "email": value
                    }
                elif self.template_properties[database_id][key]["type"] == "phone_number":
                    properties[key] = {
                        "phone_number": value
                    }
                else:
                    properties[key] = {
                        "text": {
                            "content": value
                        }
                    }
        return properties
    
    def get_page_attributes(self, page_id):
        url = f"{self.base_url}/pages/{page_id}"

        response = requests.get(url, headers=self.headers)
        if(response.status_code == 200):
            print("Page retrieved successfully")
        else: 
            print("Error retrieving page")
            print(response.json())
        
        attributes = {}
        data = response.json()

        # Iterate over each property key-value pair
        for key, value in data.get("properties", {}).items():
            prop_type = value.get("type")

            # Handle different property types and extract relevant values
            if prop_type == "title":
                title_value = value.get(prop_type)[0].get("plain_text")
                attributes[key] = title_value
            elif prop_type == "rich_text":
                rich_text_values = [text.get("plain_text") for text in value.get(prop_type)]
                attributes[key] = rich_text_values
            elif prop_type == "number":
                number_value = value.get(prop_type)
                attributes[key] = number_value
            elif prop_type == "select":
                select_value = value.get(prop_type).get("name")
                attributes[key] = select_value
            elif prop_type == "multi_select":
                attributes[key] = value.get(prop_type)
            elif prop_type == "date":
                date_value = value.get(prop_type).get("start")
                attributes[key] = date_value
            elif prop_type == "checkbox":
                checkbox_value = value.get(prop_type)
                attributes[key] = checkbox_value
            elif prop_type == "url":
                url_value = value.get(prop_type)
                attributes[key] = url_value
            elif prop_type == "email":
                email_value = value.get(prop_type)
                attributes[key] = email_value
            elif prop_type == "phone_number":
                phone_value = value.get(prop_type)
                attributes[key] = phone_value
            elif prop_type == "formula":
                formula_value = value.get(prop_type).get("expression")
                attributes[key] = formula_value
            elif prop_type == "relation":
                relation_values = [item.get("id") for item in value.get(prop_type)]
                attributes[key] = relation_values
            elif prop_type == "rollup":
                rollup_value = value.get(prop_type).get("array")
                attributes[key] = rollup_value
            elif prop_type == "created_time":
                created_time_value = value.get(prop_type)
                attributes[key] = created_time_value
            elif prop_type == "created_by":
                created_by_value = value.get(prop_type)
                attributes[key] = created_by_value
            elif prop_type == "last_edited_time":
                last_edited_time_value = value.get(prop_type)
                attributes[key] = last_edited_time_value
            elif prop_type == "last_edited_by":
                last_edited_by_value = value.get(prop_type)
                attributes[key] = last_edited_by_value

        return attributes