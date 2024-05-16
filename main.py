from pprint import pprint
import json
import time
from getpass import getpass


class Books:
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("books.json", "w") as f:
                json.dump([], f)
                data = []
        self.__Books = data

    def commit(self):
        with open("books.json", "w") as f:
            json.dump(self.__Books, f, indent=3)

    def add_book(self, title, author, page_count, id):
        id = id
        title = title
        author = author
        page_count = page_count
        book = {
            "ID": id,
            "Title": title,
            "Author": author,
            "Page Count": page_count
        }
        self.__Books.append(book)
        self.commit()
        print()
        print("successfully registered")
        print()
        main_menu()

    def my_books(self):
        for b in self.__Books:
            pprint(b)
            print()
        main_menu()

    def delete_books(self, book_id):
        book_id = book_id
        index = 0
        yes = 0
        for books in self.__Books:
            if books["ID"] == book_id:
                self.__Books.pop(index)
                self.commit()
                print("Successfully deleted")
                yes +=1
                break
        if yes == 0:
            print("Not found try again :)")
            index += 1
        main_menu()

def main_menu():
    b = Books()
    print("1. Add book")
    print("2. My books")
    print("3. Delete books")
    ch = input()
    match ch:
        case "1":
            id = time.time_ns()
            title = input("Title: ")
            author = input("Author: ")
            page_count = input("Page count: ")
            b.add_book(title, author, page_count, id)
        case "2":
            b.my_books()
        case "3":
            book_id = int(input("Book Id: "))
            b.delete_books(book_id)
main_menu()



