from __future__ import annotations

from rich import print as pretty_print
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.tree import Tree

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infra.TableOptions import TableOptions


class RichClient:
    @staticmethod
    def inputData(message=''):
        return Prompt.ask(message)

    @staticmethod
    def printSpace():
        print('\n\n\n\n\n\n\n\n\n')

    @staticmethod
    def printHeader(title):
        pretty_print(Panel(title, expand=True))

    @staticmethod
    def printOptions(title, options):
        tree = Tree(title)

        for option in options:
            tree.add(f'[italic yellow]({option.get("id")})[/] {option.get("label")}')

        pretty_print(tree)

    @staticmethod
    def printError(error):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('')
        print(error)
        print('')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def printTable(tableOptions: 'TableOptions'):
        user_renderables = [Panel(f"[b]{user[0]}[/b]\n[yellow]{user[1]}", expand=True) for user in tableOptions.getData()]
        pretty_print(Columns(user_renderables))

        table = Table(title=tableOptions.getTitle())

        for column in tableOptions.getColumns():
            table.add_column(column, style="cyan", no_wrap=True)

        for row in tableOptions.getData():
            table.add_row(*row)

        pretty_print(table)
