from enum import Enum

TYPE_USER = Enum('TYPE_USER', ['COSTUMER', 'LIBRARIAN'])


class User:
    __name: str
    __login: str
    __password: str
    __codeUser: str
    __type: 'TYPE_USER'

    def __init__(self, codeUser: str, name: str, typeUser: 'TYPE_USER', login: str, password: str):
        self.__name = name
        self.__type = typeUser
        self.__codeUser = codeUser

        self.__login = login
        self.__password = password

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getType(self):
        return self.__type

    def setType(self, type: 'TYPE_USER'):
        self.__type = type

    def getCodeUser(self):
        return self.__codeUser

    def setCodeUser(self, codeUser: str):
        self.__codeUser = codeUser

    def getLogin(self):
        return self.__login

    def setLogin(self, login: str):
        self.__login = login

    def getPassword(self):
        return self.__password

    def setPassword(self, password: str):
        self.__password = password
