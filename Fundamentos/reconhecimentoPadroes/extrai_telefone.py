import re

entrada = "Conpre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."

padrao = re.compile(r"\((\d{2,3})\)\s*(\d{4,5})-(\d{4})")

telefones = []
for match in padrao.finditer(entrada):
    ddd, parte1, parte2 = match.groups()
    formatado = f"({ddd}){parte1}-{parte2}"
    concatenado = f"{ddd}{parte1}{parte2}"
    telefones.append(
        {
            "inicio": match.start(),
            "fim": match.end() - 1,
            "formatado": formatado,
            "concatenado": concatenado,
        }
    )

if not telefones:
    print("Nenhum telefone encontrado.")
else:
    for tel in telefones:
        print(f"Telefone encontrado nas posições: {tel['inicio']} a {tel['fim']}")
        print(f"Formatado:   {tel['formatado']}")
        print(f"Concatenado: {tel['concatenado']}")
