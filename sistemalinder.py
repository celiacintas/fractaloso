#! /usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl


class Cursor:
      def __init__(self,x,y, angulo):
        self.x = x
        self.y = y
        self.ang = angulo

class SistemaL:

      def __init__(self,gramatica, inicial, distancia, nivel):
          self.gramatica = gramatica
          self.inicial = inicial
          self.distancia = distancia
          self.nivel = nivel

      def iniciar(self):
          self.cursor = Cursor(0,0,0)
          pl.plot([self.cursor.x, self.cursor.x+ self.distancia],[self.cursor.y, self.cursor.y])
          #pass

      def generar(self, nivel, cursor, distancia):

          if nivel == 0:
                  a = (cursor.x, cursor.y)
                  b = (cursor.x + distancia*np.cos(cursor.ang),cursor.y + distancia*np.sin(cursor.ang))
                  print a, "-->", b
                  pl.plot([a[0],b[0]],[a[1],b[1]])
                  cursor.x = b[0]
                  cursor.y = b[1]
          else:
              print "nivel = ", nivel
              for i in self.gramatica[self.inicial]:
                  if i == 'F':
                      self.generar(nivel-1, cursor, distancia/3)
                  elif i == '+':
                      cursor.ang = cursor.ang - np.pi/3
                  elif i == '-':
                      cursor.ang = cursor.ang + np.pi/3

if __name__ == "__main__":
    miSistema = SistemaL(gramatica = {'F':"F-F++F-F"},inicial = 'F',distancia = 10000, nivel = 5)
    miSistema.iniciar()
    miSistema.generar(miSistema.nivel, miSistema.cursor, miSistema.distancia)
    print "termine con todos los niveles"
    pl.show()
