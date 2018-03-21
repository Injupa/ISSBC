# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:35:44 2018

@author: juan
"""

import modP3 as mod
import os


def newOpen(self):
    aux = mod.abrir(self)
    return aux
    
def guardar(self):
   guardar = mod.guardar(self)
   return guardar
   
def saveAsC(self):
    save = mod.guardarComo(self)
    return save
    
def fileSystem(self):
    carpeta = mod.abrirCarpeta(self)
    return carpeta
    
