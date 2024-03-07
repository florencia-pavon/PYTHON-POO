# CREATE TABLE IF NOT EXISTS libros (libro_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, titulo TEXT NOT
# NULL, precio_reposicion NUMERIC (7, 2) NOT NULL, estado_id INTEGER REFERENCES estados (estado_id) NOT NULL,
# activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));
from estado import Estado


class Libro:
    
    def __init__(self, libro_id: int, titulo: str, precio_reposicion: float, estado_id: int, activo: int) -> None:
        self._libro_id = libro_id
        self._titulo = titulo
        self._precio_reposicion = precio_reposicion
        self._estado_id = estado_id
        self._activo = activo
        
        self._errores = ""
        
        self._estado = Estado

    def __str__(self) -> str:
        # return f"LibroID: {self._libro_id} | Titulo: {self._titulo} | Precio de Reposicion: ${
        # self._precio_reposicion} | Estado: {self._estado_id} | Activo: {self.es_activo()} -"
        string = f"LibroID: {self._libro_id} | Titulo: {self._titulo} | Precio de Reposicion: " \
                 f"${self._precio_reposicion} | Estado: {self.estado_descripcion()} | Activo: {self.es_activo()} -"
        return string
        
    @property
    def libro_id(self):
        return self._libro_id
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def precio_reposicion(self):
        return self._precio_reposicion
    
    @property
    def estado_id(self):
        return self._estado_id
    
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor: Estado):
        self._estado = valor
            
    @property
    def activo(self):
        return self._activo
            
    @property
    def errores(self):
        return self._errores

    def es_activo(self) -> str:
        """
        Activo =1 "SI".
        Borrado =0 "NO"
        """
        aux = "SI"
        if self._activo == 0:
            aux = "NO"
        return aux

    # ESTO NO ES RESPONSABILIDAD DE LIBRO. ESTA SOLO PARA COMPROBAR QUE LOS DATOS SON CONSISTENTES EN LOS TESTS
    def estado_descripcion(self):
        aux = "Disponible"
        if self.estado_id == 2:
            aux = "Prestado"
        if self.estado_id == 3:
            aux = "Extraviado"
        return aux

    # Para saber si los datos del objeto son consistentes con las reglas de negocio y se puede guardar en la base de
    # datos guarda los errores en el atributo errores. Se consulta con objeto.errores
    def is_check(self) -> bool:
        """
        Valida si los datos del objeto son consistentes. Usar Property .errores para conocer errores
        """
        flag = True
        if self.libro_id < 0:
            self._errores += "-Libro ID debe ser positivo \n"
            flag = False
        if len(self.titulo) > 50:
            self._errores += "-Titulo debe ser menor a 50 caracteres \n"
            flag = False
        if self._precio_reposicion <= 0:
            self._errores += "-Precio de reposicion debe ser positivo mayor a cero \n"
            flag = False

        match self._estado_id:
            case 1 | 2 | 3:
                pass 
            case _:
                self._errores += "-Estado Id debe ser 1, 2, 3 \n"
                flag = False
                           
        match self._activo:
            case 1 | 2:
                pass 
            case _:
                self._errores += "-Activo debe ser 1, 2 \n"
                flag = False
        
        if flag:
            self._errores = ""
        return flag
