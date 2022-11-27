import uuid

from infra.TableOptions import TableOptions
from models.Book import Book
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.BookController import BookController


class BookView:
    __bookController: 'BookController'

    def __init__(self, bookController: 'BookController', printGenerator):
        self.__bookController = bookController
        self.__printGenerator = printGenerator

    def printCreateBook(self):
        bookName = self.__printGenerator.inputData("Digite o Nome do livro")
        bookAuthor = self.__printGenerator.inputData("Digite o Autor do livro")
        bookPublisher = self.__printGenerator.inputData(
            "Digite a Editora do livro")
        bookPrice = float(self.__printGenerator.inputData(
            "Digite o preço do multa do empréstimo do livro"))
        codBook = f'Book-{uuid.uuid4()}'

        book = Book(codBook, bookName, bookPrice, bookAuthor, bookPublisher)

        self.__bookController.createBook(book)

    def printBooks(self):
        books = self.__bookController.listBooks()
        booksTable = TableOptions("Livros que possuimos", [
                                  "Código", "Nome", "Autor", "Editora", "Preço"], books)
        self.__printGenerator.printTable(booksTable)
