import os


def createDataFile(filePath: str):
    basedir = os.path.dirname(filePath)

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    file = open(filePath, 'w')
    file.close()


class DatabaseController:
    __fileName: str
    __filePath: str

    def __init__(self, filePath: str):
        if not os.path.exists(filePath):
            createDataFile(filePath)

        head, tail = os.path.split(filePath)

        self.__fileName = tail
        self.__filePath = filePath

    def getEntries(self):
        try:
            entries = []

            with open(self.__filePath, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    entries.append(line.replace('\n', '').split(','))

            return entries
        except FileNotFoundError:
            print('Não foi possível encontrar a base de dados')
        finally:
            file.close()

    def saveEntry(self, data: str):
        try:
            entries = self.getEntries()

            with open(self.__filePath, 'w') as file:
                for entry in entries:
                    file.write(f'{",".join(entry)}\n')

                file.write(data)
                file.write('\n')
        except (OSError, IOError):
            print('Não foi possível salvar os dados')
        except FileNotFoundError:
            print('Não foi possível encontrar a base de dados')
        finally:
            file.close()

    def deleteEntry(self, key: str):
        try:
            entries = self.getEntries()

            with open(self.__filePath, 'w') as file:
                for entry in entries:
                    if key in entry:
                        file.write(f'{",".join(entry)}\n')
        except (OSError, IOError):
            print('Não foi possível excluir os dados')
        except FileNotFoundError:
            print('Não foi possível encontrar a base de dados')
        finally:
            file.close()

