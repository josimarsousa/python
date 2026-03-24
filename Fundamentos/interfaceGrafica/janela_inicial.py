import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Janela Inicial")
raiz.geometry("250x50")
quadro = ttk.Frame(raiz)
texto = ttk.Label(quadro, text="Olá Gui - Grafic user interface")
texto.pack()

botao = ttk.Button(quadro, text="Sai", command=raiz.destroy)
botao.pack()
quadro.pack(expand=True)
raiz.mainloop()
