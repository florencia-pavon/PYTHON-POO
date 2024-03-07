import tkinter as tk
from tkinter import messagebox
from Prestamo import Prestamo
from Prestamo_dao import PrestamoDao
from datetime import datetime
from prestamo_error import PrestamoError


class InterfazPrestamos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Préstamos")

        # Etiquetas
        lbl_libro_id = tk.Label(root, text="ID del Libro:")
        lbl_socio_id = tk.Label(root, text="ID del Socio:")
        lbl_duracion = tk.Label(root, text="Duración (días):")

        # Campos de entrada
        self.entry_libro_id = tk.Entry(root)
        self.entry_socio_id = tk.Entry(root)
        self.entry_duracion = tk.Entry(root)

        # Botón para registrar el préstamo
        btn_registrar_prestamo = tk.Button(root, text="Registrar Préstamo", command=self.nuevo_prestamo)

        # Posicionamiento de elementos en la interfaz
        lbl_libro_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        lbl_socio_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        lbl_duracion.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_libro_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_socio_id.grid(row=1, column=1, padx=10, pady=5)
        self.entry_duracion.grid(row=2, column=1, padx=10, pady=5)

        btn_registrar_prestamo.grid(row=3, column=0, columnspan=2, pady=10)

    def nuevo_prestamo(self):
        try:
            libro_id = self.validar_input_int(self.entry_libro_id.get())
            socio_id = self.validar_input_int(self.entry_socio_id.get())
            dias_pactados = self.validar_input_int(self.entry_duracion.get())
            fecha_prestamo = datetime.now()
            fecha_prestamo_formateada = fecha_prestamo.strftime('%Y-%m-%d')

            prestamo = Prestamo(prestamo_id=0, socio_id=socio_id, libro_id=libro_id, activo=1,
                                fecha_prestamo=fecha_prestamo_formateada, dias_pactados=dias_pactados, dias_retraso=None,  fecha_devolucion=None)
            print(prestamo)
            if prestamo.is_check():
                prestamo_db = PrestamoDao().registrar_prestamo(prestamo)
                if isinstance(prestamo_db, PrestamoError):
                    self.mostrar_error_interno(prestamo_db)
                else:
                    self.mostrar_exito()
            else:
                self.mostrar_error_interno(str(prestamo.errores))
        except ValueError as ve:
            self.mostrar_error_validacion(str(ve))
        except Exception as e:
            self.mostrar_error_interno(str(e))

    @staticmethod
    def mostrar_exito():
        messagebox.showinfo("Éxito", "Préstamo registrado con éxito!")

    @staticmethod
    def mostrar_error_validacion(mensaje):
        messagebox.showinfo('Error en los datos del prestamo.', mensaje)

    @staticmethod
    def mostrar_error_interno(mensaje):
        messagebox.showinfo('Error Interno.', mensaje)

    @staticmethod
    def validar_input_int(nuevo_valor):
        try:
            return int(nuevo_valor)
        except ValueError:
            raise ValueError("Error en los datos ingresados. Debe ser de tipo numerico.")

