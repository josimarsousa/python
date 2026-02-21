import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY, 
        nome TEXT, 
        telefone TEXT)
    ''')   

cursor.execute('''
        INSERT INTO contatos (nome, telefone) VALUES (?, ?)
        ''', ("Maria", "9876-5678"))

conexao.commit()
cursor.close()
conexao.close()
