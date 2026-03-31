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
        self.l_temperatura.pack()
        self.temperatura = ttk.Entry(self.quadro)
        self.temperatura.pack()
        self.botao_cf = ttk.Button(self.quadro, text="Celsius para Fahrenheit")
        self.botao_cf.pack()
        self.botao_fc = ttk.Button(self.quadro, text="Fahrenheit para Celsius")
        self.botao_fc.pack()
        self.resultado = ttk.Label(self.quadro, text="Resultado:")
        self.resultado.pack()
        self.quadro.pack(expand=True)

    def celsius_para_fahrenheit(self):
        temperatura = float(self.temperatura.get())
        fahrenheit = 9/5.0 * temperatura + 32.0
        self.resultado["text"] = f"{fahrenheit:5.2f}  \u00B0F"

    def fahrenheit_para_celsius(self):
        temperatura = float(self.temperatura.get())
        celsius = (temperatura - 32.0) * 5/9.0
        self.resultado["text"] = f"{celsius:5.2f}  \u00B0C"

raiz = Aplicacao()
raiz.mainloop()