nome = "fulano"

print(nome)
#fulano

len(nome)
6

len("O rato roeu a roupa ")


#acessando um indice em uma palavra

a = "ABCDEF"

a[0]
#A

a[1]
#B

a[3]
#D

a[4]
##E

a[5]
#F

#concatenaçao
a + "G"
'ABCDEFG'

a + "H" * 3
'ABCDEFGHHH'


"X" + "-" * 10 + "Y"
'X----------Y'

nome = "Tiao"
idade = 20
print("Joao tem %d anos" % idade )


#outro exemplo
print("%s tem %d anos e apenas R$%5.2f no bolso" % ("Joao", 22, 51.34))

#forma mais moderna de concatenacao com o metodo format

nome = "joao"
idade  = 22
dinheiro = 52.00

print("{} tem {} anos e {} no bolso. ".format(nome, idade, dinheiro))
#exemplo com mascaras
print("{:12} tem {:3} anos e R${:5.3f} no bolso".format(nome, idade, dinheiro))
#outro exemplo com mascaras
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso".format(nome, idade, dinheiro))

#format com posicao do parametros
print("{0} {1} {2}".format("a", "b", "c"))
print("{1} {0} {2}".format("a", "b", "c"))
print("{2} {1} {0} {0}".format("a", "b", "c"))

#format com f-string
print(f"{nome} tem {idade} anos e {dinheiro} no bolso.")

#fatiamento de strings
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[0:25])




