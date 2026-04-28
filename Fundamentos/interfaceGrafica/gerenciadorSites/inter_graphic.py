import tkinter as tk

def acao_sair():
    print("Saindo...")
    root.quit()

root = tk.Tk()
root.title("Exemplo de menu")
root.geometry("300x200")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Novo")
filemenu.add_command(label="Abrir")
filemenu.add_separator()
filemenu.add_command(label="Sair", command=acao_sair)

menubar.add_cascade(label="Arquivo", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
