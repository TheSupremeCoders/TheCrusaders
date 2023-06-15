import mysql.connector

class SQLClient:
    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.port = port

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.username,
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

