from Router import Router

from infra.PrintClient import PrintClient


if __name__ == '__main__':
    print(r"""
        ═╬═════════════════════════════════════════════════════════════════════╬═
         ║   ____               __  __      __                      __         ║
         ║  /\  _`\            /\ \/\ \  __/\ \                    /\ \        ║
         ║  \ \ \L\ \     __   \_\ \ \ \/\ \ \ \    ___     ___    \_\ \       ║
         ║   \ \ ,  /   /'__`\ /'_` \ \ \ \ \ \ \  / __`\  / __`\  /'_` \      ║
         ║    \ \ \\ \ /\  __//\ \L\ \ \ \_/ \_\ \/\ \L\ \/\ \L\ \/\ \L\ \     ║
         ║     \ \_\ \_\ \____\ \___,_\ `\___x___/\ \____/\ \____/\ \___,_\    ║
         ║      \/_/\/ /\/____/\/__,_ /'\/__//__/  \/___/  \/___/  \/__,_ /    ║
         ║                                                                     ║
        ═╬═══════════════════════ Biblioteca Digital ══════════════════════════╬═
    """)

    printGenerator = None

    try:
        from infra.RichClient import RichClient

        printGenerator = RichClient()
    except ModuleNotFoundError:
        printGenerator = PrintClient()

    routerController = Router(printGenerator)

    routerController.changePage('index')
