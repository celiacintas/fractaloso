#! /usr/bin/python2
# -*- coding: utf-8 -*-

# Using AC for the construction of galaxies


import numpy as np
import scipy.stats.distributions as dis
from mayavi import mlab
from itertools import repeat, izip, ifilter


class Star(object):
    "Clase para definir una Estrella"""

    def __init__(self, r, angle, state=0):
        """Constructor de estrellas """
        self.r = r
        self.angle = angle
        self.state = state


class Galaxy(object):
    """Clase galaxia"""

    def __init__(self, radio, neighborhood):
        """Initialize the galaxy with some radius
        and the chosen neighborhood """

        self.distributionFuncStars = dis.rv_discrete(name='custm',
                                                     values=[(0, 1),
                                                             (0.84, 0.16)])
        self.distributionGas = dis.rv_discrete(name='custm_gas',
                                               values=[(0, 1), (0.3, 0.7)])
        stars = []
        stars.append(Star(0, neighborhood[0],
                          self.distributionFuncStars.rvs()))

        try:
            for r in np.arange(1, radio + 1, 0.5):  # para regular el tamaño de la celda
                map(lambda a: stars.append(Star(a[1], a[0] / float(a[1]),
                    self.distributionFuncStars.rvs())), izip(neighborhood,
                    repeat(r, len(neighborhood))))
            self.stars = stars
        except e:
            print(e)

    def birthFunction(self, star):
        """Initialize one star"""
        star[0].state = self.distributionFuncStars.rvs()

    def growthFunction(self, star):
        """Increases growth of each star"""
        if star.state > 8:
            star.state = 0
        star.state += 1
        try:
            # set angular velocity
            star.angle = star.angle + 1 / float(star.r)
        except ZeroDivisionError:
            # just for save the  day :)
            star.angle = star.angle + 1

    def scanning(self):
        """See state of stars and change formations"""
        for s in self.stars:
            localNeighborhood = ifilter(lambda star: star[1] == star[0].r + 1,
                                        izip(self.stars,
                                        repeat(s.r, len(self.stars))))
            map(self.birthFunction, localNeighborhood)
        #  aqui envejecemos la galaxia
        map(self.growthFunction, self.stars)

    def plottingStars(self, colors):
        """For plotting the stars"""
        x = []
        y = []
        activeStars = filter(lambda s: s.state != 0, self.stars)
        map(lambda star: x.append(float(star.r * np.cos(star.angle))),
            activeStars)
        map(lambda star: y.append(float(star.r * np.sin(star.angle))),
            activeStars)

        return mlab.points3d(x, y, x, resolution=20, scale_factor=.5,
                             scale_mode='none')

    def countOfActiveStars(self):
        """Show counter of stars"""
        activeStars = ifilter(lambda s: s.state != 0, self.stars)
        noActiveStars = ifilter(lambda s: s.state == 0, self.stars)

        return len(list(activeStars)), len(list(noActiveStars))

    def plottingInterstellarGas(self):
        """Insert randomness in the production of the galaxy """
        x = []
        y = []

        activeGas = filter(lambda s: self.distributionGas.rvs() == 1,
                           self.stars)

        map(lambda star: x.append(float(star.r * np.cos(star.angle))),
            activeGas)
        map(lambda star: y.append(float(star.r * np.sin(star.angle))),
            activeGas)

        return mlab.points3d(x, y, x, color=(0.8, 0.5, 0), resolution=20,
                             scale_factor=.5, scale_mode='none')


if __name__ == "__main__":
    neighborhood = [0, 60, 120, 180, 240, 330]
    colors = {1: (1, 1, 0.9), 2: (1, 1, 0.6), 3: (1, 1, 0.4), 4: (1, 1, 0.2),
              5: (1, 1, 0), 6: (1, 0.8, 0), 7: (1, 0.5, 0), 8: (1, 0.2, 0),
              9: (1, 0, 0)}

    myGalaxy = Galaxy(50, neighborhood)
    print("al comienzo tenemos {}".format(myGalaxy.countOfActiveStars()))
    for t in range(40):
        myGalaxy.scanning()
    points = myGalaxy.plottingStars(colors)
    otherpoints = myGalaxy.plottingInterstellarGas()
    print("al final tenemos {}".format(myGalaxy.countOfActiveStars()))

    mlab.pipeline.volume(mlab.pipeline.gaussian_splatter(points))
    mlab.pipeline.volume(mlab.pipeline.gaussian_splatter(otherpoints))
    mlab.view(49, 31.5, 52.8, (4.2, 37.3, 20.6))
    mlab.show()
