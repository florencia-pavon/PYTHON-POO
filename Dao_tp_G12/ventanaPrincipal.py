import tkinter as tk
import os
from tkinter import Label, PhotoImage
from VentanaDevolucion import InterfazDevolucion
from VentanaLibros import InterfazLibros
from VentanaPrestamos import InterfazPrestamos
from VentanaRepo2 import InterfazRepo2
from VentanaSocios import InterfazSocios
from VentanaRepo1 import InterfazRepo1
from VentanaRepo4 import InterfazRepo4
from VentanaRepo5 import InterfazRepo5
from VentanaRepo3 import InterfazRepo3


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener el directorio del script
        img_dir = os.path.join(script_dir, 'imgs')  # Asumiendo que las imágenes están en un directorio llamado 'imgs'

        # Cargar imágenes
        self.imagen_libros = PhotoImage(file=os.path.join(img_dir, 'libro.png'))
        self.imagen_prestamos = PhotoImage(file=os.path.join(img_dir, 'prestamo.png'))
        self.imagen_socios = PhotoImage(file=os.path.join(img_dir, 'socio.png'))
        self.root.title("Inicio")

        # Configuración de la ventana principal
        self.root.geometry("600x600")  # Tamaño de la ventana principal

        # Estilo de los botones
        btn_style = {"font": ("Arial", 14), "bg": "#FA0000", "fg": "black", "relief": "ridge", "width": 20, "height": 2}
        self.root.update()

        # Poner imagenes como label
        label_imagen_libros = Label(self.root, image=self.imagen_libros)
        label_imagen_prestamos = Label(self.root, image=self.imagen_prestamos)
        label_imagen_socios = Label(self.root, image=self.imagen_socios)

        # Posicionar imagenes
        label_imagen_libros.grid(row=0, column=2, padx=2, pady=15, sticky="ne")
        label_imagen_prestamos.grid(row=2, column=2, padx=2, pady=40, sticky="ne")
        label_imagen_socios.grid(row=1, column=2, padx=2, pady=20, sticky="ne")

        # Botones
        btn_registrar_libros = tk.Button(root, text="Registrar Libros", command=self.abrir_ventana_libros, **btn_style)
        btn_registrar_socios = tk.Button(root, text="Registrar Socios", command=self.abrir_ventana_socios, **btn_style)
        btn_registrar_prestamos = tk.Button(root, text="Registrar Préstamos", command=self.abrir_ventana_prestamos, **btn_style)
        btn_registrar_devolucion = tk.Button(root, text="Registrar Devolucion", command=self.abrir_ventana_devolucion, **btn_style)
        btn_libros = tk.Button(root, text="Libros", **btn_style)
        btn_socios = tk.Button(root, text="Socios", **btn_style)
        btn_prestamos = tk.Button(root, text="Préstamos", **btn_style)
        
        btn_repo1 = tk.Button(root, text="Reporte1", command=self.abrir_ventana_repo1, **btn_style)
        btn_repo2 = tk.Button(root, text="Reporte2", command=self.abrir_ventana_repo2, **btn_style)
        btn_repo4 = tk.Button(root, text="Reporte4", command=self.abrir_ventana_repo4, **btn_style)
        btn_repo5 = tk.Button(root, text="Reporte5", command=self.abrir_ventana_repo5, **btn_style)
        btn_repo3 = tk.Button(root, text="Reporte3", command=self.abrir_ventana_repo3, **btn_style)

        # Posicionamiento de los botones en la ventana principal
        btn_libros.grid(row=0, column=0, pady=20, padx=10)
        btn_socios.grid(row=1, column=0, pady=20, padx=10)
        btn_prestamos.grid(row=2, column=0, pady=20, padx=10)
        btn_registrar_libros.grid(row=0, column=1, pady=20, padx=10)
        btn_registrar_socios.grid(row=1, column=1, pady=20, padx=10)
        btn_registrar_prestamos.grid(row=2, column=1, pady=20, padx=10)
        btn_registrar_devolucion.grid(row=5, column=1, pady=20, padx=10)
        
        btn_repo1.grid(row=3, column=0, pady=20, padx=10)
        btn_repo2.grid(row=3, column=1, pady=20, padx=10)
        btn_repo4.grid(row=4, column=0, pady=20, padx=10)
        btn_repo5.grid(row=4, column=1, pady=20, padx=10)
        btn_repo3.grid(row=5, column=0, pady=20, padx=10)

    def abrir_ventana_libros(self):
        ventana_libros = tk.Toplevel(self.root)
        ventana_libros.grab_set()  # Hacer que la ventana sea modal
        interfaz_libros = InterfazLibros(ventana_libros)

    def abrir_ventana_devolucion(self):
        ventana_devolucion = tk.Toplevel(self.root)
        ventana_devolucion.grab_set()  # Hacer que la ventana sea modal
        interfaz_libros = InterfazDevolucion(ventana_devolucion)

    def abrir_ventana_socios(self):
        ventana_socios = tk.Toplevel(self.root)
        ventana_socios.grab_set()  # Hacer que la ventana sea modal
        interfaz_socios = InterfazSocios(ventana_socios)

    def abrir_ventana_prestamos(self):
        ventana_prestamos = tk.Toplevel(self.root)
        ventana_prestamos.grab_set() # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazPrestamos(ventana_prestamos)

    def abrir_ventana_repo1(self):
        ventana_repo1 = tk.Toplevel(self.root)
        ventana_repo1.grab_set()  # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazRepo1(ventana_repo1)

    def abrir_ventana_repo2(self):
        ventana_repo2 = tk.Toplevel(self.root)
        ventana_repo2.grab_set()  # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazRepo2(ventana_repo2)

    def abrir_ventana_repo4(self):
        ventana_repo4 = tk.Toplevel(self.root)
        ventana_repo4.grab_set()  # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazRepo4(ventana_repo4)

    def abrir_ventana_repo5(self):
        ventana_repo5 = tk.Toplevel(self.root)
        ventana_repo5.grab_set()  # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazRepo5(ventana_repo5)

    def abrir_ventana_repo3(self):
        ventana_repo3 = tk.Toplevel(self.root)
        ventana_repo3.grab_set()  # Hacer que la ventana sea modal
        interfaz_prestamos = InterfazRepo3(ventana_repo3)


root = tk.Tk()
ventana_principal = VentanaPrincipal(root)
root.mainloop()

