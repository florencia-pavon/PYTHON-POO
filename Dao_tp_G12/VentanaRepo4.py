import tkinter as tk
from Socio_dao import SocioDao


class InterfazRepo4:
    def __init__(self, root):
        self.root = root
        self.root.title("Reporte de Prestamos por Socio")
        self.root.geometry("700x300")

        # Etiquetas
        titulo = tk.Label(root, text="Reporte de Prestamos por Socio")

        # Campo de entrada para el ID del socio
        lbl_socio_id = tk.Label(root, text="ID del Socio:")
        self.entry_socio_id = tk.Entry(root)

        # Botón para generar el reporte
        btn_generar_reporte = tk.Button(root, text="Generar Reporte", command=self.generar_reporte)

        # Resultado del reporte
        self.resultado_label = tk.Label(root, text="")

        # Botón para cerrar/salir
        btn_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar)

        # Posicionamiento de elementos en la interfaz
        titulo.grid(row=0, padx=10, pady=5, sticky="w")
        lbl_socio_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_socio_id.grid(row=1, column=1, padx=10, pady=5)
        btn_generar_reporte.grid(row=2, column=0, columnspan=2, pady=10)
        self.resultado_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")
        btn_cerrar.grid(row=4, column=0, columnspan=2, pady=10)

    def generar_reporte(self):
        try:
            socio_id = int(self.entry_socio_id.get())
            socio = SocioDao()
            prestamos = socio.prestamo_por_socio(socio_id)

            # Mostrar el resultado en la etiqueta
            resultado_text = "Prestamos del Socio:\n"
            for prestamo in prestamos:
                resultado_text += str(prestamo) + "\n"
            self.resultado_label.config(text=resultado_text)
        except ValueError:
            self.resultado_label.config(text="Error: Ingrese un ID de Socio válido.")

    def cerrar(self):
        self.root.destroy()


