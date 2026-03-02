import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    # A coluna regiao já foi criada no script brasil.py
    # conexao.execute("""ALTER TABLE estados ADD regiao text""")
    
    # Adicionamos apenas a coluna sigla
    conexao.execute("""ALTER TABLE estados ADD sigla text""")

conexao.commit()
conexao.close()