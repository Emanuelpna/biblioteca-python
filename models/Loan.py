class Loan:
    def __init__(self, codLoan: int, codClient: int, codBook: int, dtLoan: str):
        self.codloan: int = codLoan
        self.codClient: int = codClient
        self.codBook: int = codBook
        self.dtLoan: str = dtLoan

    def setCodLoan(self, codLoan):
        self.codloan = codLoan

    def getCodLoan(self):
        return self.codloan

    def setCodClient(self, codClient):
        self.codloan = codClient

    def getCodClient(self):
        return self.codClient

    def setCodBook(self, codBook):
        self.codBook = codBook

    def getCodBook(self):
        return self.codBook

    def setDtLoan(self, dtLoan):
        self.dtLoan = dtLoan

    def getDtLoan(self):
        return self.dtLoan

    def toList(self):
        codLoan = self.getCodLoan()
        codClient = self.getCodClient()
        codBook = self.getCodBook()
        dtLoan = self.getDtLoan()

        return [codLoan, codClient, codBook, dtLoan]
