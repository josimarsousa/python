import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    conexao.execute("""ALTER TABLE estados ADD sigla text""")

    conexao.execute("""ALTER TABLE estados ADD regiao text""")

conexao.commit()
conexao.close()