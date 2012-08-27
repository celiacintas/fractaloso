#! /usr/bin/python2
# -*- coding: utf-8 -*-

# Using AC for the construction of galaxies with 
# Exponentianl Disk Potential as Rotation Dynamic
#

import numpy as np
from mayavi import mlab
#import pylab as pl


class Star:
      def __init__(self, r, angle, state = 0):
        self.r = r
        self.angle = angle
        self.state = state
        

class Galaxy:

      def __init__(self, r, neighborhood):
          """Initialize the galaxy with some radius and the chosen neighborhood """
          pass
          
      def scanning(self):
          """See state of stars and change formations"""
          pass
                 
if __name__ == "__main__":
    miGalaxia = Galaxia()
    mlab.show()
