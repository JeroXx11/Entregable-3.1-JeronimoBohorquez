from vista import Ventanalogin
from modelo import Modelo
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class ControladorInicioSesion(object):
    def __init__(self,vista,modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
    def Validar_usuario(self,l,p):
        return self.__mi_modelo.Verificar(l,p)
    def CargarArchivosDICOM(self, carpeta):
       return self.__mi_modelo.CargarArchivosDICOM(carpeta)
def main():
    app = QApplication(sys.argv)
    mi_vista = Ventanalogin()
    mi_modelo = Modelo()
    mi_coordinador = ControladorInicioSesion(mi_vista,mi_modelo)
    mi_vista.Setcontrolador(mi_coordinador)
    mi_modelo.SetUsuario("medicoAnalitico")
    mi_modelo.SetContraseña("bio12345")
    mi_vista.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
        