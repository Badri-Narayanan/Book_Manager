from typing import List, Dict, Union

Book = Dict[str, Union[str, int]]


class DataBase:
    def __init__(self, db_file_name: str):
        self.db_file_name = db_file_name

    def create_storage(self) -> None:
        raise NotImplementedError("This method needs to be implemented!!!")

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


