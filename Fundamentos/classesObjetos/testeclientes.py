from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco

c1 = Cliente("Joao", "777-1234")
c2 = Cliente("Maria", "555-4321")
c3 = Cliente("José", "333-7777")

conta1 = Conta([c1], 1, 1000)
conta2 = ContaEspecial([c2], 2, 500, 1000)
conta3 = Conta([c3], 3, 100)

tatu = Banco("Tatu")
tatu.abre_conta(conta1)
tatu.abre_conta(conta2)
tatu.abre_conta(conta3)

conta1.saque(50)
conta2.deposito(300)
conta3.deposito(1000)
conta1.saque(190)
conta3.saque(500)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
conta3.extrato()

tatu.lista_contas()



