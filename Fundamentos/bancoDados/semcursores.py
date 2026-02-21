import sqlite3

print("\nDados do banco de dados agenda\n")
with sqlite3.connect("agenda.db") as conexao:
    for regitstro in conexao.execute("SELECT * FROM contatos"):
        print(f"Nome: {regitstro[1]}Telefone: {regitstro[2]}")
    print("\nFim da consulta\n")