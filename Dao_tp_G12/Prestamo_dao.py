from Prestamo import Prestamo
from prestamo_error import PrestamoError
# import socio_dao
# import libro_dao
from Socio_dao import SocioDao
from Libro_dao import LibroDao
from db_singleton import DBConection
import datetime
from datetime import datetime
from typing import List


DB = "biblitecaDB.sqlite"

libro_dao = LibroDao()
socio_dao = SocioDao()


class PrestamoDao:

    def obtener_todos(self) -> Prestamo:
        """
        Obtiene todos los Prestamos, Activos y Eliminados. Devuelve Array 
        """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Prestamos")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def obtener_prestamos_activos(self) -> Prestamo:
        """
        Obtiene todos los Prestamos Activos. Devuelve Array 
        """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Prestamos where activo=1")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def obtener_prestamos_eliminados(self) -> Prestamo:
        """
        Obtiene todos los Prestamos Eliminados. Devuelve Array 
        """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Prestamos where activo=0")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def buscar_id(self, id: int) -> Prestamo:
        """
        Busca Prestamo por ID y devuelve array. Si no Existe devuelve array vacio.
        """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Prestamos where Prestamo_id=?", (id,))
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)

    # def buscar_id( id:int)->Prestamo: 
    # el metodo actualizar por id es reemplazado por otros metodos mas especificos al dominio
    #

    def registrar_prestamo(self, nuevo: Prestamo) -> Prestamo:
        """
        Recibe Objeto Prestamo. Cada Prestamo es Individual por libro. No tiene 'DETALLE' 
        Chequea validez de datos si es True guarda en DB y devuelve Objeto Prestamo. 
        Sino devuelve Objeto PrestamoError   
        """

        flag = True
        error = PrestamoError()
        aux = None
        respuesta = None
        query = ''
        fecha_hoy = datetime.now()  # FORMATO DATETIME
        fecha = datetime
        if nuevo.is_check():

            # VALIDAR FECHA
            try:
                fecha = datetime.strptime(nuevo.fecha_prestamo, '%Y-%m-%d')
                # print(f"Fecha Valida: {fecha} TRY OK ")
                if fecha_hoy < fecha:
                    flag = False
                    error._error += "-Fecha Prestamo debe ser Hoy como maximo  \n"
            except Exception as e:
                # print(f"fallo TRY ")
                flag = False
                error._error += "-Fecha Prestamo no es Valida \n"

                # validar claves foraneas
            # busco socio ID
            socio = socio_dao.buscar_id(nuevo.socio_id)
            # print(f"//// SOCIO LEN ***** {len(socio)}")
            # print(f"//// SOCIO ***** {socio[0]}")
            if len(socio) != 1:
                flag = False
                error._error += "-No existe Socio ID \n"

            if len(socio) == 1:

                # Valida que el socio no posea más de tres libros prestados (aunque todavía se encuentre dentro del
                # plazo del préstamo).
                if not self.is_prestamo_posible(
                        nuevo.socio_id):  # Valida que el socio no posea más de tres libros prestados (aunque todavía
                    # se encuentre dentro del plazo del préstamo).
                    flag = False
                    error._error += "-Socio ya tiene 3 libros prestados. No es apto para nuevo prestamo  \n"

                # Valida que el socio no posea ningún libro con demora en su devolución
                if not self.is_socio_cumplidor(nuevo.socio_id):
                    flag = False
                    error._error += "-Socio ya tiene prestados con demora en su devolución. No es apto para nuevo " \
                                    "prestamo  \n"

            # busco libro ID
            libro = libro_dao.buscar_id(nuevo.libro_id)
            # print(libro[0]) #
            if len(libro) != 1:
                flag = False
                error._error += "-No existe Libro ID \n"
            # busco libro disponible
            if libro[0]._estado_id != 1:
                flag = False
                error._error += "-El Libro no esta 'Disponible' para prestamo \n"

            # FIN DE VALIDACIONES
            if not flag:
                return error

            aux = (
                nuevo.socio_id, nuevo.libro_id, nuevo.fecha_prestamo, nuevo.dias_pactados, nuevo.fecha_devolucion,
                nuevo.dias_retraso, nuevo.activo)
            query = " insert into prestamos (socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) values(?,?,?,?,?,?,?) returning prestamo_id"

            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, aux)
            id = cursor.fetchall()
            # print(f"   ID:  {id[0][0]} ")
            conn.commit()
            cursor.close()
            print('llego db')
            prestado = libro_dao.registar_prestado(libro[0].libro_id)
            # print (prestado)
            buscado = self.buscar_id(id[0][0])
            # print (f"////// BUSCADO @@@@@  {buscado[0]}")
            respuesta = buscado[0]

        else:
            # print("############ ELSE")
            return nuevo.errores

        return respuesta

    def eliminar(self, id: int) -> Prestamo:
        """
        Recibe PrestamoID del prestamo para baja logica.
        Chequea validez de datos si es True guarda en DB y devuelve Objeto Prestamo. 
        Sino devuelve Objeto PrestamoError   
        """
        flag = True
        error = PrestamoError()
        respuesta = None
        prestamo = Prestamo
        query = ''
        aux = None

        # INICIO VALIDACIONES
        if id <= 0:
            flag = False
            error._error += "-El prestamo ID debe ser mayor a cero \n"

        existe = self.buscar_id(id)
        # print(len(existe))
        # print(existe[0])

        if len(existe) != 1:
            flag = False
            error._error += "-No se encontro el prestamo ID \n"

        if len(existe) == 1:
            prestamo = existe[0]
            # print(prestamo)
            if prestamo.fecha_devolucion != None:
                flag = False
                error._error += "-No se puede registrar Devolucion. Prestamo ya Devuelto \n"

                # FIN VALIDACIONES
        if not flag:
            return error

        aux = self.registrar_devolucion(id, prestamo.fecha_prestamo)
        query = "update prestamos set activo=0 where prestamo_id=? "
        # print (f"////// Prestamo devuelto @@@@@  {aux}")

        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        buscado = self.buscar_id(id)
        # print (f"////// BUSCADO @@@@@  {buscado[0]}")
        respuesta = buscado[0]

        return respuesta

    def registrar_devolucion(self, id: int, fecha: str) -> Prestamo:
        """
        Recibe PrestamoID y Fecha Devolucion.
        Chequea validez de datos si es True guarda en DB y devuelve Objeto Prestamo. 
        Sino devuelve Objeto PrestamoError   
        """
        flag = True
        error = PrestamoError()
        fecharray = None
        fecha_devolucion = None
        # fecha_hoy=datetime.strftime(datetime.now(), '%Y-%m-%d') #EN FORMATO STRING
        # fecha_hoy=datetime.now() #FORMATO DATETIME
        # print(f"fecha_hoy: {fecha_hoy} ")
        respuesta = None
        prestamo = Prestamo
        query = ''
        aux = None

        # INICIO DE VALIDACIONES
        if len(fecha) != 10:
            flag = False
            error._error += "-Fecha debe ser 'AAAA-MM-DD' 10 caracteres \n"

        fecharray = fecha.split("-")
        if len(fecharray) != 3:
            flag = False
            error._error += "-Fecha debe ser 'AAAA-MM-DD' separada con - \n"

        if len(fecharray) == 3:
            if not (len(fecharray[0]) == 4) & (len(fecharray[1]) == 2) & (len(fecharray[2]) == 2):
                flag = False
                error._error += "-Fecha debe ser 'AAAA-MM-DD' Año 4 digitos, Mes 2 digitos, Dia 2 digitos \n"

        if id <= 0:
            flag = False
            error._error += "-El prestamo ID debe ser mayor a cero \n"
        try:
            fecha_devolucion = datetime.strptime(fecha, '%Y-%m-%d')
            # print(f"Fecha Valida: {fecha7} TRY OK ")
        except Exception as e:
            # print(f"fallo TRY ")
            flag = False
            error._error += "-Fecha no es Valida \n"

        existe = self.buscar_id(id)
        # print(len(existe))
        # print(existe[0])

        if len(existe) != 1:
            flag = False
            error._error += "-No se encontro el prestamo ID \n"

        if len(existe) == 1:
            prestamo = existe[0]
            # print(prestamo)
            if prestamo.fecha_devolucion is not None:
                flag = False
                error._error += "-No se puede registrar Devolucion. Prestamo ya Devuelto \n"

            if fecha_devolucion != None:
                fecha_prestamo = datetime.strptime(prestamo.fecha_prestamo, '%Y-%m-%d')
                # print(f"fecha_prestamo: {fecha_prestamo}")
                if fecha_devolucion < fecha_prestamo:
                    flag = False
                    error._error += "-Fecha de devolucion debe ser mayor que fecha del prestamo \n"

                    # FIN VALIDACIONES
        if not flag:
            return error

        # REGISTAR DEVOLUCION
        diferencia = fecha_devolucion - fecha_prestamo
        # print(diferencia)
        dif_dias = diferencia.days
        # print(f"dif_dias: {dif_dias}")
        if prestamo.dias_pactados < dif_dias:
            # print(f"prestamo.dias_pactados: {prestamo.dias_pactados}")
            retraso = dif_dias - prestamo.dias_pactados
            query = "update prestamos set fecha_devolucion=?, dias_retraso=? where prestamo_id=? "
            aux = (fecha, retraso, id)
        else:
            query = "update prestamos set fecha_devolucion=?, dias_retraso=0 where prestamo_id=? "
            aux = (fecha, id)

        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(query, aux)
        conn.commit()
        cursor.close()
        libro = libro_dao.registar_disponible(prestamo.libro_id)
        # print (libro)
        buscado = self.buscar_id(id)
        # print (f"////// BUSCADO @@@@@  {buscado[0]}")
        respuesta = buscado[0]

        return respuesta

    def is_prestamo_posible(self, socioID: int) -> bool:
        '''
        TRUE -> Socio apto para nuevo prestamo. FALSE no apto.
        Valida que el socio no posea más de tres libros prestados (aunque todavía se encuentre dentro del plazo del préstamo).       
        '''
        respuesta = True
        query = "select * from prestamos where socio_id=? and fecha_devolucion is null  "

        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(query, (socioID,))
        resultado = cursor.fetchall()
        cursor.close()
        aux = self.map_a_objeto(resultado)
        if len(aux) >= 3:
            respuesta = False

        return respuesta

    def is_socio_cumplidor(self, socio_id: int) -> bool:
        """
        TRUE -> Socio apto para nuevo prestamo. FALSE no apto.
        Valida que el socio no posea ningún libro con demora en su devolución.
        """
        respuesta = True
        resultado = self.obtener_prestamos_demorados()
        for x in resultado:
            if x.socio_id == socio_id:
                respuesta = False
                # print(x)
        return respuesta

    def obtener_prestamos_demorados(self) -> Prestamo:
        """
        REPORTE: Listado de préstamos demorados.
        Devuelve Array de prestamos
        """
        fecha_hoy = datetime.now()
        respuesta = []
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from prestamos where fecha_devolucion is null  ")
        resultado = cursor.fetchall()
        cursor.close()
        aux = self.map_a_objeto(resultado)
        for x in aux:
            # print(x)
            fecha_prestamo = datetime.strptime(x.fecha_prestamo, '%Y-%m-%d')
            diferencia = fecha_hoy - fecha_prestamo
            # print(diferencia)
            dias = diferencia.days
            if x.dias_pactados < dias:
                respuesta.append(x)
                # print(x)

        return respuesta

    def obtener_prestamos_demorados_30dias(self) -> Prestamo:
        """
        REPORTE: Listado de préstamos demorados mas de 30 dias.
        Devuelve Array de prestamos
        """
        fecha_hoy = datetime.now()
        respuesta = []

        aux = self.obtener_prestamos_demorados()
        for x in aux:
            # print(x)
            fecha_prestamo = datetime.strptime(x.fecha_prestamo, '%Y-%m-%d')
            diferencia = fecha_hoy - fecha_prestamo
            # print(diferencia)
            dias = diferencia.days
            if dias >= 30:
                respuesta.append(x)
                # print(x)

        return respuesta

    @staticmethod
    def obtener_socios_titulo(titulo: str) -> Prestamo:
        """
        REPORTE: Listado de Nombre de todos los solicitantes de un libro en particular identificado por su título.
        Devuelve Array de Apellido, Nombre de Socios
        """
        # select (s.apellido|| ',  '|| s.nombre) as 'Apellido, Nombre' from prestamos p join socios s on
        # p.socio_id=s.socio_id join libros l on p.libro_id=l.libro_id where l.titulo like'matematica i' group by (
        # s.apellido|| ',  '|| s.nombre);
        query = "select (s.apellido|| '  '|| s.nombre) as 'Apellido, Nombre' from prestamos p join socios s on p.socio_id=s.socio_id join libros l on p.libro_id=l.libro_id where l.titulo like ?  group by (s.apellido|| ',  '|| s.nombre) "

        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(query, (titulo,))
        resultado = cursor.fetchall()
        cursor.close()
        respuesta = []
        for x in resultado:
            # print(x)
            respuesta.append(x[0])

        return respuesta

    def obtener_prestamos_de_socio(self, socio_id: int) -> Prestamo:
        """
        REPORTE: Listado de préstamos de un socio identificado por su número de socio.
        Devuelve Array de prestamos
        """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from prestamos where socio_id=? ", (socio_id,))
        resultado = cursor.fetchall()
        cursor.close()

        return self.map_a_objeto(resultado)

    def registrar_libros_extraviados(self):
        respuesta = []
        aux = self.obtener_prestamos_demorados_30dias()
        for x in aux:
            lib = libro_dao.registar_extravio(x.libro_id)
            respuesta.append(lib)

        return respuesta

    def prestamos_demorados(self) -> List[Prestamo]:
        """
        Retorna una lista de préstamos demorados.
        """
        fecha_actual = datetime.now()
        try:
            with DBConection(DB) as conn:
                cursor = conn.cursor()
                query = f"SELECT * FROM prestamos WHERE fecha_devolucion IS NULL AND fecha_prestamo + dias_pactados < '{fecha_actual}'"
                prestamos_demorados = cursor.execute(query).fetchall()

                prestamos = [self.map_a_objeto(prestamo) for prestamo in prestamos_demorados]

                return prestamos

        except Exception as e:
            print(f"Error al obtener préstamos demorados: {e}")
            return []

    @staticmethod
    def map_a_objeto(resultado) -> Prestamo:
        todos = []
        for fila in resultado:
            # aux=Prestamo(int(fila[0]),int(fila[1]),int(fila[2]),fila[3],int(fila[4]),fila[5],int(fila[6]),int(fila[7]))
            # aux=Prestamo(int(fila[0]),int(fila[1]),int(fila[2]),fila[3],int(fila[4]),int(fila[7]))
            if fila[6] is None:
                dias_retraso = fila[6]
            else:
                dias_retraso = int(fila[6])
            aux = Prestamo(
                prestamo_id=int(fila[0]),
                socio_id=int(fila[1]),
                libro_id=int(fila[2]),
                fecha_prestamo=fila[3],
                dias_pactados=int(fila[4]),
                fecha_devolucion=fila[5],
                dias_retraso=dias_retraso,
                activo=int(fila[7]))
            todos.append(aux)
            # print(aux)
            # print(fila)

        return todos
