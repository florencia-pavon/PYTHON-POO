from sqlalchemy import Column, Integer, String, Date
from db_singleton import Base

class Encuesta(Base):
    __tablename__ = 'encuesta'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    fechaFinVigencia = Column(Date)

    def __init__(self, descripcion: str, fechaFinVigencia: Date):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        
    def __str__(self) -> str:
        return f"Id: {self.id} | Descripción: {self.descripcion} | Fecha de Fin de Vigencia: {self.fechaFinVigencia}" 

    def getId(self):
        return self.id

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def getFechaFinVigencia(self):
        return self.fechaFinVigencia

    def setFechaFinVigencia(self, nueva_fecha):
        self.fechaFinVigencia = nueva_fecha

    @staticmethod
    def getAll(session):
        return session.query(Encuesta).all()

    @staticmethod
    def getById(session, encuesta_id):
        return session.query(Encuesta).filter(Encuesta.id == encuesta_id).first()
