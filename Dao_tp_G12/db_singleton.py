

import sqlite3

class DBConection:
    _instance=None
    _dbconnection=None
    _conn=None
    
    def __new__(cls, connection_string:str):
        if not cls._instance:
            cls._instance=super (DBConection, cls).__new__(cls)
            
            if connection_string=="":
                cls._dbconnection="biblitecaDB.sqlite"                 
            else:
                cls._dbconnection= connection_string
            cls._conn= sqlite3.connect(cls._dbconnection)    
        
        #print(cls._dbconnection)
           
        return cls._conn
    
    
    
    def __str__(self) -> str:
        return f" Conexion: {self._dbconnection}  "

