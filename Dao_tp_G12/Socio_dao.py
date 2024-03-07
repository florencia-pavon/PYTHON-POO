from Socio import Socio
from db_singleton import DBConection
from typing import List
from Prestamo import Prestamo
DB = "biblitecaDB.sqlite"


class SocioDao:
    @staticmethod
    def obtener_todos() -> Socio:
        """
      Obtiene todos los Socios, Activos y Borrados. Devuelve Array. 
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from socios")
        resultado = cursor.fetchall()
        cursor.close()
        return map_a_objeto(resultado)

    @staticmethod
    def buscar_id(id: int) -> Socio:
        """
      Busca Socio por ID y devuelve array. Si no Existe devuelve array vacio.
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Socios where Socio_id=?", (id,))
        resultado = cursor.fetchall()
        cursor.close()
        return map_a_objeto(resultado)

    def agregar(self, nuevo: Socio) -> List[Socio]:
        """
      Recibe Objeto Socio. 
      Chequea validez de datos si es True guarda en DB y devuelve Objeto Socio. 
      Sino devuelve None   
      """
        buscado = None
        if nuevo.is_check:
            conn = DBConection(DB)
            cursor = conn.cursor()
            aux = (nuevo.apellido, nuevo.nombre, nuevo.email, nuevo.celular)
            cursor.execute("insert into Socios (apellido, nombre, email, celular) values(?,?,?,?) returning Socio_id"
                           , aux)
            id = cursor.fetchall()
            conn.commit()
            # print(f"   ID:  {id[0][0]} ")
            cursor.close()
            buscado = self.buscar_id(id[0][0])
        return buscado[0]

    def modificar(self, nuevo: Socio) -> Socio:
        """
      Recibe Objeto Socio. 
      Chequea validez de datos si es True y existe ID actualiza en DB y devuelve Objeto Socio. 
      Si es False o no existe devuelve None   
      """
        modificado = None
        existe = self.buscar_id(nuevo.socio_id)
        if len(existe) == 1 & nuevo.is_check():
            conn = DBConection(DB)
            cursor = conn.cursor()
            aux = (nuevo.apellido, nuevo.nombre, nuevo.email, nuevo.celular, nuevo.activo, nuevo.socio_id)
            query = "update Socios set apellido=?, nombre=?, email=?, celular=? , activo=? where Socio_id=? "
            cursor.execute(query, aux)
            conn.commit()
            buscado = self.buscar_id(nuevo.socio_id)
            # for x in buscardo:
            #   print(x)
            modificado = buscado[0]
            cursor.close()
        return modificado

    def eliminar(self, id: int) -> Socio:
        """
      Recibe id:int. 
      Busca existencia de id en BD. Si existe ID actualiza en DB atributo activo=0 y devuelve Objeto Socio. 
      Si no existe devuelve None 
      """
        respuesta = None
        existe = self.buscar_id(id)
        if len(existe) == 1:
            query = "update Socios set activo=0 where Socio_id=? "
            conn = DBConection(DB)
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            existe = self.buscar_id(id)
            respuesta = existe[0]
        return respuesta

    @staticmethod
    def obtener_activos() -> List[Socio]:
        """
      Buscar Socio activos y devuelve array. Si no Existe devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Socios where activo=1")
        resultado = cursor.fetchall()
        cursor.close()
        return map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    @staticmethod
    def obtener_inactivos() -> List[Socio]:
        """
      Buscar Socio NO activos y devuelve array. Si no Existe devuelve array vacio.   
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        cursor.execute("select * from Socios where activo=0")
        resultado = cursor.fetchall()
        cursor.close()
        return map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    @staticmethod
    def buscar_apellido(apell: str) -> List[Socio]:
        """
      Busca Socios por Apellido que esten activos. Si existen dedevuelve array. Sino array vacio
      """
        conn = DBConection(DB)
        cursor = conn.cursor()
        query = f"select * from Socios where apellido like '%{apell}%' and activo=1"
        # print(query)
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        return map_a_objeto(resultado)  # mapear todos= map_a_objeto(resultado)

    @staticmethod
    def buscar_nombre(nom: str) -> List[Socio]:
        """
      Busca Socios por Nombre que esten activos. Si existen dedevuelve array. Sino array vacio
      """
        resultado = None
        conn = DBConection(DB)
        cursor = conn.cursor()
        query = f"select * from Socios where nombre like '%{nom}%' and activo=1"
        # print(query)
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        socios = map_a_objeto(resultado)
        return socios  # mapear todos= map_a_objeto(resultado)

    def prestamo_por_socio(self, socio_id: int) -> List[Prestamo]:
        resultado = []
        conn = DBConection(DB)
        cursor = conn.cursor()
        query = f"SELECT * FROM Prestamos WHERE socio_id=?"

        try:
            cursor.execute(query, (socio_id,))

            for row in cursor.fetchall():
                prestamo = Prestamo(
                    row[0],  # prestamo_id
                    row[1],  # socio_id
                    row[2],  # libro_id
                    row[3],  # fecha_prestamo
                    row[4],  # dias_pactados
                    row[5],  # fecha_devolucion
                    row[6],  # dias_retraso
                    row[7]  # activo
                )
                resultado.append(prestamo)
        except Exception as e:
            print(f"Error al recuperar prestamos por socio: {e}")

        return resultado


def map_a_objeto(resultado: List[tuple]) -> List[Socio]:
    todos = []
    for fila in resultado:
        aux = Socio(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]))
        todos.append(aux)
    return todos
