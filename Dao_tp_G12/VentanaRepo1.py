import tkinter as tk

from Libro_dao import LibroDao


class InterfazRepo1:
    def __init__(self, root):
        self.root = root
        self.root.title("Reporte 1")
        self.root.geometry("250x200")
        
        dao=LibroDao()
        rep=dao.libros_por_estado()

        # Etiquetas
        titulo = tk.Label(root, text="Reporte General de Libros:")
        
        disponible = tk.Label(root, text="Cantidad de Libros Disponibles:")
        prestado = tk.Label(root, text="Cantidad de Libros Prestados")
        extraviado = tk.Label(root, text="Cantidad de Libros Extraviados")
  
        disp = tk.Label(root, text=rep["disponible"])
        pres = tk.Label(root, text=rep["prestado"])
        extr = tk.Label(root, text=rep["extraviado"])

        # Botón para cerrar/salir
        btn_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar)

        # Posicionamiento de elementos en la interfaz
        titulo.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        disponible.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        prestado.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        extraviado.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        disp.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        pres.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        extr.grid(row=3, column=1, padx=10, pady=5, sticky="w")
 
        btn_cerrar.grid(row=4, column=0, columnspan=2, pady=10)
        
        

    def cerrar(self):
        self.root.destroy()
