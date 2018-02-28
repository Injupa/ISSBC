# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:07:02 2018

@author: juanp
"""

import sys
from PyQt4 import QtGui, QtCore
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
         #Menus
        newAction = QtGui.QAction(QtGui.QIcon('newFile.png'), 'Nuevo', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)
         
        saveAction = QtGui.QAction(QtGui.QIcon('descarga.png'), 'Guardar', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
         
        openAction = QtGui.QAction(QtGui.QIcon('openfile.png'), 'Abrir', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)
         
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Archivo')
        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openAction)
 
        self.txt = QtGui.QTextEdit(self)
        self.setCentralWidget(self.txt)
         
            
         #Ventana
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Editor de textos simple")
        self.show()
 
    #Slots 
    def newFile(self):
        self.txt.clear()
         
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo')
        f = open(filename, 'w')
        filedata = self.txt.toPlainText()
        f.write(filedata)
        f.close()
         
         
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Archivo')
        f = open(filename, 'r')
        filedata = f.read()
        self.txt.setText(filedata)
        f.close()
 
         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()