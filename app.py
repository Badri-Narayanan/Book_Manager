from Model.database import DataBase, Dict, Union
import json


class BookManager:
    def __init__(self, db_file_name):
        self.database = DataBase(db_file_name)
        self.max_print_length = 50
        with open("meta_book_information.json") as meta_book_info_file:
            self.book_info_needed = json.load(meta_book_info_file)

    def display_user_menu(self):
        raise NotImplementedError("Yet to Implement this section!!!")

    def store_book(self):
        book_info = dict()

        for info in self.book_info_needed:
            meta_book_info = self.book_info_needed[info]

            book_info[info] = eval(meta_book_info["value"])

        self.database.store_book(book_info)

        print("Your Book is saved successfully!!!")

    def display_book_info(self, book: dict) -> None:
        for info in self.book_info_needed:
            meta_book_info = self.book_info_needed[info]

            print(f"{meta_book_info['display_text']} : {book[info]}")

    def display_all_books(self):
        list_of_books = self.database.get_all_books()

        for book_no, book in enumerate(list_of_books):
            print("-" * self.max_print_length)
            print(f"Book {book_no}")
            print("-" * self.max_print_length)

            self.display_book_info(book)

            print("-" * self.max_print_length)

        print("All books are printed successfully!!")

    def search_book(self, book_name: str) -> Dict[str, Union(str, bool)]:
        book = self.database.get_book_details(book_name)

        return book

    def find_book(self):
        book_name = input("Enter the Book Name to find : ")

        book = self.search_book(book_name)

        if not book:
            print("Sorry the Book you are finding is not present in our Data Base!!!")
            return

        print("Book Info:")
        self.display_book_info(book)

    def delete_book(self):
        book_name = input("Enter the Book Name to delete : ")

        book = self.search_book(book_name)

        if not book:
            print("Sorry the book you are trying to delete is not present in our Data Base!!!")
            return

        self.database.delete_book(book_name)

    def mark_book_as_read(self):
        raise NotImplementedError("Yet to Implement this section!!!")

    def run(self):
        self.display_user_menu()
        user_input = input("Enter one of the option above : ")

        user_options = {
            "1": self.store_book,
            "2": self.display_all_books,
            "3": self.find_book,
            "4": self.mark_book_as_read,
            "5": self.delete_book
        }

        while user_input != "q":
            if user_input in user_options:
                user_options[user_input]()
            else:
                print("Please Enter valid user option available!!")

            self.display_user_menu()
            user_input = input("Enter one of the option above : ")

        print('Thank you for your interaction with "Book Manager" your responses are being saved safely!!!')
