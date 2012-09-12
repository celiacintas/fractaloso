#! /usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
from itertools import product
from mayavi import mlab
#import pylab as pl


class Cursor:
      def __init__(self,x,y,z, angulo):
        self.x = x
        self.y = y
        self.z = z
        self.ang = angulo

class SistemaL:

      def __init__(self,gramatica, inicial, distancia, nivel):
          self.gramatica = gramatica
          self.inicial = inicial
          self.distancia = distancia
          self.nivel = nivel

      def iniciar(self):
          self.cursor = Cursor(0,0,0,0)
         
      def generar(self, nivel, cursor, distancia, dim):

          if nivel == 0:
                  mlab.points3d([cursor.x, cursor.x+3, cursor.x, cursor.x+3],[cursor.y, cursor.y, cursor.y -3,cursor.y -3],
                                [cursor.z, cursor.z, cursor.z -3,cursor.z -3],colormap="copper", scale_factor=.25)
                                
                  cursor.x = cursor.x + distancia*np.cos(cursor.ang)
                  cursor.y = cursor.y + distancia*np.sin(cursor.ang)
                  cursor.z = cursor.z + distancia*np.sin(cursor.ang)
                  
                  #a = [(cursor.x, cursor.x, cursor.x)] #para trabajar con 1D
                  #b = (cursor.x + distancia*np.cos(cursor.ang),cursor.y + distancia*np.sin(cursor.ang))
                  #mlab.points3d(a, a, a, colormap="copper", scale_factor=.25)
                  
                  #cursor.x = b[0]
                  #cursor.y = b[1]
          else:
              print "nivel = ", nivel
              for i in self.gramatica[self.inicial]:
                  if i == 'A':
                      self.generar(nivel-1, cursor, distancia/3.0, dim)
                  elif i == 'B':
                      cursor.x += 3*distancia
                      
                      print "la x de cursor tiene: ",cursor.x
              
if __name__ == "__main__":
    miSistema = SistemaL(gramatica = {'A':"ABA", 'B':"BBB"},inicial = 'A',distancia = 1, nivel = 1)
    miSistema.iniciar()
    miSistema.generar(miSistema.nivel, miSistema.cursor, miSistema.distancia, "2D")
    print "termine con todos los niveles"
    mlab.show()
