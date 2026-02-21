#ler todos os dados de contatos
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("SELECT * FROM contatos")
        for linha in cursor.fetchall():
            print(f"ID: {linha[0]}\nNome: {linha[1]}\nTelefone: {linha[2]}\n")