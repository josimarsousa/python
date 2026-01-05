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