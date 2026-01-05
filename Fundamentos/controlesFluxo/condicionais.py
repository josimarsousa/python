#if // lê dois valores e mostra qual o maior
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print("O primeiro numero é maior que o segundo")
if num2 > num1:
    print("O segundo numero é maior que o primeiro")
if num1 == num2:
    print("Os dois numeros são iguais")

#controle de velocidade de um carro
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("A velociadade foi ultrapassada do limite de 80km/h")
if velocidade <= 80: 
    print("A velocidade está dentro do limite permitido de 80km/h")

#calculo de imposto de renda
salario = float(input("Digite o salario: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000: 
    imposto = imposto + ((base - 1000) * 0.20)
if base < 1000:
    print("Como seu salario esta abaixo de R$1000,00 você não pagará imposto!")

print(f"SALÁRIO: R${salario:.2f} IMPOSTO A PAGAR: R${imposto:.2f}")

#programa que lê tres numeros e mostra o maior e o menor
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
maior = 0
menor = 0

if num1 > num2 and num1 > num3 and num2 > num3: 
    maior = num1
    menor = num3
if num2 > num1 and num2 > num3 and num1 > num3:
    maior = num2
    menor = num3
if num3 > num2 and num3 > num1 and num2 > num1:
    maior = num3
    menor = num1


print(f"O maior numero é: {maior:.2f}") 
print(f"O menor numero é: {menor:.2f}")

