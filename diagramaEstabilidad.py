#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np


outputDer =[]
alpha = 0.9
xd = 0.2
derivadaDeVerhus = lambda a,x : (a*x)*(1-x)

for i in range(50):
    xd = derivadaDeVerhus(alpha, xd)
    outputDer.append([derivadaDeVerhus(alpha, xd)])
    #xd = np.abs(xd)
    """if (xd < 1):
        print "es estable", xd
        pl.annotate("prueba",xy =(i,xd), xytext = (-20, 20))
    elif (xd == 1):
        print "es neutral", xd
        pl.annotate("prueba 2",xy =(i,xd), xytext = (-20, 20))
    else:
        print "es inestable", xd
        pl.annotate("prueba 3", xy =(i,xd), xytext = (-20, 20))
        #es mayor
    """
pl.plot(range(50),outputDer,'ro-')        
pl.show()
