from sqlalchemy import Column, Integer, String
from db_singleton import Base

class Estado(Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    
    
    def __init__(self, nombre: str):
        self.nombre=nombre
     
    def __str__(self) -> str:
        return f"Id: {self.id} | Nombre: {self.nombre}"
    
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, name):
        self.nombre = name

    def getId(self):
        return self.id
    
    @staticmethod
    def getAll(session):
        return session.query(Estado).all()

    @staticmethod
    def getById(session, estado_id):
        return session.query(Estado).filter(Estado.id == estado_id).first()
