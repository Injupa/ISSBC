# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:14:39 2018

@author: juan
"""

from PyQt4 import QtCore
from PyQt4 import QtGui


def abrir(self):
    
        archivo = QtGui.QFileDialog.getOpenFileName(self, 'Guardar archivo', '/home', 'Text (*.txt)')
        
        fichero = open(archivo)
        data = fichero.read()
        self.AreaTextoArchivo.setText(data)
        fichero.close()
            
def guardar(self):

        ruta_guardar = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo', '/home', 'Text (*.txt)')
 
        fichero = open(ruta_guardar, "w")
        fichero.write(self.AreaTextoArchivo.toPlainText())
        fichero.close()
        
        
def guardarComo(self):
    
    ruta_guardar = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo', '/home', 'Text (*.txt)')
 
    fichero = open(ruta_guardar, "w")
    fichero.write(self.AreaTextoArchivo.toPlainText())
    fichero.close()
    
    
def abrirCarpeta(self):
    
    archivo = QtGui.QFileDialog.getExistingDirectory(self, 'Abrir archivo', '/home')
    archivo = str(archivo)
    self.CampoTextoCarpeta.setText(archivo)
        
    if self.ListaArchivosCarpeta is not None:
        self.ListaArchivosCarpeta.clear()
       
    if self.AreaTextoArchivo is not None:
        self.AreaTextoArchivo.clear()
        
    row = self.ListaArchivosCarpeta.currentRow()
    
    from os import listdir        
    for files in listdir(archivo):
        if files.endswith('.txt'):
            self.ListaArchivosCarpeta.insertItem(row,files)
            self.ListaArchivosCarpeta.setCurrentRow(0)