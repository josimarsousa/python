#soma de 2 valores
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite um valor para o numero 2: "))
soma = float(num1+num2)
print(f"A soma dos valores é: {soma:.2f}")

#converter valor em metros para milimetros
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros} metros é igual a {milimetros:.2f} milimetros")

#ler a quantidade de dias em segundos, calcule o total em segundos    
dias = int(input("Digite a quantidade de dias: "))
total_segundos = dias * 24 * 60 * 60
print(f"{dias} dias em segundos é igual a {total_segundos} segundos")

#calcular um aumento de salario e mostrar a porcentagem do aumento  
salario = float(input("Digite o salario atual: "))
aumento = float(input("Digite a porcentagem de aumento: "))
print(f"O salario atual é de {salario:.2f}")
print(f"A porcentagem do aumento é de {aumento:.0f}%")
novo_salario = salario + salario * aumento / 100
print(f"O aumento de {aumento:.0f}% no salario de {salario:.2f} é igual a {novo_salario:.2f}")

#desconto na compra de uma mercadoria e valor a pagar
preco = float(input("Digite o preco da mercadoria: "))
desconto = float(input("Digite a porcentagem de desconto: "))
print(f"O preco da mercadoria é de {preco:.2f}")
print(f"O desconto é de {desconto:.0f}%")
preco_com_desconto = preco - preco * desconto / 100
print(f"O preco com desconto é de {preco_com_desconto:.2f}")