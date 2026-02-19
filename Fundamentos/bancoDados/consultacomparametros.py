#consulta utilizando parametros
import sqlite3
from contextlib import closing
nome = input("Digite o nome a pesquisar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("SELECT * FROM contatos WHERE nome = ?", (nome,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Contato não encontrado.")
                break
            print(f"Nome: {resultado[1]}\nTelefone: {resultado[2]}")
            x += 1