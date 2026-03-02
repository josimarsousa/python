
import sqlite3

from contextlib import closing

dados = [
    ["São Paulo", 49024937, "Sudeste"],
    ["Rio de Janeiro", 16615526, "Sudeste"],
    ["Minas Gerais", 20732600, "Sudeste"],
    ["Espírito Santo", 4018650, "Sudeste"],
    ["Bahia", 14016238, "Nordeste"],
    ["Paraná", 11444052, "Sul"],
    ["Goiás", 7056495, "Centro-Oeste"],
    ["Pernambuco", 9058962, "Nordeste"],
    ["Maranhão", 6775152, "Nordeste"],
    ["Amazonas", 3941613, "Norte"],
    ["Rondônia", 1771654, "Norte"],
    ["Tocantins", 1572866, "Norte"],
    ["Pará", 8602865, "Norte"],
    ["Amapá", 877016, "Norte"],
    ["Acre", 884431, "Norte"],
    ["Roraima", 63772, "Norte"],
    ["Sergipe", 2291077, "Nordeste"],
    ["Alagoas", 3337599, "Nordeste"],
    ["Piauí", 3273227, "Nordeste"],
    ["Distrito Federal", 3015268, "Centro-Oeste"],
    ["Mato Grosso", 3484466, "Centro-Oeste"],
    ["Mato Grosso do Sul", 2778986, "Centro-Oeste"],
    ["Paraíba", 4059905, "Nordeste"],
    ["Ceará", 8835051, "Nordeste"],
    ["Rio Grande do Norte", 3483348, "Nordeste"],
    ["Rio Grande do Sul", 11247972, "Sul"],
    ["Santa Catarina", 7164788, "Sul"]
]

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute("DROP TABLE IF EXISTS estados")
        cursor.execute("""CREATE TABLE IF NOT EXISTS estados (
                            id integer primary key autoincrement, 
                            nome text, 
                            populacao integer,
                            regiao text
                       )""")
        cursor.executemany("INSERT INTO estados (nome, populacao, regiao) VALUES (?, ?, ?)", dados)    
    conexao.commit()
conexao.close()