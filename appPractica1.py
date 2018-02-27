# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:31:04 2018

@author: juanp
"""

#Aplicación básica práctica 1 ISSBC


import sys
from PyQt4 import *


class ventana(QtGui.QMainWindow):
    
    def __init__(self):
        super(ventana, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        #Información a mostrar
        label1 = QtGui.QLabel('Descartes:', self)
        label1.move(35, 30)        
        
        label2 = QtGui.QLabel('31 de mayo de 1596', self)
        label2.move(55, 60)      
        
        #Barra de menus
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        saveAction = QtGui.QAction(QtGui.QIcon('descarga.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save proyect')
        saveAction.triggered.connect(QtGui.qApp.saveState)
        
        nextAction = QtGui.QAction(QtGui.QIcon('next.ico'), '&Siguiente', self)
        nextAction.setShortcut('Ctrl+P')
        nextAction.setStatusTip('Next Quote')
        #nextAction.triggered.connect(QtGui.qApp.nextState)
        

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(nextAction)
        
        #Botones
        boton = QtGui.QPushButton("Verdadero", self)
        boton1 = QtGui.QPushButton("Falso", self)
        boton.move(100, 250) 
        boton1.move(200, 250)
        
        #Barra de estado
        self.statusBar().showMessage('Ready')
                
        
        #Tamaño ventana.
        self.setWindowTitle('Buttons')           
        
        self.resize(400, 300)
        self.center()        
        self.setWindowTitle('Quiz Fechas')    
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Salir',
            "¿Esta seguro de que quiere salir?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
            
    
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ventana()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()