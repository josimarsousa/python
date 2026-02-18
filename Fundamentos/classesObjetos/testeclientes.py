from clientes import Cliente
from contas import Conta

c1 = Cliente("Joao", "777-1234")
c2 = Cliente("Maria", "555-4321")

conta1 = Conta([c1], 1, 1000)
conta2 = Conta([c2], 2, 500)

conta1.saque(200)
conta2.deposito(500)
conta1.saque(150)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()


