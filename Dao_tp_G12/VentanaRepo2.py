import tkinter as tk

from Libro_dao import LibroDao


class InterfazRepo2:
    def __init__(self, root):
        self.root = root
        self.root.title("Reporte Costo Reposicion")
        self.root.geometry("350x150")
        
        dao=LibroDao()
        rep=dao.costo_libros_extraviados()

        # Etiquetas
        titulo = tk.Label(root, text="Reporte Costo Reposicion de Libros extraviados")
               
        costo = tk.Label(root, text="Costo Total:  $ "+str(rep["total"]))
  

        # Botón para cerrar/salir
        btn_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar)

        # Posicionamiento de elementos en la interfaz
        titulo.grid(row=0, padx=10, pady=5, sticky="w")
        
        costo.grid(row=1, column=0, padx=10, pady=5, sticky="w")

 
        btn_cerrar.grid(row=3, column=0, columnspan=2, pady=10)
        
        

    def cerrar(self):
        self.root.destroy()
