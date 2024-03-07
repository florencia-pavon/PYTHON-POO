from Prestamo import Prestamo
from Prestamo_dao import PrestamoDao

dao=PrestamoDao()

def test_prestamo():
   
   print()
   print()
   print("##############   INICIO TEST PRESTAMO   ##############")
   print()  
   
  
   # BUSCAR UNO POR ID
   print("           TEST PRESTAMO DAO 01 - BUSCAR POR ID =1")
   aa=dao.buscar_id(1)
   print(aa[0])
   print("\n")

   # BUSCAR TODOS
   print("           TEST PRESTAMO DAO 02 - BUSCAR TODOS")
   aa=dao.obtener_todos()
   for l in aa:
      print(l)
   print("\n")

   
   print("           TEST PRESTAMO DAO 03 - REGISTRAR NUEVO PRESTAMO 'BASICO'  ")
   print(" ******** CASO EXITOSO  ******" )
   print("creo y guardo Prestamo Basico  aa.init_basico(0,5,1,'2023-10-25', 5 ) " )
   print ("busco y muestro Prestamo creado")
   aa=Prestamo()
   #print(f"Objeto Vacio: ")
   #print(aa)   
   aa.init_basico(0,5,1,'2023-10-25',5 )
   #print(f"Objeto:")  
   #print(aa)     
   resp=dao.registrar_prestamo(aa)
   print(resp)
   print("\n")

   
   print("           TEST PRESTAMO DAO 04 - REGISTRAR NUEVO PRESTAMO 'BASICO'  ")
   print(" ******** CASO FRACASO  ******" )
   print("creo y guardo Prestamo Basico  aa.init_basico(0,-1,-1,'2023-11-35',-5 ) " )
   print ("busco y muestro Prestamo creado")
   aa=Prestamo()
   print(aa)   
   aa.init_basico(0,-1,-1,'2023-11-35',-5 )
   print(aa)     
   #print (f"IS_CHECK??? {aa.is_check()}")
   #print(f"ERRORES: {aa.errores}")
   resp=dao.registrar_prestamo(aa)
   print(f"RESULTADO DE REGISTRO \n {resp}")
   print("\n")   
   
   
   print("           TEST PRESTAMO DAO 05 - REGISTRAR PRESTAMO 'OBJETO COMPLETO' ")
   print("creo y guardo Prestamo Basico  aa.init_completo(0,1,1,'2023-10-25',5,'2023-10-30',0,0 ) " )
   print ("busco y muestro Prestamo creado")
   aa=Prestamo()
   print(f"Objeto Vacio: ")   
   print(aa)   
   aa.init_completo(0,1,1,'2023-10-25',5,'2023-10-30',0,0 )
   print(f"Objeto:")     
   print(aa)     
   resp=dao.registrar_prestamo(aa)
   print("RESPUESTA ")
   print(resp)
   print("\n")


   # REGISTRAR DEVOLUCION VALIDA
   print("           TEST PRESTAMO DAO 06 - REGISTRAR DEVOLUCION VALIDA ")
   print("Test Exitoso la primera vez. La siguente informa Fracaso ")
   respu=dao.registrar_devolucion(2,'2023-10-24')
   print(f"RESULTADO DE REGISTRO \n {respu}")


   # Valida que el socio no posea más de tres libros prestados
   print("           TEST PRESTAMO DAO 07 - Valida que el socio no posea más de tres libros prestados")
   print("TRUE -> Socio apto para nuevo prestamo. FALSE no apto.")
   print(f"Socio ID 1 es apto prestamo??? {dao.is_prestamo_posible(1)}")
   print(f"Socio ID 2 es apto prestamo??? {dao.is_prestamo_posible(2)}")
   print(f"Socio ID 3 es apto prestamo??? {dao.is_prestamo_posible(3)}")
   print(f"Socio ID 4 es apto prestamo??? {dao.is_prestamo_posible(4)}")
   print(f"Socio ID 5 es apto prestamo??? {dao.is_prestamo_posible(5)}")



   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO PRESTAMO
   # EJEMPLO PRESTAMO CORRECTO
   print("           TEST PRESTAMO DAO 08 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO PRESTAMO")
   print(" Prestamo correcto -> true")
   print("aa.init_basico(1,1,1,'2023-10-25', 5 )")
   aa=Prestamo()
   #print(aa)   
   aa.init_basico(1,1,1,'2023-10-25',5 )
   print(aa)     
   print (aa.is_check())
   print(aa.errores)
   print("\n")
   

   # CHECK DE CONSISTENCIA DE DATOS DEL OBJETO PRESTAMO
   # EJEMPLO PRESTAMO INCORRECTO
   print("           TEST PRESTAMO DAO 09 - CHECK DE CONSISTENCIA DE DATOS DEL OBJETO PRESTAMO")
   print(" Prestamo NO correcto -> False")
   print("aa.init_basico(-1,-1,-1,'aaaa', -5 )")
   aa=Prestamo()
   #print(aa)   
   aa.init_basico(-1,-1,-1,'aaaa', -5 )   
   print(aa)      
   print (aa.is_check())
   print(aa.errores)
   print("\n")



   # 
   # 
   print("           TEST PRESTAMO DAO 10 - REPORTE: Listado de préstamos demorados")
   print(" Devuelve Array de prestamos ")
   resp=dao.obtener_prestamos_demorados()
   print(f"LEN RESP: {len(resp)}")
   for x in resp:
      print(x)
   print("\n")
   print("\n")
   
   # 
   # EJEMPLO PRESTAMO INCORRECTO
   print("           TEST PRESTAMO DAO 11 - Valida que el socio no posea ningún libro con demora en su devolución")
   print(" TRUE -> Socio apto para nuevo prestamo. FALSE no apto")
   print(f"Socio ID 1 es cumplidor??? {dao.is_socio_cumplidor(1)}")
   print(f"Socio ID 2 es cumplidor??? {dao.is_socio_cumplidor(2)}")
   print(f"Socio ID 3 es cumplidor??? {dao.is_socio_cumplidor(3)}")
   print(f"Socio ID 4 es cumplidor??? {dao.is_socio_cumplidor(4)}")
   print(f"Socio ID 5 es cumplidor??? {dao.is_socio_cumplidor(5)}")
   print("\n")
   print("\n")
   
   print("           TEST PRESTAMO DAO 12 - REPORTE: Listado de préstamos demorados mas de 30 dias")
   print(" Devuelve Array de prestamos mas de 30 dias ")
   resp=dao.obtener_prestamos_demorados_30dias()
   print(f"LEN RESP: {len(resp)}")
   for x in resp:
      print(x)
   print("\n")
   print("\n")
   
   print("           TEST PRESTAMO DAO 13 - Registrar libros extraviado desde Listado de préstamos demorados mas de 30 dias")
   print(" Devuelve Array de libros extraviados ")
   resp=dao.registrar_libros_extraviados()
   print(f"LEN RESP: {len(resp)}")
   for x in resp:
      print(x)
   print("\n")
   print("\n")

   print("           TEST PRESTAMO DAO 14 - REPORTE: Listado de préstamos de un socio identificado por su número de socio")
   print(" Devuelve Array de prestamos ")
   resp =dao.obtener_prestamos_de_socio(1)
   for x in resp:
      print(x)
   print(f"LEN RESP: {len(resp)}")
   #print(resp)
   print("\n")
   print("\n")

   print("           TEST PRESTAMO DAO 15 - REPORTE: Listado de Nombre de todos los solicitantes de un libro en particular identificado por su título")
   print(" Devuelve Array de Apellido, Nombre de Socios ")
   resp=dao.obtener_socios_titulo('matematica i')
   for x in resp:
      print(x)
   print(f"LEN RESP: {len(resp)}")
   print(resp)



   print("           TEST PRESTAMO DAO 16 - Borrado logico de prestamo")
   print(" Devuelve Objeto Prestamo. Sino devuelve Objeto PrestamoError   ")
   print (f"Prestamo 6 antes de borrado logico  ")
   prest= dao.buscar_id(6)
   print(f"LEN RESP: {len(prest)}")
   if len(prest)>0:
         print(prest[0])
   print()
   resp=dao.eliminar(6)
   #print(f"LEN RESP: {len(resp)}")
   print(resp)
   
   print("           TEST PRESTAMO DAO 17 - Obtener prestamos Activos")
   print("         Obtiene todos los Activos. Devuelve Array    ")

   #print("########## obtener_prestamos_activos")
   resp=dao.obtener_prestamos_activos()
   for x in resp:
         print(x)
   print ()

   
   print("           TEST PRESTAMO DAO 18 - Obtener prestamos Eliminados")
   print("         Obtiene todos los Prestamos Eliminados. Devuelve Array    ")
   #print("########## obtener_prestamos_eliminados")
   resp=dao.obtener_prestamos_eliminados()
   for x in resp:
         print(x)
   print ()   
   
   print()
   print("##############   FIN TEST PRESTAMO   ##############")
   print()   
   




test_prestamo()