from typing import List
from interfaces.iAgregado import IAgregado
from interfaces.iterador import Iterator
from tkinter import *
from tkinter import messagebox
from datetime import date
from models.llamada import Llamada
from models.cliente import Cliente
from db_singleton import session
from iteradores.iteradorLlamadas import IteradorLlamadas
from models.cambioEstado import CambioEstado


class GestorConsultarEncuesta(IAgregado):
    
    
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fecha_desde = None
        self.fecha_hasta = None
        self.llamada_seleccionada = None
        self.cliente = None
        self.nombreEstadoActual = None
        self.duracionLlamada = None
        self.respuestas = []
        self.preguntas = []
        self.descripcionEncuesta = None

    def getDuracionLlamada(self):
        return self.duracionLlamada
    
    def getPreguntas(self):
        return self.preguntas
            

    def setDuracionLlamada(self, nuevaDuracionLlamada):
        self.duracionLlamada = nuevaDuracionLlamada

    def agregarRespuesta(self, rta):
        self.respuestas.append(rta)

    def quitarRespuesta(self, rta):
        self.respuestas.remove(rta)

    def agregarPregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def quitarPregunta(self, pregunta):
        self.preguntas.remove(pregunta)

    def getDescripcionEncuesta(self):
        return self.descripcionEncuesta

    def setDescripcionEncuesta(self, nuevaDescripcionEncuesta):
        self.descripcionEncuesta = nuevaDescripcionEncuesta
        
        
    def getNombreEstadoActual(self):
        return self.nombreEstadoActual
    
    def setNombreEstadoActual(self, nuevoNombreEstado):
        self.nombreEstadoActual = nuevoNombreEstado
        
    def getPantalla(self):
        return self.pantalla
    
    def getRespuestas(self):
        return self.respuestas
    
    def setPantalla(self, nuevaPantalla):
        self.pantalla = nuevaPantalla
        
    def getCliente(self):
        return self.Cliente
    
    def setCliente(self, nuevoCliente):
        self.Cliente = nuevoCliente
        
    def getFechaDesde(self):
        return self.fecha_desde
    
    def setFechaDesde(self, nuevaFecha):
        self.fecha_desde = nuevaFecha
    
    def getFechaHasta(self):
        return self.fecha_hasta
    
    def setFechaHasta(self, nuevaFecha):
        self.fecha_hasta = nuevaFecha
      
    @classmethod  
    def getLlamadaSeleccionada(cls):
        return cls.llamada_seleccionada
    
    @classmethod
    def setLlamadaSeleccionada(cls, nuevaLlamada):
        cls.llamada_seleccionada = nuevaLlamada
        
    def crearIterador(self, elementos:List[Llamada]) -> IteradorLlamadas:
        periodo = [self.fecha_desde, self.fecha_hasta]
        iterator = IteradorLlamadas(elementos, periodo)
        return iterator
    
    
    def consultarEncuesta(self):
        self.pantalla.pedirPeriodoFecha()
    
    def tomarPeriodoFecha(self, fecha_desde, fecha_hasta):
        if not self.validarPeriodo(*fecha_desde) or not self.validarPeriodo(*fecha_hasta):
            return None
    
        diaDesde = int(fecha_desde[0])
        mesDesde = int(fecha_desde[1])
        añoDesde = int(fecha_desde[2])
        fecha_desde = date(year=añoDesde, month=mesDesde, day=diaDesde)
        

        diaHasta = int(fecha_hasta[0])
        mesHasta = int(fecha_hasta[1])
        añoHasta = int(fecha_hasta[2])
        fecha_hasta = date(year=añoHasta, month=mesHasta, day=diaHasta)
        
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta

        self.buscarLlamadasConEncuestas()

    def validarPeriodo(self, day, month, year):
        if len(day) > 2 or str(day) == "" or int(day) > 31:
            messagebox.showerror(title="Error", message="Datos no válidos!")
            return False
        elif len(month) > 2 or str(month) == "" or int(month) > 12:
            messagebox.showerror(title="Error", message="Datos no válidos!")
            return False
        elif len(year) > 4 or str(year) == "" or int(year) > 3000:
            messagebox.showerror(title="Error", message="Datos no válidos!")
            return False
        else:
            return True
        
    def buscarLlamadasConEncuestas(self):
        llamadas_con_encuesta = []
        llamadas = Llamada.getAll(session)
        iterator_llamada = self.crearIterador(llamadas)
        iterator_llamada.primero()
        while not iterator_llamada.haTerminado():
            llamada = iterator_llamada.actual()
            if iterator_llamada.cumpleFiltro(llamada):
                llamadas_con_encuesta.append(llamada)
            iterator_llamada.siguiente()
        
        self.pantalla.mostrarLlamadasConEncuestas(llamadas_con_encuesta)
        
    def buscarDatosLlamadaSeleccionada(self):
        llamada_seleccionada = self.getLlamadaSeleccionada()
        cliente = llamada_seleccionada.getCliente()
        self.setCliente(cliente)
        nombre_estado_actual = CambioEstado.sosEstadoActual(llamada_seleccionada.getId()).getEstado().getNombre()
        self.setNombreEstadoActual(nombre_estado_actual)
        duracion = llamada_seleccionada.getDuracion()
        self.setDuracionLlamada(duracion)
        respuestas = llamada_seleccionada.getRespuestas()
        iterator_rta_cliente = llamada_seleccionada.crearIterador(respuestas)
        iterator_rta_cliente.primero()
        while not iterator_rta_cliente.haTerminado():
            rta_cliente_actual = iterator_rta_cliente.actual()
            if iterator_rta_cliente.cumpleFiltro(rta_cliente_actual):
                descripcion_rta = rta_cliente_actual.getRespuestaPosible().getDescripcion()
                self.agregarRespuesta(descripcion_rta)
                pregunta = rta_cliente_actual.getRespuestaPosible().getPregunta().getPregunta()
                self.agregarPregunta(pregunta)
                encuesta = rta_cliente_actual.getRespuestaPosible().getPregunta().getEncuesta().getDescripcion()
                self.setDescripcionEncuesta(encuesta)
            iterator_rta_cliente.siguiente()

        self.pantalla.mostrarDatosLlamadaSeleccionada()
            
            
         

        
        
session.close()