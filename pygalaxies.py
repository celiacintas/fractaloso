#! /usr/bin/python2
# -*- coding: utf-8 -*-

# Using AC for the construction of galaxies with
# Exponentianl Disk Potential as Rotation Dynamic
#

import numpy as np
import scipy.stats.distributions as dis
from mayavi import mlab
from itertools import repeat, izip, ifilter
#import pylab as pl


class Star:
    "Clase para definir una Estrella"""

    def __init__(self, r, angle, state=0):
        """Constructor de estrellas """
        self.r = r
        self.angle = angle
        self.state = state


class Galaxy:
    """Clase galaxia"""

    def __init__(self, radio, neighborhood):
        """Initialize the galaxy with some radius
        and the chosen neighborhood """

        stars = []
        stars.append(Star(0, neighborhood[0], np.random.randint(1, 15)))

        try:
            for r in np.arange(1, radio + 1):
                map(lambda a: stars.append(Star(a[1], a[0] / float(a[1]),
                    np.random.randint(1, 15))), izip(neighborhood,
                    repeat(r, len(neighborhood))))
            self.stars = stars
        except e:
            print e

    def scanning(self):
        """See state of stars and change formations"""
        #for s in self.stars:
        neighborhood = ifilter(lambda star: ((s.r + 1) == star.r)
                               & (star.state == 0), self.stars)
        #print self.stars

    def plotting(self):
        """For plotting the stars"""
        mlab.clf()
        map(lambda star: mlab.points3d(star.r * np.cos(star.angle),
            star.r * np.sin(star.angle), star.r * np.cos(star.angle),
            colormap="copper", scale_factor=.25), self.stars)

        print self.stars

if __name__ == "__main__":
    neighborhood = [0, 60, 120, 180, 240, 330]
    vals = [(0, 1), (0.84, 0.16)]
    distributionFunc = dis.rv_discrete(name='custm', values=vals)
    myGalaxy = Galaxy(1.5, neighborhood)
    myGalaxy.scanning()
    myGalaxy.plotting()

    mlab.show()
