class PrintGenerator:
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
            print(f'   - [{option.get("id")}] {option.get("label")}')

        print('')
        print('==========================')

    @staticmethod
    def printError(error):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('')
        print(error)
        print('')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def printTable():
        print(rf"""
            +----------------------------------+---------+------------------------+----------------+
            |               Col1               |  Col2   |          Col3          | Numeric Column |
            +----------------------------------+---------+------------------------+----------------+
            | Value 1                          | Value 2 | 123                    |           10.0 |
            | Separate                         | cols    | with a tab or 4 spaces |       -2,027.1 |
            | This is a row with only one cell |         |                        |                |
            +----------------------------------+---------+------------------------+----------------+
        """)
