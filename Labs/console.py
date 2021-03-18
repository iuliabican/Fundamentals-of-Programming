"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
import re

from src.domain.entity import Book
from src.services.service import Service


class UI:
    def __init__(self, service):
        self._service = service

    def _printMenu(self):
        """
        Print out the menu of the program
        """
        print("\n------  Books Manager  ------")
        print("    0 - Exit the program")
        print("    1 - Add books to the list")
        print("    2 - Show the current list of books")
        print("    3 - Filter the list so that it contains only books that don't contain a given word in the title")
        print("    u - Undo the last operation that modified the program data")

    def validISBN(self, isbn):
        reIsbn = re.fullmatch('978[0-9\-]+', isbn)
        if reIsbn is None:
            raise Exception("Day needs to to have the following format: 978-x-xxxxx-xxx-x !")

    def validFilterBook(self, word):
        isSpace = bool(re.search(r"\s", word))
        if isSpace:
            raise Exception("Filter can only be done by one word!")

    def addBook(self):
        """
        Adds an book to a list
        """
        a = input("Give ISBN ( format 978-x-xxxxx-xxx-x ): ")
        try:
            self.validISBN(a)
            b = input("Give Author: ")
            c = input("Give Title: ")
            book = Book(a, b, c)
            self._service.addBook(book)
            self.showBooks()
        except Exception as e:
            print(e)

    def showBooks(self):
        """
        Shows the list of books2
        """
        bookList = self._service.showBooks
        i=1
        for book in bookList:
            print((str(i) + " ").ljust(3) + str(book))
            i = i + 1

    def filterBooks(self):
        a = input("Give word by which to filter: ").strip()
        try:
            self.validFilterBook(a)
            self._service.filter(a)
            self.showBooks()
        except Exception as e:
            print(e)

    def undo(self):
        self._service.undo()
        self.showBooks()

    def start(self):
        self._commands = {'1': self.addBook, '2': self.showBooks, '3': self.filterBooks, 'u': self.undo}

        while True:
            self._printMenu()
            m = input().strip()
            # Exit program
            if m == '0':
                return
                # Invalid option
            if m not in self._commands:
                print("Bad command")
            # Run user option
            try:
                self._commands[m]()
            except ValueError as ve:
                print("Error - " + str(ve))
            except Exception as e:
                print("Exception - " + str(e))


service = Service()
ui = UI(service)
ui.start()
