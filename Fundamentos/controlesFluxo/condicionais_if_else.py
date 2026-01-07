#programa para ver se carro é novo ou velho
ano_do_carro = int(input("Digite o ano do carro: "))
if ano_do_carro > 2020:
    print("O carro é novo")
else:
    print("O carro é velho")


#verificando qual numero é maior
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero:"))

if num1 > num2:
    print(f"O numero {num1} é maior que o numero {num2}")
else:
    print(f"O numero {num2} é maior que o numero {num1}")
if num1 == num2:
    print(f"Os dois numeros são iguais")

#programa para verificar preço de passagem por km percorrido
nome_passageiro = input("Digite o nome do passageiro: ")
origem = input("Digite a origem do passageiro: ")
destino = input("Digite o destino do passageiro: ")
km = float(input("Digite a quantidade de km percorridos: "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print(f"O passageiro {nome_passageiro} de {origem} para {destino} percorreu {km:.2f} km e pagará R${preco:.2f}")

#if_else aninhados - Conta de telefone dom tres faixas de precos
minutos = int(input("Digite a quantidade de minutos utilizados: "))

if minutos <= 200:
    preco = minutos * 0.20
else:
    if minutos <= 400:
        preco = minutos * 0.15
    else:
        preco = minutos * 0.10

print(f"Você vai pagar este mês: R${preco:.2f}")

#elif - soluçao para ifs aninhados
#categoria x preco usando elif
categoria  = input("Digite a categoria do produto: ")
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3: 
    preco = 23
elif categoria == 4:
    preco = 26
else: 
    print("Categoria inválida, digite um valor entre 1 e 4!")
    preco = 0
print(f"O preço do produto é: R${preco:.2f}")
