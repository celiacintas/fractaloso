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
from random import randrange

def randomize(data):
	randomData = []
	for i in range(len(data)-1):
		randomData.append(data[randrange(0, len(data)-1)])
	return randomData

if __name__ == "__main__":
	
	fileA = open('F/F003.txt')
	originalData = [float(k) for k in fileA.readlines()]
	randomData = randomize(originalData)
	#get the dfa for both set of values
	alphaO, forplotO, forplotNO = dfa(originalData)
	alphaR, forplotR, forplotNR = dfa(randomData)

	#plot the results
	fig = pylab.figure()
	ax = fig.add_subplot(3, 1, 1)
	ori = ax.plot(log10(forplotNO), forplotO, 'b-', label = "Original Data")
	ran = ax.plot(log10(forplotNR), forplotR, 'g-', label = "Random Data")
	pylab.title("DFA")
	pylab.legend([ori[0], ran[0]], ['Original Data','Random Data'])
	pylab.text(2,3, r'$\alpha Original = %f $'%(alphaO), multialignment = 'center')
	pylab.text(2,2, r'$\alpha Random  = %f $'%(alphaR), multialignment = 'center')
	#plot the original and randomize data
	bx = fig.add_subplot(3, 1, 2)
	bx.plot(randomData, 'g-')
	pylab.title("Random Data")
	cx = fig.add_subplot(3, 1, 3)
	cx.plot(originalData, 'b-')
	pylab.title("Original Data")
	
	pylab.show()
