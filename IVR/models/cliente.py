from sqlalchemy import Column, Integer, String
from db_singleton import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    dni = Column(Integer)
    nombre_completo = Column(String)
    nro_celular = Column(Integer)

    def __init__(self, dni, nombre_completo, nro_celular):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.nro_celular = nro_celular

    def __str__(self):
        return f"Id: {self.id} | Dni: {self.dni} | Nombre: {self.nombre_completo} | Celular: {self.nro_celular}" 

    def getId(self):
        return self.id
    
    def getDni(self):
        return self.dni  

    def setDni(self, dniNuevo) -> None:
        self.dni = dniNuevo  
    
    def getNombreCompleto(self):
        return self.nombre_completo

    def setNombreCompleto(self, nombreNuevo) -> None:
        self.nombre_completo = nombreNuevo
    
    def getNroCelular(self):
        return self.nro_celular

    def setNroCelular(self, celularNuevo) -> None:
        self.nro_celular = celularNuevo

    @staticmethod
    def getAll(session):
        return session.query(Cliente).all()

    @staticmethod
    def getById(session, cliente_id):
        return session.query(Cliente).filter(Cliente.id == cliente_id).first()
