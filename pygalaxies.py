#! /usr/bin/python2
# -*- coding: utf-8 -*-

# Using AC for the construction of galaxies with 
# Exponentianl Disk Potential as Rotation Dynamic
#

import numpy as np
import scipy.stats.distributions as dis
from mayavi import mlab
#import pylab as pl


class Star:
    
      def __init__(self, r, angle, state = 0):
        self.r = r
        self.angle = angle
        self.state = state
        

class Galaxy:

      def __init__(self, range, neighborhood):
          """Initialize the galaxy with some radius and the chosen neighborhood """
          
          stars = []
          stars.append(Star(0, neighborhood[0], np.random.randint(1,15)))
          #colocar zip y map
          for r in np.arange(1, range):
              for a in neighborhood:
                  stars.append(Star(r, a/float(r), np.random.randint(1,15)))
              
          self.stars = stars
          
      def scanning(self):
          """See state of stars and change formations"""
          pass
                 
if __name__ == "__main__":
    neighborhood = [0, 60, 120, 180, 240, 330]
    vals = [np.arange(7), (0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1)]
    distributionFunc = dis.rv_discrete(name='custm', values=vals)
    myGalaxy = Galaxy(, 1.5 ,neighborhood)
    mlab.show()
