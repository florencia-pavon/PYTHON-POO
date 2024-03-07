import tkinter as tk
from Prestamo_dao import PrestamoDao


class InterfazRepo5:
    def __init__(self, root):
        self.root = root
        self.root.title("Listado de Préstamos Demorados")
        self.root.geometry("400x300")

        prestamo_dao = PrestamoDao()
        prestamos_demorados = prestamo_dao.prestamos_demorados()

        if len(prestamos_demorados) > 0:
            for index, prestamo in enumerate(prestamos_demorados):
                label_info = tk.Label(root, text=f"{index + 1}. {prestamo}")
                label_info.grid(row=index, column=0, padx=10, pady=5, sticky="w")
        else:
            label_info_empty = tk.Label(root, text='No existen prestamos demorados a la fecha de Hoy.')
            label_info_empty.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        btn_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar)
        btn_cerrar.grid(row=len(prestamos_demorados) + 1, column=0, pady=10)

    def cerrar(self):
        self.root.destroy()

