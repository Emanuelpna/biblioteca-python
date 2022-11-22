from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.LoginController import LoginController

from infra.PrintGenerator import PrintGenerator


class LoginView:
    __loginController: 'LoginController'

    def __init__(self, loginController: 'LoginController'):
        self.__loginController = loginController

    def printLogin(self):
        PrintGenerator.printHeader("Faça seu Login")

        login = input('Qual o seu usuário? ')
        password = input('Qual a sua senha? ')

        self.__loginController.login(login, password)

    def printLogout(self):
        if not self.__loginController.isUserLoggedIn():
            PrintGenerator.printHeader('Você não está conectado em nenhuma conta')
            return

        self.__loginController.logout()

        PrintGenerator.printHeader('Você foi desconectado com sucesso')
