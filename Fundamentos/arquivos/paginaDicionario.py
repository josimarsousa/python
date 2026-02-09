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
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Filmes</title>
                </head>
                <body>
                <h1>Filmes por Categoria</h1>
                """)
    for c, v in filmes.items():
        pagina.write(f"<h2>{c}</h2>\n")
        pagina.write("<ul>\n")
        for e in filmes.items():
            pagina.write(f"<li>{c}</li>\n")
            for e in v:
                pagina.write("</ul>\n")
    pagina.write("""
                </body>
                </html>
                """)