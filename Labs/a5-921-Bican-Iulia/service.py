"""
    Service class includes functionalities for implementing program features
"""
import re
import random
from src.domain.entity import Book


class Service:

    def __init__(self):
        self._books = []
        self._history = []
        self.initialiseBookList()

    def isInBooks(self, isbn):
        for book in self._books:
            if book.Isbn == isbn:
                return True
        return False

    def addBook(self, book):
        """
        Adds a new Book to the list
        :param:self - the object
        :param:book - the book to be added to the book list
        :raise: ValueError - If ISBN already in bookList
        """
        if not self.isInBooks(book.Isbn):
            c = self._books.copy()
            self._history.append(c)
            self._books.append(book)
        else:
            raise ValueError("A book with this ISBN already exists in the list!")

    @property
    def showBooks(self):
        """
        This function returns the list of books
        """
        return self._books

    def undo(self):
        """
        Undoes the last performed modification on the list
        :param: self - the object
        :raise: Exception -  for no more undoes
        """
        if len(self._history) == 0:
            raise Exception("No more undoes.")
        u = self._history.pop()  # returns the last element of the list
        self._books.clear()  # same list but I want it clear
        for e in u:
            self._books.append(e)

    def filter(self, word):
        """
        Filters the list so that the books that have a title containing a given word are deleted
        :param: self - the object
        :param: word - the word to filter by
        :raise: ValueError - if there are no books left in the list to be filtered
        """
        c = self._books.copy()
        self._history.append(c)
        i = 0
        while i < len(self._books):
            # Regex function to find a substring in a string
            if re.search(word, self._books[i].Title, re.IGNORECASE):
                self._books.remove(self._books[i])
            else:
                i += 1
        if len(self._books) == 0:
            raise Exception("No more books to be filtered!")

    def initialiseBookList(self):
        ISBNList = ["978-1-56619-909-4", "978-1-56625-919-6", "978-1-55625-978-3", "978-1-56625-936-6",
                    "978-1-24462-657-8", "978-1-51465-346-2", "978-1-56231-564-3", "978-1-27465-826-7",
                    "978-1-19452-286-5", "978-1-19452-286-9", "978-1-23015-025-0", "978-1-82549-207-1"]
        AuthorList = ["Rudyard Kipling", "Jane Austen", "Lev Tolstoi", "William Shakespeare", "Agatha Christie",
                      "Mark Twain", "Margaret Atwood", "Ernest Hemingway", "Marcel Proust", "James Joyce",
                      "Feodor Dostoievski", "Virginia Woolf", "F. Scott Fitzgerald", "Charles Dickens"]
        TitleList = ["In Search of Lost Time", "Ulysses", "The great Gatsby", "One Hundred Years of Solitude",
                     "Moby Dick", "War and Peace", "Lolita", "Hamlet", "The Odyssey", "Madame Bovary", "Great Expectations",
                     "The Trial", "The Red and the Black", "Mrs. Dalloway"]
        ISBNListCopy = ISBNList.copy()
        AuthorListCopy = AuthorList.copy()
        TitleListCopy = TitleList.copy()
        i = 0
        while i < 10:
            isbn = random.choice(ISBNListCopy)
            ISBNListCopy.remove(isbn)
            author = random.choice(AuthorListCopy)
            AuthorListCopy.remove(author)
            title = random.choice(TitleListCopy)
            TitleListCopy.remove(title)
            book = Book(isbn, author, title)
            self._books.append(book)
            i = i + 1

def testAdd():
    """
    Test function for Adding Books
    Because I initialised the list in service, the following additions will be numbered starting from position 10
    """
    s = Service()
    e = Book("978-1-17322-286-5", "Anton Chekhov", "The Stories of Anton Chekhov")
    s.addBook(e)
    assert len(s.showBooks) == 11
    e1 = Book("978-2-17392-286-2", "Stendhal", "The Charterhouse of Parma")
    s.addBook(e1)
    assert len(s._books) == 12
    assert s._books[10] == e
    e2 = Book("978-2-17392-679-7", "Voltaire", "Candide")
    s.addBook(e2)
    assert len(s._books) == 13


testAdd()
