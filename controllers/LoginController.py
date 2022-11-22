from infra.PrintGenerator import PrintGenerator


class LoginController:
    def __init__(self):
        self.__user = None

        self.__users = [
            {
                'login': 'admin',
                'password': 'admin'
            },
            {
                'login': 'jose',
                'password': '1234'
            }
        ]

    def getUserLogin(self):
        return self.__user

    def isUserLoggedIn(self):
        return self.__user is not None

    def logout(self):
        self.__user = None

    def login(self, username, password):
        try:
            self.__user = next(
                user for user in self.__users if user.get("login") == username and user.get("password") == password
            )

            return self.__user
        except StopIteration:
            PrintGenerator.printError("Não foi possível encontrar\no usuário ou senha digitados")



