import tkinter as tk
from tkinter import ttk

class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Conversos")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_temperatura = ttk.Label(self.quadro, text="Temperatura:")
               
