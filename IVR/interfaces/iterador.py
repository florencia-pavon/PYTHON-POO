from abc import ABC, abstractmethod

class Iterator(ABC):

    @abstractmethod
    def primero(self) -> None:
        pass

    @abstractmethod
    def siguiente(self) -> None:
        pass

    @abstractmethod
    def actual(self) -> 'object':
        pass

    @abstractmethod
    def haTerminado(self) -> bool:
        pass
    
    @abstractmethod
    def cumpleFiltro(self, elemento:'object') -> bool:
        pass

