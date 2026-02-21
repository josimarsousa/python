
import sqlite3

from contextlib import closing

dados = [["Sao Paulo", 49024937], ["Rio de Janeiro", 16615526], ["Minas Gerais", 20732600],
    ["Bahia", 14016238], ["Paraná", 11444052], ["Goiás", 7056495], ["Pernambuco", 9058962],
    ["Maranhão", 6775152], ["Amazonas", 3941613], ["Rondônia", 1771654], ["Tocantins", 1572866],
    ["Pará", 8602865], ["Amapá", 877016], ["Acre", 884431], ["Roraima", 63772], ["Sergipe", 2291077],
    ["Alagoas", 3337599], ["Piauí", 3273227], ["Distrito Federal", 3015268], ["Mato Grosso", 3484466],
    ["Alagoas", 3337599], ["Piauí", 3273227], ["Distrito Federal", 3015268], ["Mato Grosso", 3484466],
    ["Mato Grosso do Sul", 2778986], ["Paraíba", 4059905], ["Ceará", 8835051 ]]

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS estados (
                            id integer primary key autoincrement, 
                            nome text, 
                            populacao integer
                       )""")
        cursor.executemany("INSERT INTO estados (nome, populacao) VALUES (?, ?)", dados)    
    conexao.commit()
