from locale import AM_STR
import sqlite3

dados = [["SP", "SE", "SAO PAULO"], ["RJ", "SE", "RIO DE JANEIRO"], ["MG", "SE", "MINAS GERAIS"],
["ES", "SE", "ESPIRITO SANTO"], ["BA", "SE", "BAHIA"], ["PE", "SE", "PERNAMBUCO"], ["AL", "SE", "ALAGOAS"],
["SE", "SE", "SERGIPE"], ["PI", "SE", "PIAUI"], ["CE", "SE", "CEARA"], ["RN", "SE", "RIO GRANDE DO NORTE"],
["PB", "SE", "PARAIBU"], ["MA", "SE", "MARANHAO"],["TO", "SE", "TOCANTINS"], ["AC", "N", "ACRE"], ["RO", "N", "RONDONIA"],
["AM", "N", "AMAZONAS"], ["PA", "N", "PARA"], ["AP", "N", "AMAPA"], ["RR", "N", "RORAIMA"], ["MA", "N", "MARANHAO"],
["DF", "N", "DISTRITO FEDERAL"]]

with sqlite3.connect("brasil.db") as conexao:
    conexao.executemany("""update estados
                        set sigla = ?,
                        regiao = ?
                        WHERE nome = ?""", dados)
