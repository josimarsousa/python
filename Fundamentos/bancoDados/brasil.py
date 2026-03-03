
import sqlite3

from contextlib import closing

dados = [
    ["São Paulo", 49024937, "Sudeste", "SP"],
    ["Rio de Janeiro", 16615526, "Sudeste", "RJ"],
    ["Minas Gerais", 20732600, "Sudeste", "MG"],
    ["Espírito Santo", 4018650, "Sudeste", "ES"],
    ["Bahia", 14016238, "Nordeste", "BA"],
    ["Paraná", 11444052, "Sul", "PR"],
    ["Goiás", 7056495, "Centro-Oeste", "GO"],
    ["Pernambuco", 9058962, "Nordeste", "PE"],
    ["Maranhão", 6775152, "Nordeste", "MA"],
    ["Amazonas", 3941613, "Norte", "AM"],
    ["Rondônia", 1771654, "Norte", "RO"],
    ["Tocantins", 1572866, "Norte", "TO"],
    ["Pará", 8602865, "Norte", "PA"],
    ["Amapá", 877016, "Norte", "AP"],
    ["Acre", 884431, "Norte", "AC"],
    ["Roraima", 63772, "Norte", "RR"],
    ["Sergipe", 2291077, "Nordeste", "SE"],
    ["Alagoas", 3337599, "Nordeste", "AL"],
    ["Piauí", 3273227, "Nordeste", "PI"],
    ["Distrito Federal", 3015268, "Centro-Oeste", "DF"],
    ["Mato Grosso", 3484466, "Centro-Oeste", "MT"],
    ["Mato Grosso do Sul", 2778986, "Centro-Oeste", "MS"],
    ["Paraíba", 4059905, "Nordeste", "PB"],
    ["Ceará", 8835051, "Nordeste", "CE"],
    ["Rio Grande do Norte", 3483348, "Nordeste", "RN"],
    ["Rio Grande do Sul", 11247972, "Sul", "RS"],
    ["Santa Catarina", 7164788, "Sul", "SC"]
]

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute("DROP TABLE IF EXISTS estados")
        cursor.execute("""CREATE TABLE IF NOT EXISTS estados (
                            id integer primary key autoincrement, 
                            nome text, 
                            populacao integer,
                            regiao text,
                            sigla text
                       )""")
        cursor.executemany("INSERT INTO estados (nome, populacao, regiao, sigla) VALUES (?, ?, ?, ?)", dados)    
    conexao.commit()
conexao.close()