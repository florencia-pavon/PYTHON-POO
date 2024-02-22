from pantallas.pantallaConsultarEncuesta import PantallaConsultaEncuesta
from control.gestorConsultarEncuesta import GestorConsultarEncuesta






def main():
    #Instanciar gestor y pantalla
    gestorConsultarEncuesta = GestorConsultarEncuesta(None)
    pantallaConsultaEncuesta = PantallaConsultaEncuesta(gestorConsultarEncuesta)
    gestorConsultarEncuesta.pantalla = pantallaConsultaEncuesta


    
    pantallaConsultaEncuesta.opcionConsultarEncuesta()
    

    
    

                        

                    
if __name__ == '__main__':
    main()




