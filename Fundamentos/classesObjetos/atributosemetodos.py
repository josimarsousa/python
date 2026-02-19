class Contador:

    instancias = 0


    def __init__(self):
        self.contador = 0
        Contador.instancias += 1

    def incrementa(self):
        self.contador += 1
