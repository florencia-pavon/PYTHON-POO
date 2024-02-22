from interfaces.iterador import Iterator
from models.respuestaDeCliente import RespuestaDeCliente

class IteradorRespuestaDeCliente(Iterator):
    
    elementoActual: int

    def __init__(self, elementos: 'RespuestaDeCliente', filtros):
        self.elementos = elementos
        self.filtros = filtros
    
    def primero(self) -> None:
        self.elementoActual = 0

    
    def siguiente(self) -> None:
        self.elementoActual += 1

    
    def actual(self) -> 'RespuestaDeCliente':
        return self.elementos[self.elementoActual]


    
    def haTerminado(self) -> bool:
        if self.elementoActual >= len(self.elementos):
            return True
        else:
            return False

    
    
    def cumpleFiltro(self, rta_cliente: 'RespuestaDeCliente') -> bool:
        return rta_cliente.getIdLlamada() == self.filtros