from abc import ABC, abstractmethod
from typing import List
from interfaces.iterador import Iterator

class IAgregado(ABC):

    @abstractmethod
    def crearIterador(self, elementos:List[object]) -> Iterator:
        pass

