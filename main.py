from Router import Router

from infra.PrintClient import PrintClient


if __name__ == '__main__':
    print(r"""
        ═╬══════════════════════════════════════════════════════════════════════════════════════════╬═
         ║      ____          __       ___                  __                                      ║
         ║     /\  _`\    __ /\ \     /\_ \    __          /\ \__                                   ║
         ║     \ \ \L\ \ /\_\\ \ \____\//\ \  /\_\     ___ \ \ ,_\     __     ___      __           ║
         ║      \ \  _ <'\/\ \\ \ '__`\ \ \ \ \/\ \   / __`\\ \ \/   /'__`\  /'___\  /'__`\         ║
         ║       \ \ \L\ \\ \ \\ \ \L\ \ \_\ \_\ \ \ /\ \L\ \\ \ \_ /\  __/ /\ \__/ /\ \L\.\_       ║
         ║        \ \____/ \ \_\\ \_,__/ /\____\\ \_\\ \____/ \ \__\\ \____\\ \____\\ \__/.\_\      ║
         ║         \/___/   \/_/ \/___/  \/____/ \/_/ \/___/   \/__/ \/____/ \/____/ \/__/\/_/      ║
        ═╬══════════════════════════════════════════════════════════════════════════════════════════╬═
    """)

    printGenerator = None

    try:
        from infra.RichClient import RichClient

        printGenerator = RichClient()
    except ModuleNotFoundError:
        printGenerator = PrintClient()

    routerController = Router(printGenerator)

    routerController.changePage('index')
