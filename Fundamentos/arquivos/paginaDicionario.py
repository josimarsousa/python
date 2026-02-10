filmes = {
    "drama": ["Cidadao kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "Ameriacan Pie", "Dr. dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de matar"],
    "guerra": ["Rambo", "Platton", "Tora!Tora!Tora!"]
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Filmes</title>
</head>
<body>
""")
    for c, v in filmes.items():
        pagina.write(f"<h2>{c}</h2>\n")
        for e in v:
            pagina.write(f"<li>{e}</li>\n")
    pagina.write("""
                </body>
                </html>
                """)