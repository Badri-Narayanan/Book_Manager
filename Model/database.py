from .database_connection import DataBaseConnection
from typing import List, Dict, Union
import json

Book = Dict[str, Union[str, int]]


class DataBase:
    def __init__(self, db_file_name: str):
        self.db_file_name = db_file_name
        with open("meta_book_information.json") as meta_book_info_file:
            self.book_info_needed = json.load(meta_book_info_file)

    def get_table_schema(self) -> str:
        table_schema = ""
        for field, field_details in self.book_info_needed.items():
            if len(table_schema) != 0:
                table_schema += ","

            table_schema += f"{field} {field_details['type']}"

            if "default_value" in field_details:
                table_schema += f" DEFAULT {field_details['default_value']}"

            if "constraints" in field_details:
                table_schema += f" {field_details['constraints']}"

        return table_schema

    def create_storage(self) -> None:
        table_schema = self.get_table_schema()
        print(table_schema)
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS BookManager({table_schema})")

    def get_all_books(self) -> List[Book]:
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM BookManager LIMIT 20")
            list_of_books = cursor.fetchall()
            return [{"name": book[0], "author": book[1], "is_read": book[2]} for book in list_of_books]

    def store_book(self, book: dict) -> None:
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO BookManager VALUES(?, ?, ?)", (book["name"], book["author"], 0))

    def mark_book_as_read(self, book_name: str) -> None:
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE BookManager SET is_read = 1 WHERE name = ?", (book_name,))

    def get_book_details(self, book_name: str) -> Dict[str, Union[str, int]]:
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM BookManager WHERE name = ? LIMIT 20", (book_name,))
            book = cursor.fetchone()
            if not book or len(book) == 0:
                return None
            return {"name": book[0], "author": book[1], "is_read": book[2]}

    def delete_book(self, book_name: str) -> None:
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM BookManager WHERE name = ?", (book_name,))


