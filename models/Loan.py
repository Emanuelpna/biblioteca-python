class Loan():
    def __init__(self, codLoan:int, codClient:int, nmBook:int, dtLoan:str):              
        self.codloan:int = codLoan
        self.codClient:int = codClient
        self.nmBook:int = nmBook
        self.dtLoan:str = dtLoan
    
    def setCodLoan(self, codLoan):
        self.codloan = codLoan

    def getCodLoan(self):
        return self.codloan

    def setCodClient(self, codClient):
        self.codloan = codClient

    def getCodClient(self):
        return self.codClient

    def setNmBook(self, nmBook):
        self.nmBook = nmBook

    def getNmBook(self):
        return self.nmBook

    def setDtLoan(self, dtLoan):
        self.dtLoan = dtLoan

    def getDtLoan(self):
        return self.dtLoan