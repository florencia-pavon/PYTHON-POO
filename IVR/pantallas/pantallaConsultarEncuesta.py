from tkinter import *
from tkinter import messagebox,ttk,font
import tkinter as tk
import csv
import time
import sys


class PantallaConsultaEncuesta():
    def __init__(self, gestor):
        self.gestor = gestor
        
    def opcionConsultarEncuesta(self):  
        self.root = Tk()
        icono = PhotoImage(file="imgs/icono.PNG")
        self.root.iconphoto(True, icono)
        self.root.geometry("400x70")
        self.root.title("Interfaz")
        self.root.resizable(False, False)
        
        icono_resized = icono.subsample(5, 5)  # Ajusta el tamaño (puedes experimentar con los valores)

        # Crear un widget Label para mostrar la imagen
        label_imagen = Label(self.root, image=icono_resized)
        label_imagen.grid(row=0, column=0, padx=40, pady=2, sticky="ne")  # Alinea la imagen en la esquina superior derecha


        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.cerrar_presionado = False

        self.boton = Button(self.root, text="Consultar Encuesta", font=mi_tipo_de_letra, command=self.habilitarPantallaConsultarEncuesta)
        self.boton.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.boton.place(relx=0.5, rely=0.5, anchor="center")

        self.cerrar_button = Button(self.root, text="Cerrar", command=self.cerrar_press)
        self.cerrar_button.place(relx=1, rely=1, anchor="se")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        self.center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:return False

    def habilitarPantallaConsultarEncuesta(self):
        messagebox.showinfo(title="Informacion",message="Se habilito la pantalla")
        self.gestor.consultarEncuesta()
        
    def pedirPeriodoFecha(self):
        fecha_desde = self.tomarFechaDesde()
        fecha_hasta = self.tomarFechaHasta()
        self.gestor.tomarPeriodoFecha(fecha_desde, fecha_hasta)
        
    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry("{}x{}+{}+{}".format(width, height, x, y))
        
    def cerrar_press(self):
        self.cerrar_presionado = True
        self.root.quit()
        
    def tomarFechaDesde(self):
        self.root = Tk()
        self.root.geometry("600x90")
        self.root.title("Pantalla Fecha Desde")
        self.root.resizable(False, False)

        self.cerrar_presionado = False

        self.entryDiaDeEntrada = StringVar()
        self.entryMesDeEntrada = StringVar()
        self.entryAnioDeEntrada = StringVar()

        
        self.lblDiaDeEntrada = Label(self.root, text="Día de entrada:")
        self.entryDiaDeEntrada = Entry(self.root, width=3, textvariable=self.entryDiaDeEntrada)

        self.lblMesDeEntrada = Label(self.root, text="Mes de entrada:")
        self.entryMesDeEntrada = Entry(self.root, width=3, textvariable=self.entryMesDeEntrada)

        self.lblAnioDeEntrada = Label(self.root, text="Año de entrada:")
        self.entryAnioDeEntrada = Entry(self.root, width=5, textvariable=self.entryAnioDeEntrada)

        self.consultar_button = Button(self.root, text="Enviar",command=self.root.quit)
        self.cerrar_button = Button(self.root, text="Cerrar",  command=self.cerrar_press)


        self.lblDiaDeEntrada.grid(row=0, column=0, padx=3, pady=3)
        self.entryDiaDeEntrada.grid(row=0, column=1, padx=3, pady=3)
        self.lblMesDeEntrada.grid(row=0, column=2, padx=3, pady=3)
        self.entryMesDeEntrada.grid(row=0, column=3, padx=3, pady=3)
        self.lblAnioDeEntrada.grid(row=0, column=4, padx=3, pady=3)
        self.entryAnioDeEntrada.grid(row=0, column=5, padx=3, pady=3)
        self.consultar_button.grid(row=1, column=3, padx=5, pady=5)
        self.cerrar_button.grid(row=1, column=2, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        self.center_window(self.root)
        self.root.mainloop()
        if self.cerrar_presionado==False:
            return self.entryDiaDeEntrada.get(),self.entryMesDeEntrada.get(),self.entryAnioDeEntrada.get()
        else: return False

    def tomarFechaHasta(self):
        self.root = Tk()
        self.root.geometry("600x90")
        self.root.title("Pantalla Fecha Hasta")
        self.root.resizable(False, False)

        self.cerrar_presionado = False

        self.entryDiaDeSalida=StringVar()
        self.entryMesDeSalida = StringVar()
        self.entryAnioDeSalida = StringVar()

        self.lblDiaDeSalida = Label(self.root, text="Día de salida:")
        self.entryDiaDeSalida = Entry(self.root, width=3, textvariable=self.entryDiaDeSalida)

        self.lblMesDeSalida = Label(self.root, text="Mes de salida:")
        self.entryMesDeSalida = Entry(self.root, width=3, textvariable=self.entryMesDeSalida)

        self.lblAnioDeSalida = Label(self.root, text="Año de salida:")
        self.entryAnioDeSalida = Entry(self.root, width=5, textvariable=self.entryAnioDeSalida)

        self.consultar_button = Button(self.root, text="Enviar",command=self.root.quit)
        self.cerrar_button = Button(self.root, text="Cerrar", command=self.cerrar_press)

        self.lblDiaDeSalida.grid(row=1, column=0, padx=5, pady=5)
        self.entryDiaDeSalida.grid(row=1, column=1, padx=5, pady=5)
        self.lblMesDeSalida.grid(row=1, column=2, padx=5, pady=5)
        self.entryMesDeSalida.grid(row=1, column=3, padx=5, pady=5)
        self.lblAnioDeSalida.grid(row=1, column=4, padx=5, pady=5)
        self.entryAnioDeSalida.grid(row=1, column=5, padx=5, pady=5)
        self.consultar_button.grid(row=2, column=3, padx=5, pady=5)
        self.cerrar_button.grid(row=2, column=2, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        self.center_window(self.root)
        self.root.mainloop()
        if self.cerrar_presionado==False:
            return self.entryDiaDeSalida.get(),self.entryMesDeSalida.get(),self.entryAnioDeSalida.get()
        else: return False
        
    def mostrarLlamadasConEncuestas(self, llamadas: list):
        if len(llamadas) > 0:
            self.root = Tk()
            self.root.title("Llamadas con Encuesta")
            treeview = ttk.Treeview(self.root)

            treeview["columns"] = ("id", "fecha", "descripcion_operador", "detalle_accion", "duracion", "encuesta_enviada", "observacion_auditor", "id_cliente")


            treeview.column("#0", width=0, stretch=NO)
            treeview.column("id", anchor=CENTER)
            treeview.column("fecha", anchor=CENTER)
            treeview.column("descripcion_operador", anchor=CENTER)
            treeview.column("detalle_accion", anchor=CENTER)
            treeview.column("duracion", anchor=CENTER)
            treeview.column("encuesta_enviada", anchor=CENTER)
            treeview.column("observacion_auditor", anchor=CENTER)
            treeview.column("id_cliente", anchor=CENTER)

            

            treeview.heading("#0", text="")
            treeview.heading("id", text="Id")
            treeview.heading("fecha", text="Fecha")
            treeview.heading("descripcion_operador", text="Descripción Operador")
            treeview.heading("detalle_accion", text="Detalle Acción Requerida")
            treeview.heading("duracion", text="Duración")
            treeview.heading("encuesta_enviada", text="Encuesta Enviada")
            treeview.heading("observacion_auditor", text="Observación Auditor")
            treeview.heading("id_cliente", text="Id Cliente")
    

            self.cerrar_presionado = False

            for i, llamada in enumerate(llamadas):
                treeview.insert("", i, text="", values=(
                    llamada.getId(),
                    llamada.getFecha(),
                    llamada.getDescripcionOperador(),
                    llamada.getDetalleAccion(),
                    llamada.getDuracion(),
                    llamada.getEncuestaEnviada(),
                    llamada.getObservacionAuditor(),
                    llamada.getIdCliente()
                    

                ))

            treeview.pack()

            self.boton = ttk.Button(self.root, text="Seleccionar", command=lambda: self.pedirSeleccionDellamada(treeview, llamadas))
            self.boton.pack()

            self.cerrar_button = Button(self.root, text="Cerrar", command=self.cerrar_press)
            self.cerrar_button.pack()

            self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

            self.root.mainloop()

            if not self.cerrar_presionado:
                return treeview
            else:
                return False
        else:
            messagebox.showinfo(title="Informacion", message="No hay llamadas con encuestas")
            return False
        
    def pedirSeleccionDellamada(self, treeview, llamadas):
            messagebox.showinfo(title="Informacion", message="Se ha tomado la seleccion")
            llamada_seleccionada = self.tomarLlamada(treeview, llamadas)
            self.gestor.setLlamadaSeleccionada(llamada_seleccionada)
            self.gestor.buscarDatosLlamadaSeleccionada()
            #formato = self.pedirSeleccionFormato()
            
    def tomarLlamada(self, treeview, llamadas):
        seleccion = treeview.selection()
        if seleccion:
            llamada_id = seleccion[0]
            llamada_values = treeview.item(llamada_id)["values"]
            for llamada in llamadas:
                if llamada.getId() == llamada_values[0]: 
                    return llamada
        return None 
    
    def mostrarDatosLlamadaSeleccionada(self):
        cliente = self.gestor.getCliente()
        nombre_estado_actual = self.gestor.getNombreEstadoActual()
        duracion_llamada = self.gestor.getDuracionLlamada()
        respuestas = self.gestor.getRespuestas()
        preguntas = self.gestor.getPreguntas()
        descripcion_encuesta = self.gestor.getDescripcionEncuesta()

        self.root = Tk()
        self.root.title("Datos de la Llamada")
        self.root.geometry("800x400")
        
        # Etiquetas para mostrar datos estáticos
        cliente_label = Label(self.root, text=f"Cliente: {cliente}", font=("Arial", 16))
        estado_label = Label(self.root, text=f"Estado Actual: {nombre_estado_actual}", font=("Arial", 16))
        duracion_label = Label(self.root, text=f"Duración de la llamada: {duracion_llamada} minutos", font=("Arial", 16))
        descripcion_encuesta_label = Label(self.root, text=f"Descripción de la encuesta: {descripcion_encuesta}", font=("Arial", 16))
        
        cliente_label.pack(padx=20, pady=5, anchor='w')
        estado_label.pack(padx=20, pady=5, anchor='w')
        duracion_label.pack(padx=20, pady=5, anchor='w')
        descripcion_encuesta_label.pack(padx=20, pady=5, anchor='w')
        
        # Etiquetas para mostrar preguntas y respuestas
        for i in range(len(preguntas)):
            pregunta_label = Label(self.root, text=f"Pregunta {i + 1}: {preguntas[i]}", font=("Arial", 16), fg="yellow")
            respuesta_label = Label(self.root, text=f"Respuesta {i + 1}: {respuestas[i]}", font=("Arial", 16))
            
            pregunta_label.pack(padx=20, pady=5, anchor='w')
            respuesta_label.pack(padx=20, pady=5, anchor='w')
        
        generar_csv_button = Button(self.root, text="Generar CSV", command=self.generarInforme)
        generar_csv_button.pack(side=RIGHT, padx=10, pady=10)
        
        imprimir_button = Button(self.root, text="Imprimir", command=self.imprimir)
        imprimir_button.pack(side=RIGHT, padx=10, pady=10)
        
        self.cerrar_button = Button(self.root, text="Cerrar", command=self.cerrar_press)
        self.cerrar_button.pack(side=LEFT, padx=10, pady=10) 
        
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        self.center_window(self.root)
 
        


    def generarInforme(self):
        nombre_cliente = self.gestor.getCliente().getNombreCompleto()
        nombre_estado_actual = self.gestor.getNombreEstadoActual()
        duracion_llamada = self.gestor.getDuracionLlamada()
        respuestas = self.gestor.getRespuestas()
        preguntas = self.gestor.getPreguntas()

        # Crear nueva ventana
        self.csv_window = Toplevel()
        self.csv_window.title("Datos en formato CSV")

        # Etiqueta para el encabezado
        encabezado_label = Label(self.csv_window, text=f"\nNombre del cliente: {nombre_cliente}\nEstado actual: {nombre_estado_actual}\nDuración de la llamada: {duracion_llamada} minutos", font=("Arial", 18))
        encabezado_label.pack(padx=20, pady=10, anchor='w')

        # Lista para almacenar los datos
        datos_csv = [
            [nombre_cliente, nombre_estado_actual, duracion_llamada, "minutos"]
        ]
         
        #Agregar datos al archivo CSV y mostrar en pantalla
        for i in range(len(preguntas)):
            pregunta = preguntas[i]
            respuesta = respuestas[i]
            datos_csv.append([f"Pregunta {i + 1}", pregunta, respuesta, "Marca de cierre"])

            pregunta_label = Label(self.csv_window, text=f"Pregunta {i + 1}: {pregunta}", font=("Arial", 16, "bold"))
            pregunta_label.pack(padx=20, pady=5, anchor='w')

            respuesta_label = Label(self.csv_window, text=f"Respuesta {i + 1}: {respuesta}", font=("Arial", 16))
            respuesta_label.pack(padx=20, pady=5, anchor='w')


        # Botón para cerrar la ventana y escribir el archivo CSV
        def guardar_csv():
            with open('datos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(datos_csv)
            self.csv_window.destroy()

        guardar_button = Button(self.csv_window, text="Guardar CSV", command=guardar_csv)
        guardar_button.pack(padx=20, pady=10)

        cerrar_button = Button(self.csv_window, text="Cerrar", command=self.csv_window.destroy)
        cerrar_button.pack(padx=20, pady=10)
        
    def imprimir(self):
        # Función para cerrar la ventana después de 3 segundos
        def close_window():
            root.destroy()
            sys.exit()

        root = tk.Tk()
        root.title("Imprimir")
        root.geometry("300x100")
        
        label = tk.Label(root, text="Imprimiendo...", font=("Arial", 16))
        label.pack(padx=20, pady=20)

        root.after(3000, close_window)  # Cierra la ventana después de 3000 milisegundos (3 segundos)

        root.mainloop()
        
        

            



            
            
            
            


    


        
            
            
