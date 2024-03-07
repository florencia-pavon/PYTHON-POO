# CREATE TABLE IF NOT EXISTS prestamos (prestamo_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
# socio_id INTEGER REFERENCES socios (socio_id) NOT NULL, libro_id INTEGER REFERENCES libros (libro_id) NOT NULL,
# fecha_prestamo DATETIME NOT NULL, dias_pactados INTEGER NOT NULL CHECK (dias_pactados > 0), fecha_devolucion
# DATETIME, dias_retraso INTEGER CHECK (dias_retraso > 0), activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo
# <= 1));

from Libro import Libro
from Socio import Socio
from datetime import datetime


class Prestamo:

    #def init_basico(self, prestamo_id: int, socio_id: int, libro_id: int, fecha_prestamo: str,
    #                dias_pactados: int) -> None:
    #    """
    #    Carga objeto Prestamo nuevo sin fecha de devolucion ni dias de retraso
    #    """
    #    self._prestamo_id = prestamo_id
    #    self._socio_id = socio_id
    #    self._libro_id = libro_id
    #    self._fecha_prestamo = fecha_prestamo
    #    self._dias_pactados = dias_pactados
    #    self._activo = 1
#
    #    self._errores = ""
    #    self._fecha_devolucion = None
    #    self._dias_retraso = None
#
    #    self._socio = Socio
    #    self._libro = Libro
#
    #def init_completo(self, prestamo_id: int, socio_id: int, libro_id: int, fecha_prestamo: str, dias_pactados: int,
    #                  fecha_devolucion: str, dias_retraso: int, activo: int) -> None:
    #    """
    #    Carga Objeto Prestamo para guarduar uno completo con fecha de devolucion y dias de retraso.
    #    O como viene de la base de datos
    #    """
    #    self._prestamo_id = prestamo_id
    #    self._socio_id = socio_id
    #    self._libro_id = libro_id
    #    self._fecha_prestamo = fecha_prestamo
    #    self._dias_pactados = dias_pactados
    #    self._fecha_devolucion = fecha_devolucion
    #    self._dias_retraso = dias_retraso
    #    self._activo = activo
#
    #    self._errores = ""
    #    self._socio = Socio
    #    self._libro = Libro

    def __init__(self, prestamo_id: int, socio_id: int, libro_id: int, fecha_prestamo: str, dias_pactados: int,
                 fecha_devolucion: str | None, dias_retraso: int | None, activo: int) -> None:
        """
        Inicializa atributos en cero, None, cadena vacia
        """
        self._prestamo_id = prestamo_id
        self._socio_id = socio_id
        self._libro_id = libro_id
        self._fecha_prestamo = fecha_prestamo
        self._dias_pactados = dias_pactados
        self._activo = 1

        self._errores = ""
        self._fecha_devolucion = fecha_devolucion
        self._dias_retraso = dias_retraso

        self._socio = Socio
        self._libro = Libro

    def __str__(self) -> str:
        string = f"PrestamoID: {self._prestamo_id} | SocioID: {self._socio_id} | LibroID: {self._libro_id} | " \
                 f"Fecha Prestamo: {self._fecha_prestamo} | Dias Pactados: {self._dias_pactados} | " \
                 f"Fecha Devolucion: {self._fecha_devolucion} | " \
                 f"Dias Retraso: {self._dias_retraso} | Activo: {self.es_activo()} -"

        return string

    @property
    def prestamo_id(self):
        return self._prestamo_id

    '''    @prestamo_id.setter
    def socio(self, valor):
        self._prestamo_id = valor'''

    @property
    def socio_id(self):
        return self._socio_id

    @property
    def libro_id(self):
        return self._libro_id

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def dias_pactados(self):
        return self._dias_pactados

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @property
    def dias_retraso(self):
        return self._dias_retraso

    @property
    def activo(self):
        return self._activo

    @property
    def socio(self):
        return self._socio

    @property
    def errores(self):
        return self._errores

    @socio.setter
    def socio(self, valor: Socio):
        self._socio = valor

    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, valor: Libro):
        self._libro = valor

    def es_activo(self) -> str:
        """
        Activo =1 "SI".
        Borrado =0 "NO"
        """
        aux = "SI"
        if self._activo == 0:
            aux = "NO"
        return aux

    # para saber si los datos del objeto son consistentes con las reglas de negocio y se puede guardar en la base de
    # datos guarda los errores en el atributo errores. Se consulta con objeto.errores
    def is_check(self) -> bool:
        """
        Valida si los datos del objeto son consistentes. Usar Property .errores para conocer errores
        """
        flag = True
        if self.prestamo_id < 0:
            self._errores += "-Prestamo ID debe ser positivo \n"
            flag = False
        if self.socio_id < 0:
            self._errores += "-Socio ID debe ser positivo \n"
            flag = False
        if self.libro_id < 0:
            self._errores += "-Libro ID debe ser positivo \n"
            flag = False

        if len(self.fecha_prestamo) != 10:
            self._errores += "-Fecha de Prestamo debe ser 'AAAA-MM-DD' 10 caracteres\n"
            flag = False

        fecharray = self.fecha_prestamo.split("-")
        if len(fecharray) != 3:
            flag = False
            self._errores += "-Fecha de Prestamo debe ser 'AAAA-MM-DD' separada con - \n"

        if len(fecharray) == 3:
            if not (len(fecharray[0]) == 4) & (len(fecharray[1]) == 2) & (len(fecharray[2]) == 2):
                flag = False
                self._errores += "-Fecha de Prestamo debe ser 'AAAA-MM-DD' Año 4 digitos, Mes 2 digitos, " \
                                 "Dia 2 digitos \n"

                # fecha se puede validar periodo o rango de fechas

        if self.dias_pactados < 0:
            self._errores += "-Dias Pactados debe ser positivo \n"
            flag = False

        if self._fecha_devolucion is not None:
            if len(self._fecha_devolucion) != 10:
                self._errores += "-Fecha de Devolucion debe ser yyyy-mm-dd \n"
                flag = False
                # fecha se puede validar periodo o rango de fechas

        if self._fecha_devolucion is not None:
            if self._dias_retraso < 0:
                self._errores += "-Dias de Retraso debe ser positivo \n"
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
