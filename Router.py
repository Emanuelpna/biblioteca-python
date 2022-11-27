from controllers.BookController import BookController
from controllers.LoanController import LoanController
from controllers.LoginController import LoginController
from views.LoanView import LoanView
from views.LoginView import LoginView
from views.BookView import BookView


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
        self.__loanController = LoanController()
        self.__bookController = BookController()

        self.__loginView = LoginView(self.__loginController, printGenerator)
        self.__bookView = BookView(self.__bookController, printGenerator)
        self.__loanView = LoanView(
            self.__loanController, self.__bookController, self.__loginController, printGenerator)

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
        if self.__currentPage == self.__pages.get('login'):
            self.__loginView.printLogin()

        if self.__currentPage == self.__pages.get('logout'):
            self.__loginView.printLogout()

        if self.__loginController.isUserLoggedIn():
            if self.__currentPage == self.__pages.get('emprestimos'):
                self.__loanView.printLoans()

            if self.__currentPage == self.__pages.get('fazer-emprestimo'):
                self.__loanView.printNewLoan()

            if self.__currentPage == self.__pages.get('livros'):
                self.__bookView.printBooks()

            if self.__currentPage == self.__pages.get('adicionar-livro'):
                self.__bookView.printCreateBook()

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
            }
        ]

        loggedInPages = [
            {
                'id': 'livros',
                'label': 'Ver Livros'
            },
            {
                'id': 'adicionar-livro',
                'label': 'Adicionar um Livro ao sistema'
            },
            {
                'id': 'emprestimos',
                'label': 'Ver Empréstimos'
            },
            {
                'id': 'fazer-emprestimo',
                'label': 'Fazer um empréstimo'
            },
            {
                'id': 'sobre',
                'label': 'Sobre a Sistema'
            },
        ]

        allPages = generalPages

        if self.__loginController.isUserLoggedIn():
            allPages.extend(loggedInPages)

        self.__printGenerator.printOptions(
            'Escolha uma Página (digite o comando entre parênteses abaixo)', allPages)

        newPage = self.__printGenerator.inputData()

        self.__printGenerator.printSpace()

        self.changePage(newPage)
