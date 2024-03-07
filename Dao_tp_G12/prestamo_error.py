

class PrestamoError():
    
    def __init__(self) -> None:
       self._estado=False
       self._error="\n"
    
    def __str__(self):
        return f"Estado: {self._estado} | Error: {self._error}"
    
    @property
    def estado(self):
        return self._estado        
            
    @property
    def error(self):
        return self._error 


