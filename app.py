from Model.database import *
import json


class BookManager:
    def __init__(self, db_file_name):
        self.database = DataBase(db_file_name)
        self.database.create_storage()
        self.max_print_length = 50

        self.user_options = {
            "1": {
                "display_text": "Add a new book",
                "execute": self.store_book
            },
            "2": {
                "display_text": "Display all available books",
                "execute": self.display_all_books
            },
            "3": {
                "display_text": "Search specific book by book name",
                "execute": self.find_book
            },
            "4": {
                "display_text": "Read a Book",
                "execute": self.mark_book_as_read
            },
            "5": {
                "display_text": "Delete a Book",
                "execute": self.delete_book
            }
        }

        with open("meta_book_information.json") as meta_book_info_file:
            self.book_info_needed = json.load(meta_book_info_file)

    @staticmethod
    def get_book_name(message="Enter the Book Name : "):
        book_name = input(message)

        while len(book_name) == 0:
            print("Please Enter valid Book Name!!!")
            book_name = input(message)

        book_name = book_name.lower()
        return book_name

    def print_line_seperator(self, seperator="-"):
        print(seperator * self.max_print_length)

    def display_user_menu(self):
        self.print_line_seperator()
        print("USER MENU".center(self.max_print_length))
        self.print_line_seperator()

        for option, content in self.user_options.items():
            print(f"{option}. {content['display_text']}")

        self.print_line_seperator()

    def store_book(self):
        book_info = dict()

        for info in self.book_info_needed:
            meta_book_info = self.book_info_needed[info]

            book_field_data = eval(meta_book_info["value"])

            if meta_book_info["type"] == "TEXT":
                book_field_data = book_field_data.lower()

            book_info[info] = book_field_data

        self.database.store_book(book_info)

        print("Your Book is saved successfully!!!")

    def display_book_info(self, book: dict) -> None:
        for info in self.book_info_needed:
            meta_book_info = self.book_info_needed[info]

            data_to_display = book[info]
            if meta_book_info["type"] == "TEXT":
                data_to_display = data_to_display.title()
            if info == "is_read":
                data_to_display = "Read" if data_to_display else "Not Read"
            print(f"{meta_book_info['display_text']} : {data_to_display}")

    def display_all_books(self):
        list_of_books = self.database.get_all_books()

        for book_no, book in enumerate(list_of_books):
            self.print_line_seperator()
            print(f"Book {book_no + 1}")
            self.print_line_seperator()

            self.display_book_info(book)

            self.print_line_seperator()

        print("All books are printed successfully!!")

    def search_book(self, book_name: str):
        book = self.database.get_book_details(book_name)
        return book

    def find_book(self):
        book_name = self.get_book_name("Enter the Book Name to find : ")

        book = self.search_book(book_name)

        if not book:
            print("Sorry the Book you are finding is not present in our Data Base!!!")
            return

        print("Book Info:")
        self.display_book_info(book)

    def delete_book(self):
        book_name = self.get_book_name("Enter the Book Name to Delete : ")

        book = self.search_book(book_name)

        if not book:
            print("Sorry the book you are trying to delete is not present in our Data Base!!!")
            return

        self.database.delete_book(book_name)
        print("Book Chosen is Deleted!!!")

    def mark_book_as_read(self):
        book_name = self.get_book_name("Enter the Book Name to Read : ")
        book = self.search_book(book_name)

        if not book:
            print("Sorry the book you are trying to read is not present!!!")
            return

        self.database.mark_book_as_read(book_name)
        print("Book Chosen is marked as Read!!!")

    def run(self):
        self.display_user_menu()
        user_input = input("Enter one of the option above : ")

        while user_input != "q":
            if user_input in self.user_options:
                self.user_options[user_input]["execute"]()
            else:
                print("Please Enter valid user option available!!")

            self.display_user_menu()
            user_input = input("Enter one of the option above or (q) to Quit : ")

        print('Thank you for your interaction with "Book Manager" your responses are being saved safely!!!')


if __name__ == "__main__":
    database_file_name = "data.db"
    BookManager(database_file_name).run()
