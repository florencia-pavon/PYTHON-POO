# import sqlite3

from Libro import Libro
from db_singleton import DBConection

DB = "biblitecaDB.sqlite"


class LibroDao:

    def obtener_todos(self) -> Libro:
        """
      Obtiene todos los Libros, Activos y Borrados. Devuelve Array 
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def buscar_id(self, id: int) -> Libro:
        """
      Busca Libro por ID y devuelve array. Si no Existe devuelve array vacio.
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where libro_id=?", (id,))
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)

    def agregar(self, nuevo: Libro) -> Libro:
        """
      Recibe Objeto Libro. 
      Chequea validez de datos si es True guarda en DB y devuelve Objeto Libro. 
      Sino devuelve None   
      """
        buscado = None
        if nuevo.is_check():
            conn = DBConection(DB)
            cursor = conn.cursor()
            aux = (nuevo.titulo, nuevo.precio_reposicion, nuevo.estado_id)
            cursor.execute("insert into libros (titulo, precio_reposicion, estado_id) values(?,?,?) returning libro_id",
                           aux)
            id = cursor.fetchall()
            conn.commit()
            # print(f"   ID:  {id[0][0]} ")
            cursor.close()
            buscado = self.buscar_id(id[0][0])
        return buscado[0]

    def modificar(self, nuevo: Libro) -> Libro:
        """
      Recibe Objeto Libro. 
      Chequea validez de datos si es True y existe ID actualiza en DB y devuelve Objeto Libro. 
      Si es False o no existe devuelve None   
      """
        modificado = None
        existe = self.buscar_id(nuevo.libro_id)
        if len(existe) == 1 & nuevo.is_check():
            conn = DBConection(DB)
            cursor = conn.cursor()
            aux = (nuevo.titulo, nuevo.precio_reposicion, nuevo.estado_id, nuevo.activo, nuevo.libro_id)
            query = "update libros set titulo=?, precio_reposicion=?, estado_id=?, activo=? where libro_id=? "
            cursor.execute(query, aux)
            conn.commit()
            buscado = self.buscar_id(nuevo.libro_id)
            # for x in buscardo:
            #   print(x)
            modificado = buscado[0]
            cursor.close()
        return modificado

    def eliminar(self, id: int) -> Libro:
        """
      Recibe id:int. 
      Busca existencia de id en BD. Si existe ID actualiza en DB atributo activo=0 y devuelve Objeto Libro. 
      Si no existe devuelve None 
      """
        respuesta = None
        existe = self.buscar_id(id)
        if len(existe) == 1:
            query = "update libros set activo=0 where libro_id=? "
            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            existe = self.buscar_id(id)
            respuesta = existe[0]
        return respuesta

    def map_a_objeto(self, resultado) -> Libro:
        todos = []
        for fila in resultado:
            # aux=Libro(fila[0],fila[1],fila[2],fila[3],,int(fila[4]))
            aux = Libro(int(fila[0]), fila[1], round(float(fila[2]), 2), int(fila[3]), int(fila[4]))
            todos.append(aux)
            # print(aux)
            # print(fila)

        return todos

    def obtener_activos(self) -> Libro:
        """
      Buscar Libro activos y devuelve array. Si no Existe devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where activo=1")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def obtener_inactivos(self) -> Libro:
        """
      Buscar Libro NO activos y devuelve array. Si no Existe devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where activo=0")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    def buscar_titulo(self, titulo: str) -> Libro:
        """
      Busca Libros por Titulo que esten activos. Si existen dedevuelve array. Sino array vacio
      """
        resultado = None
        conn = DBConection(DB)
        cursor = conn.cursor()
        query = f"select * from libros where titulo like '%{titulo}%' and activo=1"
        # print(query)
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    #  REGISTRAR LIBROS EXTRAVIADOS
    def registar_extravio(self, id: int) -> Libro:
        """
      Recibe id:int. 
      Busca existencia de id en BD. Si existe ID actualiza en DB atributo estado_id=3 y activo=0. Devuelve Objeto Libro. 
      Si no existe devuelve None 
      """
        respuesta = None
        existe = self.buscar_id(id)
        if len(existe) == 1:
            query = "update libros set estado_id=3, activo=0  where libro_id=? "
            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            existe = self.buscar_id(id)
            respuesta = existe[0]
        return respuesta

    #  REGISTRAR LIBRO DISPONIBLE
    def registar_disponible(self, id: int) -> Libro:
        """
      Recibe id:int. 
      Busca existencia de id en BD. Si existe ID actualiza en DB atributo estado_id=1. Devuelve Objeto Libro. 
      Si no existe devuelve None 
      """
        respuesta = None
        existe = self.buscar_id(id)
        if len(existe) == 1:
            query = "update libros set estado_id=1 where libro_id=? "
            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            existe = self.buscar_id(id)
            respuesta = existe[0]
        return respuesta

    #  REGISTRAR LIBRO PRESTADO
    def registar_prestado(self, id: int) -> Libro:
        """
      Recibe id:int. 
      Busca existencia de id en BD. Si existe ID actualiza en DB atributo estado_id=2. Devuelve Objeto Libro. 
      Si no existe devuelve None 
      """
        respuesta = None
        existe = self.buscar_id(id)
        if len(existe) == 1:
            query = "update libros set estado_id=2 where libro_id=? "
            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            existe = self.buscar_id(id)
            respuesta = existe[0]
        return respuesta

    #  LISTAR LIBROS DISPONIBLES
    def obtener_libros_disponibles(self) -> Libro:
        """
      Buscar Libros disponibles y activos, devuelve array. Si no Existen devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where estado_id=1 and activo=1")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    #  LISTAR LIBROS PRESTADOS
    def obtener_libros_prestados(self) -> Libro:
        """
      Buscar Libros prestados y activos, devuelve array. Si no Existen devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where estado_id=2 and activo=1")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    #  LISTAR LIBROS EXTRAVIADOS
    def obtener_libros_extraviados(self) -> Libro:
        """
      Buscar Libros extraviados y devuelve array. Si no Existen devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from libros where estado_id=3")
        resultado = cursor.fetchall()
        cursor.close()
        return self.map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    # Cantidad de libros en cada estado (tres totales)  (disponible, prestado o extraviado).
    def libros_por_estado(self) -> dict:
        """
      REPORTE: Cantidad de libros en cada estado (tres totales)  (disponible, prestado o extraviado).
      """
        query1 = "select count(estado_id) from libros where estado_id=1"
        query2 = "select count(estado_id) from libros where estado_id=2"
        query3 = "select count(estado_id) from libros where estado_id=3"
        querytodos = "select count(estado_id) from libros "

        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(querytodos)
        todos = cursor.fetchall()

        cursor.execute(query1)
        disponible = cursor.fetchall()

        cursor.execute(query2)
        prestado = cursor.fetchall()

        cursor.execute(query3)
        extraviado = cursor.fetchall()

        cursor.close()
        return {"todos": todos[0][0], "disponible": disponible[0][0], "prestado": prestado[0][0],
                "extraviado": extraviado[0][0]}

    # Sumatoria del precio de reposición de todos los libros extraviados
    def costo_libros_extraviados(self) -> dict:
        """
      REPORTE: Sumatoria del precio de reposición de todos los libros extraviados
      """
        query = "select round(sum(precio_reposicion),2) from libros where estado_id=3"
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute(query)
        total = cursor.fetchall()
        cursor.close()
        return {"total": total[0][0]}
