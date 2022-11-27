import uuid
from datetime import datetime

from models.Loan import Loan

from infra.TableOptions import TableOptions

from typing import TYPE_CHECKING
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

    def printNewLoan(self):
        books = self.__bookController.listBooks()
        booksNames = []
        for book in books:
            loan = self.__loanController.getLoanByCodBook(book.getCod())
            if not loan:
                booksNames.append(book.getName())

        bookName = self.__printGenerator.printSelect(
            "Escolha um dos livros disponiveis", booksNames)

        user = self.__loginController.getUserLoggedIn()

        codClient = user.getCodeUser()
        book = self.__bookController.getBookByName(bookName)
        loanDate = datetime.now().strftime("%d/%m/%Y")
        codLoan = f'Loan-{uuid.uuid4()}'

        loan = Loan(codLoan, codClient, book.getCod(), loanDate)

        self.__loanController.createLoan(loan)

        self.__printGenerator.printHeader('Empréstimo Criado com Sucesso')

    def printLoans(self):
        loans = self.__loanController.listLoans()

        loansWithBookName = []
        for loan in loans:
            book = self.__bookController.getBookByCode(loan.getCodBook())
            loansWithBookName.append(
                Loan(
                    codLoan=loan.getCodLoan(),
                    codBook=book.getName(),
                    codClient=loan.getCodClient(),
                    dtLoan=loan.getDtLoan()
                )
            )

        loansTable = TableOptions("Livros emprestados", [
                                  "Código", "Cliente", "Nome do livro", "Data empréstimo"], loansWithBookName)
        self.__printGenerator.printTable(loansTable)
