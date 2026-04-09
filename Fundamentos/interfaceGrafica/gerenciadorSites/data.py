import tkinter as tk
import tkinter.ttk as ttk

class Data(ttk.Frame):
    def __init__(self, parent, min_ano=00, max_ano=40):
        super().__init__(parent)
        self.min_ano = min_ano
        self.max_ano = max_ano
        self.dia = tk.StringVar()
        self.mes = tk.StringVar()
        self.ano = tk.StringVar()
        self.cria_controles()

    def set(self, data):
        dia, mes, ano = data.split("-")
        self.dia.set(dia)
        self.mes.set(mes)
        self.ano.set(ano)

    
