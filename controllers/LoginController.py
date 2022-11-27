from models.User import User

from controllers.DatabaseController import DatabaseController


class LoginController:
    def __init__(self, printGenerator):
        self.__user = None

        self.__printGenerator = printGenerator
        self.__databaseController = DatabaseController(filePath='./data/usuarios.txt')

    def createUser(self, user: 'User'):
        codeUser = user.getCodeUser()
        name = user.getName()
        userType = user.getType()
        login = user.getLogin()
        password = user.getPassword()

        self.__databaseController.saveEntry(f'{codeUser},{name},{userType},{login},{password}')

    def getUsers(self):
        users = self.__databaseController.getEntries()

        mappedUsers = []

        for user in users:
            if len(user) > 0:
                mappedUsers.append(
                    User(
                        codeUser=user[0],
                        name=user[1],
                        typeUser=user[2],
                        login=user[3],
                        password=user[4]
                    )
                )

        return mappedUsers

    def getUserLoggedIn(self):
        return self.__user

    def isUserLoggedIn(self):
        return self.__user is not None

    def logout(self):
        self.__user = None

    def login(self, username, password):
        users = self.getUsers()

        for user in users:
            if user.getLogin() == username and user.getPassword() == password:
                self.__user = user
                break

        if not self.__user:
            self.__printGenerator.printError(
                "Não foi possível encontrar\no usuário ou senha digitados"
            )

        return self.__user
