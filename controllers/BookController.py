from controllers.DatabaseController import DatabaseController
from models.Book import Book

class BookController:

    def __init__(self):
        self.__databaseController = DatabaseController(filePath='./data/livros.txt')

    def createBook(self, book):
        name = book.getName()
        publisher = book.getPublisher()
        finePrice = book.getFinePrice()
        author = book.getAuthor()

        self.__databaseController.saveEntry(f'{name},{author},{publisher},{finePrice}')

    def listBooks(self):
        books = self.__databaseController.getEntries()
        mappedBooks = []
        for book in books:
            mappedBooks.append(Book(codBook=book[0], name=book[1], author=book[2], publisher=book[3], finePrice=book[4]))
        return mappedBooks

    def getBookByName(self, name):
        books = self.listBooks()
        for book in books:
            if name == book.getName():
                return book

