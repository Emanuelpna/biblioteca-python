import os

# emprestimos.txt: arquivo que contêm as informações dos empréstimos realizados. 
# (na sequência: código do empréstimo, código do cliente, código do livro e data do empréstimo). 
# Vale lembrar que podem existir mais de uma e no máximo 3 (três) linhas de registro para um mesmo código de empréstimo.


class loan():
    def __init__(self, codClient, codBook, dtLoan):
        listloan = list

        #Sempre ao iniciar, ler o arquivo txt e alimentar a lista criada acima.


        self.codloan = max(listloan) + 1 #Sempre ao instanciar um empréstimo, definir o código como sendo o maior número da lista + 1.
        listloan.append(self.codloan) #Sempre ao instanciar um empréstimo, Acrescentar a lista de empréstimos.
        
        self.codClient = int(codClient)
        self.codBook = int(codBook)
        self.dtLoan = dtLoan

    def removeLoan(self, cod):       
        listloan.remove(cod) #Remover o empréstimo da lista.
        #Remover o empréstimo do arquivo txt.

    def getCodLoan(self):
        return self.codloan

    def getCodClient(self):
        return self.codClient