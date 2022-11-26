from typing import List


class TableOptions:
    __title: str
    __data: list
    __columns: List[str]

    def __init__(self, title: str, tableColumns: List[str], tableData: list):
        self.__title = title
        self.__data = tableData
        self.__columns = tableColumns

    def getTitle(self):
        return self.__title

    def getData(self):
        return self.__data

    def getColumns(self):
        return self.__columns
