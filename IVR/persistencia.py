from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.cliente import Cliente
from models.estado import Estado
from models.encuesta import Encuesta
from models.pregunta import Pregunta
from models.llamada import Llamada
from models.cambioEstado import CambioEstado
from models.respuestaPosible import RespuestaPosible
from models.respuestaDeCliente import RespuestaDeCliente
from db_singleton import Base
from db_singleton import session
from db_singleton import engine
from datetime import date, timedelta, datetime

# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear clientes
cliente_1 = Cliente(dni=123456789, nombre_completo='Juan Pérez', nro_celular=5551234567)
cliente_2 = Cliente(dni=987654321, nombre_completo='Ana Martínez', nro_celular=5559876543)
cliente_3 = Cliente(dni=456789123, nombre_completo='Carlos Sánchez', nro_celular=5554567890)
cliente_4 = Cliente(dni=789123456, nombre_completo='Laura Rodríguez', nro_celular=5557891234)
cliente_5 = Cliente(dni=654321987, nombre_completo='María López', nro_celular=5556543219)
#Agregar los clientes a la base de datos
session.add_all([cliente_1, cliente_2, cliente_3, cliente_4, cliente_5])

# Crear estados
estado_1 = Estado(nombre='iniciada')
estado_2 = Estado(nombre='finalizada')
#Agregar los estado a la base de datos
session.add_all([estado_1, estado_2])

#Crear encuesta
encuesta = Encuesta(descripcion='Satisfacción cliente', fechaFinVigencia=date(2024, 12, 1))
#Agregar encuesta a la base de datos
session.add(encuesta)

# Crear preguntas
pregunta_1 = Pregunta(pregunta='¿Que puntaje le da a la atencion?', id_encuesta=1)
pregunta_2 = Pregunta(pregunta='¿Se resolvio su problematica?', id_encuesta=1)
#Agregar preguntas a la base de datos
session.add_all([pregunta_1, pregunta_2])

# Crear respuestas posibles
respuesta_1 = RespuestaPosible(valor=3, descripcion='Malo', id_pregunta=1)
respuesta_2 = RespuestaPosible(valor=5, descripcion='Normal', id_pregunta=1)
respuesta_3 = RespuestaPosible(valor=10, descripcion='Excelente', id_pregunta=1)
respuesta_4 = RespuestaPosible(valor=1, descripcion='Si', id_pregunta=2)
respuesta_5 = RespuestaPosible(valor=2, descripcion='No', id_pregunta=2)
#Agregar respuestas posibles a la base de datos
session.add_all([respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5])

# Crear las llamadas
llamada_1 = Llamada(fecha=date(2023, 11, 9), descripcion_operador='Operador 1', detalle_accion='Accion 1', duracion=30, encuesta_enviada=True, observacion_auditor='Correcta', id_cliente=1)
llamada_2 = Llamada(fecha=date(2023, 10, 9), descripcion_operador='Operador 3', detalle_accion='Accion 2', duracion=30, encuesta_enviada=True, observacion_auditor='Correcta', id_cliente=2)
llamada_3 = Llamada(fecha=date(2023, 11, 21), descripcion_operador='Operador 3', detalle_accion='Accion 1', duracion=30, encuesta_enviada=True, observacion_auditor='Correcta', id_cliente=3)
llamada_4 = Llamada(fecha=date(2023, 10, 3), descripcion_operador='Operador 2', detalle_accion='Accion 1', duracion=30, encuesta_enviada=True, observacion_auditor='Correcta', id_cliente=4)
llamada_5 = Llamada(fecha=date(2023, 11, 1), descripcion_operador='Operador 1', detalle_accion='Accion 1', duracion=30, encuesta_enviada=True, observacion_auditor='Correcta', id_cliente=5)
#Agregar llamadas a la base de datos
session.add_all([llamada_1, llamada_2, llamada_3, llamada_4, llamada_5])

