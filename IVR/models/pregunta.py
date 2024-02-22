from sqlalchemy import Column, Integer, String, ForeignKey
from db_singleton import Base
from sqlalchemy.orm import relationship


class Pregunta(Base):
    __tablename__ = 'pregunta'

    id = Column(Integer, primary_key=True)
    pregunta = Column(String)
    id_encuesta = Column(Integer, ForeignKey('encuesta.id'))
    encuesta = relationship("Encuesta")
    
    def __init__(self, pregunta: str, id_encuesta: int):
        self.pregunta = pregunta
        self.id_encuesta = id_encuesta
        
    def __str__(self) -> str:
        return f"Id: {self.id} Pregunta: {self.pregunta} Encuesta: {self.encuesta}"

    def getId(self):
        return self.id

    def getPregunta(self):
        return self.pregunta

    def setPregunta(self, nueva_pregunta):
        self.pregunta = nueva_pregunta

    def getIdEncuesta(self):
        return self.id_encuesta

    def setIdEncuesta(self, nuevo_id_encuesta):
        self.id_encuesta = nuevo_id_encuesta

    def getEncuesta(self):
        return self.encuesta

    def setEncuesta(self, nueva_encuesta):
        self.encuesta = nueva_encuesta

    @staticmethod
    def getAll(session):
        return session.query(Pregunta).all()

    @staticmethod
    def getById(session, pregunta_id):
        return session.query(Pregunta).filter(Pregunta.id == pregunta_id).first()
