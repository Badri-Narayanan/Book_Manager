import sqlite3


class DataBaseConnection:
    def __init__(self, file_name):
        self.host = file_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.connection.commit()
        finally:
            self.connection.close()
