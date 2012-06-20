#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np


verhus = lambda a,x : a*x*(1-x)

#xs = np.linspace(0.1, 0.9, 100)
output =[]
alpha = 2.6
x = xd = 0.2
for i in range(50):
    x = verhus(alpha, x)
    output.append([verhus(alpha, x)])

pl.title("Iterated solutions of the logistic equation plotted")
pl.plot(output,'bo-') 
   
pl.show()