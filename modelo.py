import os
class Modelo(object):
    def __init__(self):
        self.__usuario = ""
        self.__contraseña = ""
        self.__archivos_dicom = []
    def SetUsuario(self,l):
        self.__usuario = l
    def SetContraseña(self,p):
        self.__contraseña = p
    def Verificar(self, l,p):
        return (self.__usuario == l) and (self.__contraseña == p )
    def CargarArchivosDICOM(self, carpeta):
        self.__archivos_dicom = [archivo for archivo in os.listdir(carpeta) if archivo.lower().endswith('.dcm')]
        return self.__archivos_dicom
    