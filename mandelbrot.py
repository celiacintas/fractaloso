import numpy as N
import pylab as P

dx = ( .663,.007)
dy = (-.191,.007) 
v  = N.zeros((2048, 2048),'uint8')


c  = N.zeros((2048,2048),'complex')
c[:].real = N.linspace(dy[0],dy[0]+dy[1],
                       c.shape[0])[:,N.newaxis]
c[:].imag = N.linspace(dx[0],dx[0]+dx[1],
                       c.shape[1])[N.newaxis,:]
z  = c.copy()           
for it in xrange(256):  
    z *= z              
    z += c              
    v += (N.abs(z) >= 4)*(v == 0)*it
P.imshow(v)     
P.show()
