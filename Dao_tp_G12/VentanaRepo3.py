import tkinter as tk
from tkinter import *

from tkinter.ttk import Treeview
from tkinter import messagebox

from Prestamo_dao import PrestamoDao


class InterfazRepo3:
    def __init__(self, root):
        self.root = root
        self.root.title("Reporte 3")
        self.root.geometry("750x350")
        self.resul = StringVar()
        
        # Campos de entrada
        #self.nombre = StringVar()
        self.entry_libro_titulo = tk.Entry(root)

        self.resultado_label = tk.Label(root, text="")
        
        # Etiquetas
        titulo = tk.Label(root, text="Reporte de socios que llevaron un titulo en partucular")
               
        titLibro = tk.Label(root, text="Ingrese titulo de libro a buscar ")
        resultado = tk.Label(root, textvariable=self.resul)
  

        # Botón para cerrar/buscar
        btn_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar)
        btn_buscar = tk.Button(root, text="Buscar", command=self.buscar)

        # Posicionamiento de elementos en la interfaz
        titulo.grid(row=0, padx=10, pady=5, sticky="w")
        
        titLibro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.resultado_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")
        
        self.entry_libro_titulo.grid(row=1, column=1, padx=10, pady=5)

        btn_buscar.grid(row=1, column=3, columnspan=2, pady=10)

        btn_cerrar.grid(row=3, column=0, columnspan=2, pady=10)

    def cerrar(self):
        self.root.destroy()

    def buscar(self):
        print("buscar")
        tit = self.entry_libro_titulo.get()
        print(f"entry_libro_titulo: {tit}")
        dao = PrestamoDao()
        rep = dao.obtener_socios_titulo(tit)
        resultado_text = ''
        if len(rep) == 0:
            self.resultado_label.config(text="Sin resultado")
        else:
            resultado_text += f"{len(rep)} resultados con: {tit} \n \n"
            for x in rep:
                resultado_text += f"- {x} \n"
        self.resultado_label.config(text=resultado_text)
        


