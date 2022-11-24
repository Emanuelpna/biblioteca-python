from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.LoginController import LoginController

from infra.PrintClient import PrintClient


class LoginView:
    __loginController: 'LoginController'

    def __init__(self, loginController: 'LoginController'):
        self.__loginController = loginController

    def printLogin(self):
        PrintClient.printHeader("Faça seu Login")

        login = input('Qual o seu usuário? ')
        password = input('Qual a sua senha? ')

        self.__loginController.login(login, password)

    def printLogout(self):
        if not self.__loginController.isUserLoggedIn():
            PrintClient.printHeader('Você não está conectado em nenhuma conta')
            return

        self.__loginController.logout()

        PrintClient.printHeader('Você foi desconectado com sucesso')
