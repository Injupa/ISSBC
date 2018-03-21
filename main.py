# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:44:59 2018

@author: juan
"""

import sys, os
from PyQt4 import QtGui
from PyQt4 import QtCore

import vistasP3 as vts

app = QtGui.QApplication(sys.argv)      
qb = vts.App()      
sys.exit(app.exec_())