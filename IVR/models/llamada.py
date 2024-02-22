
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from db_singleton import Base
from sqlalchemy.orm import relationship
from models.respuestaDeCliente import RespuestaDeCliente
from models.cliente import Cliente
from models.respuestaPosible import RespuestaPosible
from models.pregunta import Pregunta
from models.encuesta import Encuesta
from db_singleton import session
from datetime import date, datetime
from interfaces.iAgregado import IAgregado
from iteradores.iteradorRespuestaDeCliente import IteradorRespuestaDeCliente
from typing import List

class NewMeta(type(IAgregado), type(Base)):
   pass

# Definir la estructura de la tabla Llamada
class Llamada(IAgregado, Base, metaclass=NewMeta):
    __tablename__ = 'llamada'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    descripcion_operador = Column(String)
    detalle_accion = Column(String)
    duracion = Column(Integer)
    encuesta_enviada = Column(Boolean)
    observacion_auditor = Column(String)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente")  
    
    def __init__(self, fecha, descripcion_operador, detalle_accion, duracion, encuesta_enviada, observacion_auditor, id_cliente):
        self.fecha = fecha
        self.descripcion_operador = descripcion_operador
        self.detalle_accion = detalle_accion
        self.duracion = duracion
        self.encuesta_enviada = encuesta_enviada
        self.observacion_auditor = observacion_auditor
        self.id_cliente = id_cliente
        
    def __str__(self) -> str:
        return f"\n | Id: {self.id} | Fecha: {self.fecha} | Descripción del Operador: {self.descripcion_operador} | Detalle de Acción Requerida: {self.detalle_accion}\n | Duración de la Llamada: {self.duracion} minutos | Encuesta enviada: {self.encuesta_enviada} | Observación del Auditor: {self.observacion_auditor} \n | Cliente: {self.cliente}"

    def getId(self):
        return self.id

    def setId(self, nuevo_id):
        self.id = nuevo_id

    def getFecha(self):
        return self.fecha

    def setFecha(self, nueva_fecha):
        self.fecha = nueva_fecha

    def getDescripcionOperador(self):
        return self.descripcion_operador

    def setDescripcionOperador(self, nueva_descripcion):
        self.descripcion_operador = nueva_descripcion

    def getDetalleAccion(self):
        return self.detalle_accion

    def setDetalleAccion(self, nuevo_detalle):
        self.detalle_accion = nuevo_detalle

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, nueva_duracion):
        self.duracion = nueva_duracion

    def getEncuestaEnviada(self):
        return self.encuesta_enviada

    def setEncuestaEnviada(self, nueva_encuesta):
        self.encuesta_enviada = nueva_encuesta

    def getObservacionAuditor(self):
        return self.observacion_auditor

    def setObservacionAuditor(self, nueva_observacion):
        self.observacion_auditor = nueva_observacion

    def getIdCliente(self):
        return self.id_cliente

    def setIdCliente(self, nuevo_id_cliente):
        self.id_cliente = nuevo_id_cliente

    def getCliente(self):
        return self.cliente

    def setCliente(self, nuevo_cliente):
        self.cliente = nuevo_cliente
        
    def tieneRespuestas(self) -> bool:
        rta_cliente = RespuestaDeCliente.getByLlamadaId(session, self.id)
        return bool(rta_cliente)
    
    def esDePeriodo(self, fecha_desde: date, fecha_hasta: date):
        fecha_date = self.fecha
        if fecha_desde <= fecha_date <= fecha_hasta:
            return True
        return False
    
    def getRespuestas(self):
        rtas = RespuestaDeCliente.getAll(session)
        return rtas
        
    
    def crearIterador(self, elementos:List[RespuestaDeCliente]) -> IteradorRespuestaDeCliente:
        id_llamada_seleccionada = self.getId()
        iterator_rta_cliente = IteradorRespuestaDeCliente(elementos, id_llamada_seleccionada)
        return iterator_rta_cliente
        
        
    

    
    
    

        

    @staticmethod
    def getAll(session):
        return session.query(Llamada).all()

    @staticmethod
    def getById(session, llamada_id):
        return session.query(Llamada).filter(Llamada.id == llamada_id).first()
