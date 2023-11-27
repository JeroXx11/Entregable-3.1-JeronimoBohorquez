from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.uic import loadUi
from modelo import Modelo
import os
import pydicom
import matplotlib.pyplot as plt

class Ventanalogin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("vista_inicio_sesion.ui", self)
        self.setup()
    def setup(self):
        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)
    def iniciar_sesion(self):
        print("INICIANDO SESION...")
        usuario = self.lineEditUsuario.text()
        contraseña = self.lineEditContrasena.text()
        resultado = self.__mi_controlador.Validar_usuario(usuario,contraseña)
        if resultado:
            print("INICIO DE SESION EXITOSO")
            texto = "Bienvenido!!"
            msj = QMessageBox(self)
            msj.setIcon(QMessageBox.Information)
            msj.setText(texto)
            msj.setWindowTitle("Información")
            msj.show()
            nueva_ventana = VentanaPrincipal()
            nueva_ventana.show()
            self.hide()
            print("VENTANA OCULTADA")
        else:
            print("ERROR DE INICIO DE SESION")
            texto = "Usuario incorrecto"
            msj = QMessageBox(self)
            msj.setIcon(QMessageBox.Warning)
            msj.setText(texto)
            msj.setWindowTitle("Alerta")
            msj.show()

    def closeEvent(self,event):
        print("Dentro de close")
    def Setcontrolador(self,c):
        self.__mi_controlador = c
class VentanaPrincipal(QWidget):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("vista_principal.ui", self)
        self.Setup()
    def Setup(self):
        self.btnCargar.clicked.connect(self.CargarArchivo)
        self.Slider.valueChanged.connect(self.mostrar_dicom)
    def CargarArchivo(self):
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", ".")
        if carpeta:
            self.lineEditCarpeta.setText(carpeta)
            archivos_dicom = [archivo for archivo in os.listdir(carpeta) if archivo.lower().endswith('.dcm')]
            print("Archivos DICOM en la carpeta:")
            for archivo in archivos_dicom:
                print(os.path.join(carpeta, archivo))
            self.Slider.setRange(0, len(self.archivos_dicom) - 1)
            self.mostrar_dicom(0)
    def convertir_dicom_a_imagen(dicom_obj):
        matriz_pixeles = dicom_obj.pixel_array
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.imshow(matriz_pixeles, cmap=plt.cm.bone)
        buf, size = fig.canvas.print_to_buffer()
        qimage = QPixmap.fromImage(QImage(buf, size[0], size[1], QImage.Format_RGB32))
        plt.close(fig)

        return qimage
    def mostrar_dicom(self, indice):
        ruta_completa = os.path.join(self.lineEditCarpeta.text(), self.archivos_dicom[indice])
        dicom_obj = pydicom.dcmread(ruta_completa)
        imagen_convertida = convertir_dicom_a_imagen (dicom_obj)
        self.labelDicom.setPixmap(imagen_convertida)
        self.sliderArchivos.setValue(indice)

    def addcontrolador(self,a):
        self.__mi_controlador2 = a
    