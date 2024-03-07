import tkinter as tk
from tkinter import messagebox
from Socio import Socio
from Socio_dao import SocioDao


class InterfazSocios:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Socios")

        # Etiquetas
        lbl_socio_id = tk.Label(root, text="ID del Socio:")
        lbl_apellido = tk.Label(root, text="Apellido:")
        lbl_nombre = tk.Label(root, text="Nombre:")
        lbl_email = tk.Label(root, text="Email:")
        lbl_celular = tk.Label(root, text="Celular:")
        lbl_activo = tk.Label(root, text="Activo:")

        # Campos de entrada
        self.entry_socio_id = tk.Entry(root)
        self.entry_apellido = tk.Entry(root)
        self.entry_nombre = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_celular = tk.Entry(root)
        self.entry_activo = tk.Entry(root)

        # Botón para registrar el socio
        btn_registrar_socio = tk.Button(root, text="Registrar Socio", command=self.nuevo_socio)

        # Posicionamiento de elementos en la interfaz
        lbl_socio_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        lbl_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        lbl_email.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        lbl_celular.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        lbl_activo.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.entry_socio_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=5)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=5)
        self.entry_email.grid(row=3, column=1, padx=10, pady=5)
        self.entry_celular.grid(row=4, column=1, padx=10, pady=5)
        self.entry_activo.grid(row=5, column=1, padx=10, pady=5)

        btn_registrar_socio.grid(row=6, column=0, columnspan=2, pady=10)

    def nuevo_socio(self):
        try:
            apellido = self.entry_apellido.get()
            nombre = self.entry_nombre.get()
            email = self.entry_email.get()
            celular = self.entry_celular.get()
            socio = Socio(0, apellido, nombre, email, celular, activo=1)
            if socio.is_check():
                SocioDao().agregar(socio)
                self.mostrar_exito()
        except ValueError as ve:
            self.mostrar_error_validacion(str(ve))
        except Exception as e:
            self.mostrar_error_interno(str(e))

    @staticmethod
    def mostrar_exito():
        messagebox.showinfo("Éxito", "Socio registrado con éxito!")

    @staticmethod
    def mostrar_error_validacion(mensaje):
        messagebox.showinfo('Error en la validacion de los datos.', mensaje)

    @staticmethod
    def mostrar_error_interno(mensaje):
        messagebox.showinfo('Error interno.', mensaje)

