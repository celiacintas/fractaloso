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

        self.distributionFunc = dis.rv_discrete(name='custm', values=[(0, 1),
                                                (0.84, 0.16)])
        stars = []
        stars.append(Star(0, neighborhood[0], self.distributionFunc.rvs()))

        try:
            for r in np.arange(1, radio + 1):
                map(lambda a: stars.append(Star(a[1], a[0] / float(a[1]),
                    self.distributionFunc.rvs())), izip(neighborhood,
                    repeat(r, len(neighborhood))))
            self.stars = stars
        except e:
            print e

    def birthFunction(self, star):
        """Initialize one star"""
        star[0].state = self.distributionFunc.rvs()
        #print "nacio otra estrella"

    def growthFunction(self, star):
        """increases growth of each star"""
        star.state += 1
        try:
            star.angle = star.angle + 1 / float(star.r)
        except ZeroDivisionError:
            star.angle = star.angle + 1

    def scanning(self):
        """See state of stars and change formations"""
        for s in self.stars:
            localNeighborhood = ifilter(lambda star: star[1] == star[0].r + 1,
                                        izip(self.stars, repeat(s.r, len(self.stars))))
            map(self.birthFunction, localNeighborhood)
        #aqui envejecemos la galaxia
        map(self.growthFunction, self.stars)

    def plotting(self):
        """For plotting the stars"""
        #mlab.clf()
        activeStars = ifilter(lambda s: s.state != 0, self.stars)
        map(lambda star: mlab.points3d(star.r * np.cos(star.angle),
            star.r * np.sin(star.angle), star.r * np.cos(star.angle),
            colormap="copper", scale_factor=.5), activeStars)

    def countOfActiveStars(self):
        """ """
        activeStars = ifilter(lambda s: s.state != 0, self.stars)
        noActiveStars = ifilter(lambda s: s.state == 0, self.stars)

        return len(list(activeStars)), len(list(noActiveStars))

if __name__ == "__main__":
    neighborhood = [0, 60, 120, 180, 240, 330]
    myGalaxy = Galaxy(50, neighborhood)
    print "al comienzo tenemos ", myGalaxy.countOfActiveStars()
    for t in range(500):
        myGalaxy.scanning()
    myGalaxy.plotting()
    print "al final tenemos ", myGalaxy.countOfActiveStars()
    mlab.show()
