#lendo um arquivo em json com python

import json
from pathlib import Path

with Path("dados.json").open() as arquivo:
    dados = json.load(arquivo)
print(dados["nome"])
print(dados["valores"])

