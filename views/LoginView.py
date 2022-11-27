from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.LoginController import LoginController


class LoginView:
    __loginController: 'LoginController'

    def __init__(self, loginController: 'LoginController', printGenerator):
        self.__loginController = loginController
        self.__printGenerator = printGenerator

    def printLogin(self):
        self.__printGenerator.printHeader("Faça seu Login")

        login = self.__printGenerator.inputData('Qual o seu usuário? ')
        password = self.__printGenerator.inputData('Qual a sua senha? ')

        self.__loginController.login(login, password)

    def printLogout(self):
        if not self.__loginController.isUserLoggedIn():
            self.__printGenerator.printHeader(
                'Você não está conectado em nenhuma conta')
            return

        self.__loginController.logout()

        self.__printGenerator.printHeader('Você foi desconectado com sucesso')
