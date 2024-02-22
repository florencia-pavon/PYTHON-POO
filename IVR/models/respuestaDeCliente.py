from sqlalchemy import Column, Integer, Date, ForeignKey
from db_singleton import Base
from sqlalchemy.orm import relationship

# Definir la estructura de la tabla RespuestaDeCliente
class RespuestaDeCliente(Base):
    __tablename__ = 'respuestaDeCliente'

    id = Column(Integer, primary_key=True)
    fecha_encuesta = Column(Date)
    id_respuesta_posible = Column(Integer, ForeignKey('respuestaPosible.valor'))
    id_llamada = Column(Integer, ForeignKey('llamada.id'))
    respuesta_posible = relationship("RespuestaPosible")
    llamada = relationship("Llamada")  

    def __init__(self, fecha_encuesta, id_respuesta_posible, id_llamada):
        self.fecha_encuesta = fecha_encuesta
        self.id_respuesta_posible = id_respuesta_posible
        self.id_llamada = id_llamada
        
    def __str__(self) -> str:
            return f"Id: {self.id} | Fecha de la Encuesta: {self.fecha_encuesta}\nRespuesta Seleccionada: {self.respuesta_posible}\nLlamada: {self.llamada}"
    
    def getId(self):
        return self.id

    def setId(self, nuevo_id):
        self.id = nuevo_id

    def getFechaEncuesta(self):
        return self.fecha_encuesta

    def setFechaEncuesta(self, nueva_fecha_encuesta):
        self.fecha_encuesta = nueva_fecha_encuesta

    def getIdRespuestaPosible(self):
        return self.id_respuesta_posible

    def setIdRespuestaPosible(self, nuevo_id_respuesta_posible):
        self.id_respuesta_posible = nuevo_id_respuesta_posible
    
    def getRespuestaPosible(self):
        return self.respuesta_posible

    def setRespuestaPosible(self, nueva_rta):
        self.respuesta_posible = nueva_rta

    def getIdLlamada(self):
        return self.id_llamada

    def setIdLlamada(self, nuevo_id_llamada):
        self.id_llamada = nuevo_id_llamada
    
    def getLlamada(self):
        return self.llamada

    def setLlamada(self, nueva_llamada):
        self.llamada = nueva_llamada

    @staticmethod
    def getAll(session):
        return session.query(RespuestaDeCliente).all()

    @staticmethod
    def getById(session, respuesta_de_cliente_id):
        return session.query(RespuestaDeCliente).filter(RespuestaDeCliente.id == respuesta_de_cliente_id).first()
    
    @staticmethod
    def getByLlamadaId(session, llamada_id):
        return session.query(RespuestaDeCliente).filter(RespuestaDeCliente.id_llamada == llamada_id).all()
