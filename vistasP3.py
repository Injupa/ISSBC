# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import controladorP3 as ctrl


class textApp(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
      
        #Elementos de la APP
        self.LabelTextoCarpeta = QtGui.QLabel("Carpeta: ")
        self.CampoTextoCarpeta = QtGui.QLineEdit()        
        self.ListaArchivosCarpeta = QtGui.QListWidget()
        self.AreaTextoArchivo = QtGui.QTextEdit()
        self.BotonCarpeta = QtGui.QPushButton("Seleccionar")
        self.BotonGuardar = QtGui.QPushButton("Guardar")
        self.BotonGuardarComo = QtGui.QPushButton("Guardar Como")
        self.BotonAbrir = QtGui.QPushButton("Abrir")
        
        #Funciones de los elementos
        self.BotonCarpeta.clicked.connect(self.archivo)
        self.BotonGuardar.clicked.connect(self.save) 
        self.BotonGuardarComo.clicked.connect(self.saveAs)
        self.BotonAbrir.clicked.connect(self.abrir)

      
        #PosiciÃÂ³n de los elementos en la interfaz
        grid = QtGui.QGridLayout()
        grid.setSpacing(7)
        grid.addWidget(self.LabelTextoCarpeta, 1, 1)
        grid.addWidget(self.CampoTextoCarpeta, 1, 2, 1, 10)
        grid.addWidget(self.ListaArchivosCarpeta, 2, 1, 6, 2)
        grid.addWidget(self.AreaTextoArchivo, 2, 3, 6, 9)
        grid.addWidget(self.BotonCarpeta, 1, 12)
        grid.addWidget(self.BotonGuardar, 8, 1)
        grid.addWidget(self.BotonGuardarComo, 8, 2)
        grid.addWidget(self.BotonAbrir, 8, 3)
        self.setLayout(grid)      
      
        #Conf ventana
        self.setGeometry(500,300,900,500)
        self.setWindowTitle('Editor de Textos')
        self.show()
        
      
                
        
    def save(self):
        ctrl.guardar(self)
        
    def saveAs(self):
        ctrl.saveAsC(self)
        
    def abrir(self):
        ctrl.newOpen(self)
        
    def archivo(self):
        ctrl.fileSystem(self)
        
        

def main():
    app = QtGui.QApplication(sys.argv)
    ex = textApp()
    sys.exit(app.exec_())



main()
    
