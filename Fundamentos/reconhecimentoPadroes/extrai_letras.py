entrada = "ABC431DEF9014C31203FXEW9"
saida = []
letras = []

for caractere in entrada:
    if "A" <= caractere <= "Z":
        if not letras:
            saida.append(letras)
        letras += caractere
    elif letras:
        letras = []
for encontrado in saida:
    print("".join(encontrado))