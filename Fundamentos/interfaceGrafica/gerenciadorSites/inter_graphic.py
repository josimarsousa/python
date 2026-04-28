import tkinter as tk

def acao_exemplo():
    print("Botão clicado!")

# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Meu App com Menu")
janela.geometry("400x300")

# 2. Criação da Barra de Menu (o container principal)
barra_menu = tk.Menu(janela)

# 3. Criação de um Menu Individual (ex: Arquivo)
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Novo", command=acao_exemplo)
menu_arquivo.add_command(label="Salvar", command=acao_exemplo)
menu_arquivo.add_separator() # Linha divisória
menu_arquivo.add_command(label="Sair", command=janela.quit)

# 4. Adicionando o menu "Arquivo" à Barra de Menu principal
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# 5. Configurando a janela para usar essa barra
janela.config(menu=barra_menu)

janela.mainloop()