# Establecer las fechas y horas manualmente para los cambios de estado
fecha_hora_12_pm = datetime(2023, 11, 9, 12, 0, 0)
fecha_hora_12_30_pm = fecha_hora_12_pm + timedelta(minutes=30)
fecha_hora_11_pm = datetime(2023, 10, 9, 12, 0, 0)
fecha_hora_11_30_pm = fecha_hora_11_pm + timedelta(minutes=30)
fecha_hora_10_pm = datetime(2023, 11, 21, 12, 0, 0)
fecha_hora_10_30_pm = fecha_hora_10_pm + timedelta(minutes=30)
fecha_hora_9_pm = datetime(2023, 10, 3, 12, 0, 0)
fecha_hora_9_30_pm = fecha_hora_9_pm + timedelta(minutes=30)
fecha_hora_8_pm = datetime(2023, 11, 1, 12, 0, 0)
fecha_hora_8_30_pm = fecha_hora_8_pm + timedelta(minutes=30)

# Crear los cambios de estado
cambio_estado_1 = CambioEstado(fecha_hora_inicio=fecha_hora_12_pm, id_estado=1, id_llamada=1)
cambio_estado_2 = CambioEstado(fecha_hora_inicio=fecha_hora_12_30_pm, id_estado=2, id_llamada=1)
cambio_estado_3 = CambioEstado(fecha_hora_inicio=fecha_hora_11_pm, id_estado=1, id_llamada=2)
cambio_estado_4 = CambioEstado(fecha_hora_inicio=fecha_hora_11_30_pm, id_estado=2, id_llamada=2)
cambio_estado_5 = CambioEstado(fecha_hora_inicio=fecha_hora_10_pm, id_estado=1, id_llamada=3)
cambio_estado_6 = CambioEstado(fecha_hora_inicio=fecha_hora_10_30_pm, id_estado=2, id_llamada=3)
cambio_estado_7 = CambioEstado(fecha_hora_inicio=fecha_hora_9_pm, id_estado=1, id_llamada=4)
cambio_estado_8 = CambioEstado(fecha_hora_inicio=fecha_hora_9_30_pm, id_estado=2, id_llamada=4)
cambio_estado_9 = CambioEstado(fecha_hora_inicio=fecha_hora_8_pm, id_estado=1, id_llamada=5)
cambio_estado_10 = CambioEstado(fecha_hora_inicio=fecha_hora_8_30_pm, id_estado=2, id_llamada=5)
# Agregar los Cambios de estado a la base de datos
session.add_all([cambio_estado_1, cambio_estado_2, cambio_estado_3, cambio_estado_4, cambio_estado_5, cambio_estado_6, cambio_estado_7, cambio_estado_8, cambio_estado_9, cambio_estado_10])

#Creaer las respuestas de cliente
respuestaCliente1 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-09', '%Y-%m-%d'), id_respuesta_posible=3, id_llamada=1)
respuestaCliente2 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-09', '%Y-%m-%d'), id_respuesta_posible=2, id_llamada=1)
respuestaCliente3 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-10-09', '%Y-%m-%d'), id_respuesta_posible=10, id_llamada=2)
respuestaCliente4 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-10-09', '%Y-%m-%d'), id_respuesta_posible=1, id_llamada=2)
respuestaCliente5 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-21', '%Y-%m-%d'), id_respuesta_posible=5, id_llamada=3)
respuestaCliente6 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-21', '%Y-%m-%d'), id_respuesta_posible=1, id_llamada=3)
respuestaCliente7 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-10-03', '%Y-%m-%d'), id_respuesta_posible=10, id_llamada=4)
respuestaCliente8 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-10-03', '%Y-%m-%d'), id_respuesta_posible=1, id_llamada=4)
respuestaCliente9 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-01', '%Y-%m-%d'), id_respuesta_posible=5, id_llamada=5)
respuestaCliente10 = RespuestaDeCliente(fecha_encuesta=datetime.strptime('2023-11-01', '%Y-%m-%d'), id_respuesta_posible=2, id_llamada=5)

# Agregar las respuestas posibles a la base de datos
session.add_all([respuestaCliente1, respuestaCliente2, respuestaCliente3, respuestaCliente4, respuestaCliente5, respuestaCliente6, respuestaCliente7, respuestaCliente8, respuestaCliente9, respuestaCliente10])

# Commit para guardar en la base de datos
session.commit()

# Cerrar la sesión
session.close()
