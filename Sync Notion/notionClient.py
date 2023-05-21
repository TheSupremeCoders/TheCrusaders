import requests

class NotionAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13"
        }

    def create_page(self, database_id, properties):
        url = f"{self.base_url}/pages"

        data = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties
        }

        response = requests.post(url, headers=self.headers, json=data)
        if(response.status_code == 200):
            print("Page created successfully")
        else: 
            print("Error creating page")
            print(response.json())
        response.raise_for_status()
        # return the page ID of the newly created page
        return response.json()["id"]
    
    def get_pages_in_database(self, database_id):
        url = f"{self.base_url}/databases/{database_id}/query"

        next_cursor = None
        pages = []
        while True:
            data = {
                "start_cursor": next_cursor
            }

            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            data = response.json()
            pages += data["results"]

            if data["has_more"]:
                next_cursor = data["next_cursor"]
            else:
                break
        data = response.json()
        return data["results"]
    

    def retrieve_database(self, database_id):
        url = f"{self.base_url}/databases/{database_id}"

        response = requests.get(url, headers=self.headers)
        if(response.status_code == 200):
            print("Database retrieved successfully")
        else: 
            print("Error retrieving database")
            print(response.json())

        return response.json()

    def update_page(self, page_id, properties):
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
    
    def create_properties_object(self,template_properties, **kwargs):
        properties = {}
        for key, value in kwargs.items():
            if key in template_properties:
                if template_properties[key]["type"] == "title": 
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
                elif template_properties[key]["type"] == "rich_text":
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
                elif template_properties[key]["type"] == "number":
                    properties[key] = {
                        "number": value
                    }
                elif template_properties[key]["type"] == "checkbox":
                    properties[key] = {
                        "checkbox": value
                    }
            elif template_properties[key]["type"] == "select":
                select_id = template_properties[key]["select"]["id"]
                select_value = next(
                    (option for option in template_properties[key]["select"]["options"] if option["name"] == value),
                    None
                )
                if select_value:
                    properties[key] = {
                        "select": {
                            "id": select_id,
                            "name": select_value["name"],
                            "color": select_value["color"]
                        }
                    }
            elif template_properties[key]["type"] == "date":
                properties[key] = {
                    "date": {
                        "start": value
                    }
                }
            elif template_properties[key]["type"] == "relation":
                properties[key] = {
                    "relation": []
                }
            elif template_properties[key]["type"] == "url":
                properties[key] = {
                    "url": value
                }
            elif template_properties[key]["type"] == "created_time":
                properties[key] = {
                    "created_time": value
                }    
            elif template_properties[key]["type"] == "last_edited_time":
                properties[key] = {
                    "last_edited_time": value
                }
            elif template_properties[key]["type"] == "last_edited_by":
                properties[key] = {
                    "last_edited_by": value
                }
            elif template_properties[key]["type"] == "people":
                properties[key] = {
                    "people": [
                        {
                            "object": "user",
                            "id": value
                        }
                    ]
                }
            elif template_properties[key]["type"] == "files":
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
            elif template_properties[key]["type"] == "checkbox":
                properties[key] = {
                    "checkbox": value
                }
            elif template_properties[key]["type"] == "number":
                properties[key] = {
                    "number": value
                }
            elif template_properties[key]["type"] == "url":
                properties[key] = {
                    "url": value
                }
            elif template_properties[key]["type"] == "email":
                properties[key] = {
                    "email": value
                }
            elif template_properties[key]["type"] == "phone_number":
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
