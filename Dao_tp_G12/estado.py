# CREATE TABLE IF NOT EXISTS estados (estado_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, descripcion TEXT);
# estado:  (disponible, prestado o extraviado)

class Estado():
    def __init__(self,estado_id,descripcion) -> None:
        self._estado_id=estado_id
        self._descripcion=descripcion
        

    @property
    def estado_id(self):
        return self._estado_id
    
    @property
    def descripcion(self):
        return self._descripcion
    
    def __str__(self) -> str:
        return f"EstadoID: {self._estado_id} | Descripcion: {self._descripcion}"    
        
