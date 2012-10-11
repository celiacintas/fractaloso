#! /usr/bin/python2
# -*- coding:utf-8 -*-

#The data analyzed in our study is available on this page. 
# http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3
#The sampling rate of the data was 173.61 Hz. For a more 
#detailed description of the data please refer to the manuscript
#Please note, however, that the time series have the spectral 
#bandwith of the aquisition system, which is 0.5 Hz to 85 Hz.

from pyeeg import dfa
import pylab 
from scipy import log10
from numpy import arange

fileA = open('F/F003.txt')
data = [float(k) for k in fileA.readlines()]

alpha, forplot, forplotN = dfa(data)

fig = pylab.figure()
ax = fig.add_subplot(3, 1, 1)
ax.plot(log10(forplotN), forplot, 'r-')
pylab.text(2,3, r'$\alpha = %f $'%(alpha), multialignment = 'center')

bx = fig.add_subplot(3, 1, 2)
bx.plot(data, 'g-')

cx = fig.add_subplot(3, 1, 3)
cx.plot(data, 'b-')

pylab.grid(True)
pylab.show()
