import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM contatos")
resultado = cursor.fetchone()
print("Contatos da agenda")
print(f"Codigo: {resultado[0]}\nNome: {resultado[1]}\nTelefone: {resultado[2]}")
cursor.close()
conexao.close()