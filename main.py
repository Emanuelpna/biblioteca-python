from controllers import DatabaseController


def databaseControllerExample():
    databaseController = DatabaseController.DatabaseController('./data/test.txt')

    data = databaseController.getEntries()

    print(data)

    preco = 520.99
    editora = 'Editora'
    nome = 'Nome do Livro'

    databaseController.saveEntry(f'{nome},{editora},{preco}')

    data = databaseController.getEntries()

    print(data)


if __name__ == '__main__':
    databaseControllerExample()
