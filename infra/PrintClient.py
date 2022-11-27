from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infra.TableOptions import TableOptions


class PrintClient:
    @staticmethod
    def inputData(message=''):
        return input(f'{message}\n>')

    @staticmethod
    def printSpace():
        print('\n\n\n\n\n\n\n\n\n')

    @staticmethod
    def printHeader(title):
        print("**************************")

        print(title)

        print("**************************")

    @staticmethod
    def printOptions(title, options):
        print('==========================')
        print('')

        print(title)

        for option in options:
            print(f'   - ({option.get("id")}) {option.get("label")}')

        print('')
        print('==========================')

    @staticmethod
    def printSelect(title, options):
        print('==========================')
        print('')

        print(title)

        index = 0
        for option in options:
            print(f'   - ({index}) {option}')
            index += 1

        choosedIndex = int(PrintClient.inputData('Escolha o número de uma das Opções acima'))

        print('==========================')

        return options[choosedIndex]

    @staticmethod
    def printError(error):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('')
        print(error)
        print('')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def printTable(tableOptions: 'TableOptions'):
        print(tableOptions.getTitle())
        print('')

        print(", ".join(tableOptions.getColumns()))
        print('---------------')
        for dataRow in tableOptions.getColumns():
            print(", ".join(dataRow.toList()))

        print('')
