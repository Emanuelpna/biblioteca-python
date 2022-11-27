from pick import pick
from rich import print as pretty_print
from rich.columns import Columns
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from rich.traceback import install as tracebackInstall

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infra.TableOptions import TableOptions


class RichClient:
    def __init__(self):
        tracebackInstall()

    @staticmethod
    def inputData(message=''):
        return Prompt.ask(message)

    @staticmethod
    def printSpace():
        print('\n\n\n\n\n\n\n\n\n')

    @staticmethod
    def printText(text):
        pretty_print(text)

    @staticmethod
    def printHeader(title):
        pretty_print(Panel(title, expand=True))

    @staticmethod
    def printOptions(title, options):
        tree = Tree(title)

        for option in options:
            tree.add(
                f'[italic yellow]({option.get("id")})[/] {option.get("label")}')

        pretty_print(tree)

    @staticmethod
    def printSelect(title, options):
        option, index = pick(options, title)

        return option

    @staticmethod
    def printCards(title, cardsData):
        pretty_print(Panel(title, title_align='center'))

        user_renderables = [
            Panel(
                f"[b]{card.get('name')}[/b]\n[yellow]{card.get('ocupation')}", expand=True
            ) for card in cardsData
        ]

        pretty_print(Columns(user_renderables))

    @staticmethod
    def printError(error):
        pretty_print(Panel.fit(error, title="Erro!"))

    @staticmethod
    def printTable(tableOptions: 'TableOptions'):
        table = Table(title=tableOptions.getTitle())

        for column in tableOptions.getColumns():
            table.add_column(column, style="cyan", no_wrap=True)

        for row in tableOptions.getData():
            table.add_row(*row.toList())

        pretty_print(table)
