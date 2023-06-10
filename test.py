
from google_custom_module import *
from sqlclient import SQLClient
sqlClient = SQLClient('localhost', 'root', 'root', 'sync_notion')
sqlClient.connect()
print('sqlClient connected')
sqlClient.update_page_id('problems', name=f"'sub1'", page_id=f"'dfasdfasd'")
sqlClient.disconnect()
print('sqlClient disconnected')