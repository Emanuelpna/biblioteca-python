class Book:

    def __init__(self, codBook, name, finePrice, author, publisher):
        self.__cod = codBook
        self.__name = name
        self.__finePrice = finePrice
        self.__author = author
        self.__publisher = publisher

    def setCod(self, codBook):
        self.__cod = codBook

    def getCod(self):
        return self.__cod

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setFinePrice(self, finePrice):
        self.__finePrice = finePrice

    def getFinePrice(self):
        return self.__finePrice

    def setAuthor(self, author):
        self.__author = author

    def getAuthor(self):
        return self.__author

    def setPublisher(self, publisher):
        self.__publisher = publisher

    def getPublisher(self):
        return self.__publisher
