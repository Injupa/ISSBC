# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import sys
from PyQt4 import QtGui


class issbc(QtGui.QWidget):
    
    def __init__(self):
        super(issbc, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "¿Esta seguro de que quiere salir?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = issbc()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()