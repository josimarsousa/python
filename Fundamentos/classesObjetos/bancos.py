class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
    
    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for conta in self.contas:
            conta.resumo()
            