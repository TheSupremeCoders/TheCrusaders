from sqlclient import SQLClient
from notionClient import NotionAPI

import json 

class ProblemClient:
    def __init__(self):
        notion_token = json.load(open('secret.json'))['notion_token']
        self.database_id = json.load(open('secret.json'))['databases']['problems']
        self.submission_database_id = json.load(open('secret.json'))['databases']['submissions']

        self.sqlClient = SQLClient('thesupremecoders', 'root', 'root', 'sync_notion')
        self.notionClient = NotionAPI(notion_token)

        self.sqlClient.connect()
        print('sqlClient connected')
        self.sqlClient.create_table('problems', {'name': 'VARCHAR(255) PRIMARY KEY', 'page_id': 'VARCHAR(255)'})
        self.sqlClient.create_table('members', {'scholar_number' : 'INT PRIMARY KEY', 'page_id': 'VARCHAR(255)'})

    def close(self):
        print('sqlClient disconnected')
        self.sqlClient.disconnect()
            


class Problem:
    def __init__(self, problem_client, name, problem_link, submission_link, submission_id, platform, scholar_number):
        self.name = name
        self.problem_link = problem_link
        self.submission_link = submission_link
        self.platform = platform
        self.problem_page_id = None

        if problem_client.sqlClient.get_page_id('problems', 'name', f"'{self.name}'") is None:
            self.problem_page_id = problem_client.notionClient.create_page(database_id = problem_client.database_id, icon='🟢', Name=self.name, URL=self.problem_link, Platform=self.platform)
            problem_client.sqlClient.update_page_id('problems', name=f"'{self.name}'", page_id=f"'{self.problem_page_id}'")
        else:
            self.problem_page_id = problem_client.sqlClient.get_page_id('problems', 'name', f"'{self.name}'")
        
        # get page id of the member
        self.member_page_id = problem_client.sqlClient.get_page_id('members', 'scholar_number', scholar_number)
        # create a submission page
        problem_client.notionClient.create_page(database_id = problem_client.submission_database_id, icon='🖍️', Submission_ID=submission_id, Problem=[self.problem_page_id], Submission_Link=self.submission_link, Submitted_By=[self.member_page_id])

    
    def __str__(self):
        return f'~ {self.name}'
    
    def html_str(self):
        return f'<a href="{self.link}">{self.name}</a>'