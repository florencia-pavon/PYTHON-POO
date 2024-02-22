from sqlalchemy import Column, Integer, DateTime, ForeignKey
from db_singleton import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from models.llamada import Llamada
from models.estado import Estado
from db_singleton import session

# Definir la estructura de la tabla CambioEstado
class CambioEstado(Base):
    __tablename__ = 'cambioEstado'

    id = Column(Integer, primary_key=True)
    fecha_hora_inicio = Column(DateTime)
    id_estado = Column(Integer, ForeignKey('estado.id'))
    id_llamada = Column(Integer, ForeignKey('llamada.id'))
    estado = relationship("Estado") 
    llamada = relationship("Llamada")  
    
    def __init__(self, fecha_hora_inicio, id_estado, id_llamada):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.id_estado = id_estado
        self.id_llamada = id_llamada
        
    def __str__(self) -> str:
          return f"Id: {self.id} | Fecha Hora Inicio: {self.fecha_hora_inicio} Estado: {self.estado} Llamada: {self.llamada}"


    def getId(self):
        return self.id

    def setId(self, nuevo_id):
        self.id = nuevo_id

    def getFechaHoraInicio(self):
        return self.fecha_hora_inicio

    def setFechaHoraInicio(self, nueva_fecha_hora_inicio):
        self.fecha_hora_inicio = nueva_fecha_hora_inicio

    def getIdEstado(self):
        return self.id_estado

    def setIdEstado(self, nuevo_id_estado):
        self.id_estado = nuevo_id_estado

    def getIdLlamada(self):
        return self.id_llamada

    def setIdLlamada(self, nuevo_id_llamada):
        self.id_llamada = nuevo_id_llamada

    def getEstado(self):
        return self.estado

    def setEstado(self, nuevo_estado):
        self.estado = nuevo_estado

    def getLlamada(self):
        return self.llamada

    def setLlamada(self, nueva_llamada):
        self.llamada = nueva_llamada
        
    @classmethod
    def sosEstadoActual(self, id_llamada) -> 'CambioEstado':
        cambiosEstados = CambioEstado.getByLlamadaId(session, id_llamada)
        if not cambiosEstados:
            return None  # Si la lista está vacía, retorna None
          
        actual = cambiosEstados[0]
        actual_fecha_hora_inicio = actual.getFechaHoraInicio()
        for cambio in cambiosEstados:
            fecha_cambio = cambio.getFechaHoraInicio() 
            if fecha_cambio > actual_fecha_hora_inicio:
                actual = cambio

                return actual

    @staticmethod
    def getAll(session):
        return session.query(CambioEstado).all()

    @staticmethod
    def getById(session, cambio_estado_id):
        return session.query(CambioEstado).filter(CambioEstado.id == cambio_estado_id).first()
    
    @staticmethod
    def getByLlamadaId(session, llamada_id):
        return session.query(CambioEstado).filter(CambioEstado.id_llamada == llamada_id).all()
