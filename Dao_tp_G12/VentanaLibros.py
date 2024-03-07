import tkinter as tk
from tkinter import messagebox
from Libro_dao import LibroDao
from Libro import Libro


class InterfazLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        
        # Etiquetas
        lbl_titulo = tk.Label(root, text="Título:")
        lbl_precio_reposicion = tk.Label(root, text="Precio de Reposición:")

        # Campos de entrada
        self.entry_titulo = tk.Entry(root)
        self.entry_precio_reposicion = tk.Entry(root)

        # Botón para registrar el libro

        # Posicionamiento de elementos en la interfaz
        lbl_titulo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        lbl_precio_reposicion.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_titulo.grid(row=1, column=1, padx=10, pady=5)
        self.entry_precio_reposicion.grid(row=2, column=1, padx=10, pady=5)

        btn_registrar_libro = tk.Button(root, text="Registrar Libro", command=self.nuevo_libro)
        btn_registrar_libro.grid(row=5, column=0, columnspan=2, pady=10)

    def nuevo_libro(self):
        try:
            titulo = self.entry_titulo.get()
            precio_reposicion = self.validar_input_float(self.entry_precio_reposicion.get())
            libro = Libro(0, titulo, precio_reposicion, activo=1,  estado_id=1)
            if libro.is_check():
                LibroDao().agregar(libro)
                self.mostrar_exito()
        except ValueError as ve:
            self.mostrar_error_validacion(str(ve))
        except Exception as e:
            self.mostrar_error_interno(str(e))

    @staticmethod
    def mostrar_exito():
        messagebox.showinfo("Éxito", "Se ha generado con éxito!")

    @staticmethod
    def mostrar_error_validacion(mensaje):
        messagebox.showinfo('Error en la validacion de los datos.', mensaje)

    @staticmethod
    def mostrar_error_interno(mensaje):
        messagebox.showinfo('Error interno.', mensaje)

    @staticmethod
    def validar_input_float(nuevo_valor):
        try:
            return float(nuevo_valor)
        except ValueError:
            raise ValueError("Error en el Precio. Debe ser de tipo numerico.")

