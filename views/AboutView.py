class AboutView:
    def __init__(self, printGenerator):
        self.__printGenerator = printGenerator

    def printAbout(self):
        self.__printGenerator.printText('''
A empresa RedWood foi criada por alunos da própria instituição como uma empresa júnior.
A missão da ReedWood é inovar a gestão da biblioteca, possibilitando, tanto aos alunos, quanto aos bibliotecários, 
uma maior eficiência e praticidade no que diz respeito ao acervo das Faculdades.
        ''')

        self.__printGenerator.printCards('Equipe', [
            {
                'name': 'Emanuel Andrade',
                'ocupation': 'Dev Frontend'
            },
            {
                'name': 'Mateus Góes',
                'ocupation': 'Dev Backend'
            },
            {
                'name': 'Luis Gustavo Theml',
                'ocupation': 'Analista de Sistema'
            },
            {
                'name': 'Bernardo Menon',
                'ocupation': 'Dev Backend'
            },
            {
                'name': 'Felipe Augusto',
                'ocupation': 'QA Tester'
            }
        ])
