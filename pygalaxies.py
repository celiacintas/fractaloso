#! /usr/bin/python2
# -*- coding: utf-8 -*-

# Using AC for the construction of galaxies with
# Exponentianl Disk Potential as Rotation Dynamic
#

import numpy as np
import scipy.stats.distributions as dis
from mayavi import mlab
from itertools import repeat, izip
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
        for r in radio:
            map(lambda a: stars.append(Star(a[1], a[0] / float(a[1]),
                np.random.randint(1, 15))), izip(neighborhood,
                repeat(r, len(neighborhood))))
        self.stars = stars

    def scanning(self):
        """See state of stars and change formations"""
        pass

if __name__ == "__main__":
    neighborhood = [0, 60, 120, 180, 240, 330]
    vals = [np.arange(7), (0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1)]
    distributionFunc = dis.rv_discrete(name='custm', values=vals)
    myGalaxy = Galaxy(1.5, neighborhood)
    mlab.show()
