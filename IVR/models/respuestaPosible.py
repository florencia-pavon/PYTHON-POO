from sqlalchemy import Column, Integer, String, ForeignKey
from db_singleton import Base
from sqlalchemy.orm import relationship

# Definir la estructura de la tabla RespuestaPosible
class RespuestaPosible(Base):
    __tablename__ = 'respuestaPosible'

    valor = Column(Integer, primary_key=True)
    descripcion = Column(String)
    id_pregunta = Column(Integer, ForeignKey('pregunta.id'))
    pregunta = relationship("Pregunta")
    
    def __init__(self, valor: int, descripcion: str, id_pregunta: int):
        self.valor = valor
        self.descripcion = descripcion
        self.id_pregunta = id_pregunta
        
    def __str__(self) -> str:
        return f"Valor: {self.valor} | Descripcion: {self.descripcion} Pregunta: {self.pregunta} "

    def getValor(self):
        return self.valor

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def getIdPregunta(self):
        return self.id_pregunta

    def setIdPregunta(self, nuevo_id_pregunta):
        self.id_pregunta = nuevo_id_pregunta

    def getPregunta(self):
        return self.pregunta

    def setPregunta(self, nueva_pregunta):
        self.pregunta = nueva_pregunta

    @staticmethod
    def getAll(session):
        return session.query(RespuestaPosible).all()

    @staticmethod
    def getById(session, valor):
        return session.query(RespuestaPosible).filter(RespuestaPosible.valor == valor).first()
