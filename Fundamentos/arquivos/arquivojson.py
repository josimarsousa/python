#lendo um arquivo em json com python

import json
from pathlib import Path

with Path("dados.json").open() as arquivo:
    dados = json.load(arquivo)
print(dados["nome"])
print(dados["valores"])

#lendo uma lista
with Path("lista.json").open(encoding="utf-8") as arquivo:
    turma = json.load(arquivo)
for aluno in turma:
    print("Nome: ", aluno["nome"])
    print("Notas: ", aluno["notas"])
    print("Média: ", sum(aluno["notas"]) / len(aluno["notas"]))
    print("-----------------")

#criando uma tabela de preços em formato json
tabela_de_precos = {}

print("Criador da tabela de preços")
print("Digite um nome de produto em branco para terminar")
while produto := input("Nome do produto: "):
    preco = input("Preço: ")
    tabela_de_precos[produto] = float(preco)

with Path("precos.json").open("w", encoding="utf-8") as arquivo:
    json.dump(tabela_de_precos, arquivo, indent=2, ensure_ascii=False)