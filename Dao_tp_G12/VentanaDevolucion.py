import tkinter as tk
from tkinter import messagebox
from Prestamo import Prestamo
from Prestamo_dao import PrestamoDao
from datetime import datetime
from prestamo_error import PrestamoError


class InterfazDevolucion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Devolucion")

        lbl_prestamo_id = tk.Label(root, text="ID del Prestamo:")
        lbl_fecha_devolucion = tk.Label(root, text="Fecha de Devolucion:")

        self.entry_prestamo_id = tk.Entry(root)
        self.entry_devolucion = tk.Entry(root)

        btn_registrar_devolucion = tk.Button(root, text="Registrar Devolucion", command=self.nueva_devolucion)

        # Posicionamiento de elementos en la interfaz
        lbl_prestamo_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        lbl_fecha_devolucion.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_prestamo_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_devolucion.grid(row=2, column=1, padx=10, pady=5)

        btn_registrar_devolucion.grid(row=3, column=0, columnspan=2, pady=10)

    def nueva_devolucion(self):
        try:
            prestamo_id = self.validar_input_int(self.entry_prestamo_id.get())
            fecha_devolucion = self.entry_devolucion.get()

            prestamo_dao_instance = PrestamoDao()
            prestamo = prestamo_dao_instance.registrar_devolucion(id=prestamo_id, fecha=fecha_devolucion)

            if isinstance(prestamo, PrestamoError):
                self.mostrar_error_interno(prestamo)
            else:
                self.mostrar_exito()
        except ValueError as ve:
            self.mostrar_error_validacion(str(ve))
        except Exception as e:
            self.mostrar_error_interno(str(e))

    @staticmethod
    def mostrar_exito():
        messagebox.showinfo('Exito', 'Devolucion registrada con exito!')

    @staticmethod
    def mostrar_error_validacion(mensaje):
        messagebox.showinfo('Error en la validacion de los datos.', mensaje)

    @staticmethod
    def mostrar_error_interno(mensaje):
        messagebox.showinfo('Error Interno', mensaje)

    @staticmethod
    def validar_input_int(nuevo_valor):
        try:
            return int(nuevo_valor)
        except ValueError:
            raise ValueError('Error en los datos ingresados. Debe ser de tipo Numerico.')


