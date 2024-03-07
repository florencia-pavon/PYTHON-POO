#from socio_dao import *

from Socio import Socio
from Socio_dao import SocioDao

dao=SocioDao()


def test_socio():
   print()
   print()
   print("##############   INICIO TEST SOCIO   ##############")
   print()  
   # BUSCAR UNO POR ID

   print("           TEST SOCIO DAO 01 - BUSCAR POR ID =1")
   aa=dao.buscar_id(1)
   print(aa[0])
   print("\n")

   # BUSCAR TODOS

   print("           TEST SOCIO DAO 02 - BUSCAR TODOS")
   aa=dao.obtener_todos()
   for l in aa:
      print(l)
   print("\n")


   #MODIFICAR POR ID

   print("           TEST SOCIO DAO 03- MODIFICAR POR ID")
   print("VERSION PREVIA: Socio(5,'TEST Editar','Test', 'tt@mail.com', '9569', 1)")
   print("Socio(5,'@Ape Editado','@Nom Editado', '@Editado@mail.com', '@Editado', 1)")
   aa=Socio(5,'@Ape Editado','@Nom Editado', '@Editado@mail.com', '@Editado', 1)
   #print (aa)
   resp= dao.modificar(aa)
   print(resp)
   print("\n")

   # AGREGAR
  
   print("           TEST SOCIO DAO 04 - AGREGAR ")
   print("creo y guardo Socio(0,'TEST AGREGAR','Nombre Agregado', 'tt@mail.com', '78962',1 ) " )
   print ("busco y muestro socio creado")

   aa=Socio(0,'TEST AGREGAR','Test Nombre Agregado', 'tt@mail.com', '78962',1 )
   resp=dao.agregar(aa)
   print(resp.__str__())
   print("\n")
   

   #ELIMINAR POR ID CASO QUE EXISTE
   
   print("           TEST SOCIO DAO 05 - ELIMINAR POR ID=5 ()")
   print(" ACTUALIZAR ATRIBUTO ACTIVO COMO 0 Y DEVUELVE OBJETO SOCIO ")
   print("EXITO SOCIO EXISTE")
   resp=dao.eliminar(5)
   print(resp.__str__())
   print("\n")
   
   #ELIMINAR POR ID CASO QUE NO EXISTE
   
   print("           TEST SOCIO DAO 06 - ELIMINAR POR ID=8000 ")
   print(" ACTUALIZAR ATRIBUTO ACTIVO COMO 0 Y DEVUELVE OBJETO SOCIO ")
   print(" (FRACASO NO EXISTE)")
   resp=dao.eliminar(8000)
   print(resp.__str__())
   print("\n")   
  
     
   # BUSCAR SOCIOS ACTIVOS

   print("           TEST SOCIO DAO 07 - BUSCAR SOCIOS ACTIVOS ")
   resp=dao.obtener_activos()
   for x in resp:
      print(x)
   print("\n")

   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO SOCIO
   # EJEMPLO SOCIO CORRECTO
   print("           TEST SOCIO DAO 08 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO SOCIO")
   print(" Socio correcto -> true")
   print("Socio(10,'aaaa', 'bbbbb', 'ccccc','ddddd',1 )")
   aa=Socio(10,'aaaa', 'bbbbb', 'ccccc','ddddd',1 )
   print (aa.is_check())
   print(aa.errores)
   print("\n")
   
   
   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO SOCIO
   # EJEMPLO SOCIO INCORRECTO
   print("           TEST SOCIO DAO 09 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO SOCIO")
   print(" SOCIO NO correcto -> False")
   print("Socio(-10,,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccc','ddddddddddddddddddddddddddddddddddddddddddddddddddd' ,4 )")
   aa=Socio(-10,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccc','ddddddddddddddddddddddddddddddddddddddddddddddddddd' ,4 )
   print (aa.is_check())
   print(aa.errores)
   print("\n")
   

   print("           TEST SOCIO DAO 10 - BUSCAR SOCIOS NO ACTIVOS  / BORRADOS")
   resp=dao.obtener_inactivos()
   for x in resp:
      print(x)
   print("\n")

   
   print("           TEST SOCIO DAO 11 - BUSCAR SOCIOS POR APELLIDO")
   print("(EXITO) buscar_apellido('t')  MUESTRA socio 3 y 7") 
   resp= dao.buscar_apellido("t")
   for x in resp:
      print(x)
   print("\n")
  
   
   print("           TEST SOCIO DAO 12 - BUSCAR SOCIOS POR APELLIDO")
   print("(FRACASO) buscar_titulo('x')  muestra array vacio") 
   resp= dao.buscar_apellido("x")
   print(resp)
   print("\n")
  
   
   print("           TEST SOCIO DAO 13 - BUSCAR SOCIOS POR NOMBRE")
   print("(EXITO) buscar_nombre('u')  MUESTRA socio 1") 
   resp= dao.buscar_nombre("u")
   for x in resp:
      print(x)
   print("\n")
  
   
   print("           TEST SOCIO DAO 14 - BUSCAR SOCIOS POR NOMBRE")
   print("(FRACASO) buscar_nombre('z')  muestra array vacio") 
   resp= dao.buscar_nombre("z")
   print(resp)
   print("\n")  


   print()
   print("##############   FIN TEST SOCIO   ##############")
   print()
   

test_socio()


