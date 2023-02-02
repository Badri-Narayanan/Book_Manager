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
        raise NotImplementedError("Not Yet Implemented!!!")

    def create_storage(self) -> None:
        table_schema = self.get_table_schema()
        with DataBaseConnection(self.db_file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS BOOKMANAGER({table_schema})")

    def get_all_books(self) -> List[Book]:
        raise NotImplementedError("This method needs to be implemented!!!")

    def store_book(self, book: dict) -> None:
        raise NotImplementedError("This method needs to be implemented!!!")

    def mark_book_as_read(self, book_name: str) -> None:
        raise NotImplementedError("This method needs to be implemented!!!")

    def get_book_details(self, book_name: str) -> Dict[str, Union[str, int]]:
        raise NotImplementedError("This method needs to be implemented!!!")

    def delete_book(self, book_name: str):
        raise NotImplementedError("This method needs to be implemented!!!")


