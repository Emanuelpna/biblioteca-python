from __future__ import annotations

from infra.TableOptions import TableOptions
from models.Loan import Loan
import uuid
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from controllers.LoanController import LoanController
    from controllers.BookController import BookController
    from controllers.LoginController import LoginController


class LoanView:
    __loanController: 'LoanController'
    __bookController: 'BookController'
    __loginController: 'LoginController'

    def __init__(self, loanController: 'LoanController', bookController: 'BookController',
                 loginController: 'LoginController', printGenerator):
        self.__loanController = loanController
        self.__printGenerator = printGenerator
        self.__bookController = bookController
        self.__loginController = loginController

    def printSelectBook(self):
        books = self.__bookController.listBooks()
        booksNames = []
        for book in books:
            loan = self.__loanController.getLoanByCodBook(book.getCod())
            if not loan:
                booksNames.append(book.getName())

        bookName = self.__printGenerator.printSelect("Escolha um dos livros disponiveis", booksNames)

        book = self.__bookController.getBookByName(bookName)
        codCliente = self.__loginController.getUserLogin().get('login')
        loanDate = datetime.now().strftime("%m/%d/%Y")
        codLoan = f'Loan-{uuid.uuid4()}'

        loan = Loan(codLoan, codCliente, book.getCod(), loanDate)

        self.__loanController.createLoan(loan)

    def printLoans(self):
        loans = self.__loanController.listLoans()
        loansTable = TableOptions("Livros emprestados", ["Código", "Cliente", "Código do livro", "Data empréstimo"], loans)
        self.__printGenerator.printTable(loansTable)
