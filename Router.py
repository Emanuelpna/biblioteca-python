from controllers.LoginController import LoginController
from views.LoginView import LoginView


class Router:
    __loginController: 'LoginController'

    def __init__(self, printGenerator):
        self.__currentPage = None
        self.__lastPage = None

        self.__pages = {
            'index': 0,
            'login': 1,
            'logout': 2,
            'emprestimos': 3,
            'fazer-emprestimo': 4,
            'livros': 5,
            'adicionar-livro': 6,
            'sobre': 7
        }

        self.__printGenerator = printGenerator

        self.__loginController = LoginController(printGenerator)

        self.loginView = LoginView(self.__loginController, printGenerator)

    def getCurrentPage(self):
        return self.__currentPage

    def getLastPage(self):
        return self.__lastPage

    def changePage(self, pageName):
        newPage = self.__pages.get(pageName)

        if not isinstance(newPage, int) or 0 > newPage > 7:
            self.__printGenerator.printError('Página Não Encontrada')

        self.__lastPage = self.__currentPage
        self.__currentPage = newPage

        self.renderPage()

    def renderPage(self):
        self.__printGenerator.printSpace()

        if self.__currentPage == self.__pages.get('login'):
            self.loginView.printLogin()

        if self.__currentPage == self.__pages.get('logout'):
            self.loginView.printLogout()

        if self.__loginController.isUserLoggedIn():
            if self.__currentPage == self.__pages.get('emprestimos'):
                # self.emprestimosView...
                pass

            if self.__currentPage == self.__pages.get('fazer-emprestimo'):
                # self.emprestimosView...
                pass

            if self.__currentPage == self.__pages.get('livros'):
                # self.livrosView...
                pass

            if self.__currentPage == self.__pages.get('adicionar-livro'):
                # self.livrosView...
                pass

            if self.__currentPage == self.__pages.get('sobre'):
                # self.sobreView...
                pass

        generalPages = [
            {
                'id': 'login',
                'label': 'Realizar Login no sistema'
            },
            {
                'id': 'logout',
                'label': 'Deslogar do sistema'
            },
            {
                'id': 'sobre',
                'label': 'Sobre a Sistema'
            },
            {
                'id': 'emprestimos',
                'label': 'Ver Empréstimos'
            },
            {
                'id': 'livros',
                'label': 'Ver Livros'
            }
        ]

        loggedInPages = [
            {
                'id': 'fazer-emprestimo',
                'label': 'Fazer um empréstimo'
            },
            {
                'id': 'adicionar-livro',
                'label': 'Adicionar um Livro ao sistema'
            }
        ]

        allPages = generalPages

        if self.__loginController.isUserLoggedIn():
            allPages.extend(loggedInPages)

        self.__printGenerator.printOptions(
            'Escolha uma Página (digite o comando entre parênteses abaixo)', allPages)

        newPage = self.__printGenerator.inputData()

        self.__printGenerator.printSpace()

        self.changePage(newPage)
