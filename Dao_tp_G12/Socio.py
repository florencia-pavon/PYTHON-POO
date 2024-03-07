# CREATE TABLE IF NOT EXISTS socios (socio_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, apellido TEXT NOT
# NULL, nombre TEXT NOT NULL, email TEXT NOT NULL, celular TEXT NOT NULL, activo INTEGER DEFAULT (1) CHECK (activo >=
# 0 and activo <= 1));

class Socio:
    
    def __init__(self, socio_id: int, apellido: str, nombre: str, email: str, celular: str, activo: int) -> None:
        self._socio_id = socio_id
        self._apellido = apellido
        self._nombre = nombre
        self._email = email
        self._celular = celular
        self._activo = activo
        
        self._errores = ""
    
    def __str__(self) -> str:
        string = f"SocioID: {self._socio_id} | Apellido: {self._apellido} | Nombre: {self._nombre} | " \
                 f"Email: {self._email} | Celular: {self._celular} | Activo: {self.es_activo()} -"
        return string

    @property
    def socio_id(self):
        return self._socio_id

    @property
    def apellido(self):
        return self._apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def celular(self):
        return self._celular

    @property
    def activo(self):
        return self._activo

    def es_activo(self) -> str:
        """
        Activo =1 "SI".
        Borrado =0 "NO"
        """
        aux = "SI"
        if self._activo == 0:
            aux = "NO"
        return aux 

    @property
    def errores(self):
        return self._errores
    
    # Para saber si los datos del objeto son consistentes con las reglas de negocio y se puede guardar en la base de
    # datos guarda los errores en el atributo errores. Se consulta con objeto.errores
    def is_check(self) -> bool:
        """
        Valida si los datos del objeto son consistentes. Usar Property .errores para conocer errores
        """
        flag = True
        if self.socio_id < 0:
            self._errores += "-Socio ID debe ser positivo \n"
            flag = False
        if len(self.apellido) > 50:
            self._errores += "-Apellido debe ser menor a 50 caracteres \n"
            flag = False
        if len(self.nombre) > 50:
            self._errores += "-Nombre debe ser menor a 50 caracteres \n"
            flag = False
        if len(self.email) > 50:
            self._errores += "-Email debe ser menor a 50 caracteres \n"
            flag = False
        if len(self.celular) == 10:
            self._errores += "-Celular debe ser de 10 caracteres \n"
            flag = False
        match self._activo:
            case 0 | 1:
                pass 
            case _:
                self._errores += "-Activo debe ser 0, 1 \n"
                flag = False

        if flag:
            self._errores = ""
        return flag    




