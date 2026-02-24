import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    conexao.execute("""ALTER TABLE estados
                    add sigla text""")

    conexao.execute("""ALTER TABLE estados
                    add regiao text""")

conexao.commit()
conexao.close()