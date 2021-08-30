import tkinter as tk
from tkinter import messagebox as msg

class Mensagem:
    def __init__(self, tipo, titulo, conteudo):
        window = tk.Tk()
        window.withdraw()
        self.mostrar_mensagem(tipo, titulo, conteudo)
        window.mainloop()

    def mostrar_mensagem(self, tipo, titulo, conteudo):
        if tipo == "info":
            msg.showinfo(titulo, conteudo)

        elif tipo == "warning":
            msg.showwarning(titulo, conteudo)

        elif tipo == "error":
            msg.showerror(titulo, conteudo)