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