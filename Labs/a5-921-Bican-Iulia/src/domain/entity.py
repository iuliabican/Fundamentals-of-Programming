"""
    Entity class should be coded here
"""
import re


class Book:
    """
    Abstract data Title - Book
    """

    def __init__(self, isbn, author, title):
        """
        Initialises a book through its characteristics
        :param: isbn - books unique code
        :param: author - book's author
        :param: title - book's title
        """
        self._isbn = isbn
        self._author = author
        self._title = title

    # Setters and Getters

    @property
    def Isbn(self):
        return self._isbn

    @Isbn.setter
    def Isbn(self, inputedIsbn):
        self._isbn = inputedIsbn

    @property
    def Author(self):
        return self._author

    @Author.setter
    def Author(self, inputedAuthor):
        self._author = inputedAuthor

    @property
    def Title(self):
        return self._title

    @Title.setter
    def Title(self, inputedTitle):
        self._title = inputedTitle

    def __str__(self):
        """
        Provides a string representation for the book
        :return: a string
        """
        return "ISBN: " + self._isbn + ", Author: " + self._author.ljust(19) + ", Title: " + self._title.ljust(20)


def test_CreateBook():
    """
      Test function for creating books
    """
    # create the Book of Isbn = 978-1-56619-909-4, Author = J.K. Rowling, Title = Harry Potter and the Sorcerer's Stone
    b1 = Book("978-1-56619-909-4", "J.K. Rowling", "Harry Potter and the Sorcerer's Stone")
    assert b1.Isbn == "978-1-56619-909-4"
    assert b1.Author == "J.K. Rowling"
    assert b1.Title == "Harry Potter and the Sorcerer's Stone"
    b1 = Book("978-1-56619-909-9", "Rudyard Kipling", "The Jungle Book")
    assert b1.Isbn == "978-1-56619-909-9"
    assert b1.Author == "Rudyard Kipling"
    assert b1.Title == "The Jungle Book"


test_CreateBook()
# isbn = re.fullmatch('978[0-9\-]+', "978-1-56619-909-4")
# print(isbn.string == "978-1-56619-909-4")
