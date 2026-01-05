#if // lê dois valores e mostra qual o maior
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print("O primeiro numero é maior que o segundo")
if num2 > num1:
    print("O segundo numero é maior que o primeiro")

#controle de velocidade de um carro
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("A velociadade foi ultrapassada do limite de 80km/h")
if velocidade <= 80: 
    print("A velocidade está dentro do limite permitido de 80km/h")