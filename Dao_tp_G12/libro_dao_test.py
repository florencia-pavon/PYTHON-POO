from libro import Libro
from Libro_dao import LibroDao

dao=LibroDao() 

def test_libro():
   
   print()
   print()
   print("##############   INICIO TEST LIBRO   ##############")
   print()  
   
   # BUSCAR UNO POR ID
   print("           TEST LIBRO DAO 01 - BUSCAR POR ID =1")
   aa=dao.buscar_id(1)
   print(aa[0])
   print("\n")

   # BUSCAR TODOS
   print("           TEST LIBRO DAO 02 - BUSCAR TODOS")
   aa=dao.obtener_todos()
   for l in aa:
      print(l)
   print("\n")


   #MODIFICAR POR ID

   print("           TEST LIBRO DAO 03- MODIFICAR POR ID")
   aa=Libro(8,'aXQasQQQ', 1239.45, 3, 1)
   print (aa)
   resp= dao.modificar(aa)
   print(resp)
   print("\n")

   # AGREGAR
   
   print("           TEST LIBRO DAO 04 - AGREGAR ")
   print("creo y guardo Libro(0,'TEST 2', 12.45, 1,1 ) " )
   print ("busco y muestro libro creado")

   aa=Libro(0,'TEST 2', 12.45, 1,1 )
   resp=dao.agregar(aa)
   print(resp.__str__())
   print("\n")
  
   #ELIMINAR POR ID CASO QUE EXISTE
   
   print("           TEST LIBRO DAO 05 - ELIMINAR POR ID=8 ()")
   print(" ACTUALIZAR ATRIBUTO ACTIVO COMO 0 Y DEVUELVE OBJETO LIBRO ")
   print("EXITO LIBRO EXISTE")
   resp=dao.eliminar(8)
   print(resp.__str__())
   print("\n")
   
   #ELIMINAR POR ID CASO QUE NO EXISTE
   
   print("           TEST LIBRO DAO 06 - ELIMINAR POR ID=8000 ")
   print(" ACTUALIZAR ATRIBUTO ACTIVO COMO 0 Y DEVUELVE OBJETO LIBRO ")
   print(" (FRACASO NO EXISTE)")
   resp=dao.eliminar(8000)
   print(resp.__str__())
   print("\n")     
   # BUSCAR LIBROS ACTIVOS

   print("           TEST LIBRO DAO 07 - BUSCAR LIBROS ACTIVOS ")
   resp=dao.obtener_activos()
   for x in resp:
      print(x)
   print("\n")

   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO LIBRO
   # EJEMPLO LIBRO CORRECTO
   print("           TEST LIBRO DAO 08 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO LIBRO")
   print(" Libro correcto -> true")
   print("Libro(10,'aaaa', 12.45, 3,1 )")
   aa=Libro(10,'aaaa', 12.45, 3,1 )
   print (aa.is_check())
   print(aa.errores)
   print("\n")
   
   
   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO LIBRO
   # EJEMPLO LIBRO INCORRECTO
   print("           TEST LIBRO DAO 09 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO LIBRO")
   print(" Libro NO correcto -> False")
   print("Libro(-10,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', -12.45, -3,1 )")
   aa=Libro(-10,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', -12.45, -3,1 )
   print (aa.is_check())
   print(aa.errores)
   print("\n")
   

   print("           TEST LIBRO DAO 10 - BUSCAR LIBROS NO ACTIVOS  / BORRADOS")
   resp=dao.obtener_inactivos()
   for x in resp:
      print(x)
   print("\n")

   
   print("           TEST LIBRO DAO 11 - BUSCAR LIBROS POR TITULO")
   print(" buscar_titulo('t')  MUESTRA MATEMATICA Y TEST") 
   resp= dao.buscar_titulo("t")
   for x in resp:
      print(x)
   print("\n")
   
   print("           TEST LIBRO DAO 12 - CONTAR LIBROS POR ESTADO")
   print(" REPORTE:  Cantidad de libros en cada estado (tres totales)  (disponible, prestado o extraviado).")   
   resp= dao.libros_por_estado()
   print(resp)
   print("\n")
   
   print("           TEST LIBRO DAO 13 - SUMAR COSTO LIBROS EXTRAVIADOS")
   print(" REPORTE:  Sumatoria del precio de reposición de todos los libros extraviados")   
   resp= dao.costo_libros_extraviados()
   print(resp)
   print("\n")
   
   print("           TEST LIBRO DAO 14 - REGISTRAR LIBROS EXTRAVIADOS")
   print(" REQUERIMIENTO:  Registración de libros extraviados")   
   print(" (EXITO SI EXISTE)")
   resp= dao.registar_extravio(10)
   print(resp)
   print("\n")
   
   print("           TEST LIBRO DAO 15 - REGISTRAR LIBROS EXTRAVIADOS")
   print(" REQUERIMIENTO:  Registración de libros extraviados")   
   print(" (FRACASO NO EXISTE id=10000)")
   resp= dao.registar_extravio(10000)
   print(resp)
   print("\n")
   
   
   print("           TEST LIBRO DAO 16 - LISTAR LIBROS EXTRAVIADOS")
   print(" REPORTE:  Listado de todos los libros extraviados")   
   resp= dao.obtener_libros_extraviados()
   for x in resp:
      print(x)
   print("\n")


   print()
   print("##############   FIN TEST LIBRO   ##############")
   print()   
   
   

test_libro()


