import mysql.connector
import os

class SQLClient:
    def __init__(self, host, username, password, database, port=3306):
        # Get the values of Docker environment variables
        '''
        self.host = os.environ.get('MYSQL_HOST')
        self.port = os.environ.get('MYSQL_PORT')
        self.user = os.environ.get('MYSQL_USER')
        self.password = os.environ.get('MYSQL_PASSWORD')
        self.database = os.environ.get('MYSQL_DATABASE')
        '''
        self.host = 'localhost'
        self.user = 'root'
        self.port = 3306
        self.password = 'root'
        self.database = 'sync_notion'
        self.conn = None
        self.cursor = None
    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            port = self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, column_names):
        columns = ', '.join([f"{column} {column_type}" for column, column_type in column_names.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()
        print("Table created successfully.")
    
    def clear_table(self, table_name):
        query = f"TRUNCATE TABLE {table_name}"
        self.cursor.execute(query)
        self.conn.commit()
        print("Table cleared successfully.")

    def update_page_id(self, table_name, **kwargs):
        columns = ', '.join([f"{column} = {value}" for column, value in kwargs.items()])
        query = f"INSERT INTO {table_name} SET {columns} ON DUPLICATE KEY UPDATE {columns}"
        self.cursor.execute(query)
        self.conn.commit()
        print("Data inserted/updated successfully.")

    def get_page_id(self, table_name, primary_key, val): 
        query = f"SELECT page_id FROM {table_name} WHERE {primary_key} = {val}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

