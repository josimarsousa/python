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






