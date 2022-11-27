from models.Loan import Loan

from controllers.DatabaseController import DatabaseController


class LoanController:
    def __init__(self):
        self.__databaseController = DatabaseController(filePath='./data/emprestimo.txt')

    def createLoan(self, loan):
        codLoan = loan.getCodLoan()
        codClient = loan.getCodClient()
        codBook = loan.getCodBook()
        dtLoan = loan.getDtLoan()

        self.__databaseController.saveEntry(f'{codLoan},{codClient},{codBook},{dtLoan}')

    def listLoans(self):
        loans = self.__databaseController.getEntries()
        mappedLoans = []
        for loan in loans:
            mappedLoans.append(Loan(codLoan=loan[0], codClient=loan[1], codBook=loan[2], dtLoan=loan[3]))
        return mappedLoans

    def getLoanByCodLoan(self, codLoan):
        loans = self.listLoans()
        for loan in loans:
            if codLoan == loan.getCodLoan():
                return loan

    def getLoanByCodBook(self, codBook):
        loans = self.listLoans()
        for loan in loans:
            if codBook == loan.getCodBook():
                return loan
