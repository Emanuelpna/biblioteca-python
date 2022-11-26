from controllers.DatabaseController import DatabaseController
from models.Book import Book


class BookController:

    def __init__(self):
        self.__databaseController = DatabaseController(filePath='./data/livros.txt')

    def createBook(self, book):
        codeBook = book.getCod()
        name = book.getName()
        author = book.getAuthor()
        publisher = book.getPublisher()
        finePrice = book.getFinePrice()

        self.__databaseController.saveEntry(f'{codeBook},{name},{author},{publisher},{finePrice}')

    def listBooks(self):
        books = self.__databaseController.getEntries()
        mappedBooks = []
        for book in books:
            if len(book) > 0:
                mappedBooks.append(
                    Book(codBook=book[0], name=book[1], author=book[2], publisher=book[3], finePrice=book[4])
                )
        return mappedBooks

    def getBookByName(self, name):
        books = self.listBooks()
        for book in books:
            if name == book.getName():
                return book
