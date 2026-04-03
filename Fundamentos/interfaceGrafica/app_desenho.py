import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quadro = ttk.Frame(self)
        self.cria_barra()
        self.cria_area_de_desenho()
        self.title("Desenho")
        self.geometry("800x600")
        self.quadro.pack(expand=True, fill="both")
        self.cruz = []
        self.cruz.append(self.canvas.create_line((0,0,0,0), dash=[2,4]))
        self.cruz.append(self.canvas.create_line((0,0,0,0), dash=[2,4]))
        self.cor_de_frente = "black"
        self.estado = 0
        self.xi = None
        self.yi = None
        self.curr_id = 0
        self.ferramenta = self.canvas.create_line

    def cria_area_de_desenho(self):
        self.trabalho = ttk.Frame(self.quadro, height=600)
        self.trabalho.grid(column=1, row=0, sticky=tk.NSEW)
        self.quadro.grid_columnconfigure(1, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.trabalho, background="#FFFFFF")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.coordenadas = tk.Label(self.trabalho, text="Mova o mouse")
        self.coordenadas.pack(ipadx=10, ipady=10)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)

        
    def cria_barra(self):
        self.barra = ttk.Frame(self.quadro, width=100, height=600)
        self.barra.grid(column=0, row=0, sticky=tk.NS)

    def mouse_move(self, event):
        self.coordenadas["text"] = f"Mouse x={event.x} y={event.y}"
        self.canvas.coords(self.cruz[0], event.x, 0, event.x, self.canvas.winfo_height())
        self.canvas.coords(self.cruz[1], 0, event.y, self.canvas.winfo_width(), event.y)
        if self.estado ==1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_click(self, event):
        if self.estado == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.ferramenta((self.xi, self.yi, event.x, event.y),
                fill=self.cor_de_frente, tags=["desenho"])
            self.estado = 1

    def mouse_release(self, event):
        if self.estado == 1:
            self.estado = 0

App().mainloop()

        