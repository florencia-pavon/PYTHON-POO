from interfaces.iterador import Iterator
from models.llamada import Llamada

class IteradorLlamadas(Iterator):
    
    elementoActual = None

    def __init__(self, elementos: 'Llamada', filtros):
        self.elementos = elementos
        self.filtros = filtros


    def primero(self) -> None:
        self.elementoActual = 0

    
    def siguiente(self) -> None:
        self.elementoActual += 1

    
    def actual(self) -> 'Llamada':
        if not self.haTerminado():
            return self.elementos[self.elementoActual]



    def haTerminado(self) -> bool:
        if self.elementoActual >= len(self.elementos):
            return True
        else:
            return False

    
    def cumpleFiltro(self, llamada: 'Llamada') -> bool:
        return  llamada.esDePeriodo(self.filtros[0], self.filtros[1]) and llamada.tieneRespuestas()