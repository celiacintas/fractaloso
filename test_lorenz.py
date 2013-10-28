#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from numpy import mgrid
from traits.api import HasTraits, Range, Instance, on_trait_change
from traitsui.api import View, Item, Group
from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel


def lorenz_func(x, y, z, s, r, b):
    u = s*(y-x)
    v = r*x -y - x*z
    w = x*y - b*z
    return u, v, w

class Lorenz_Model(HasTraits):
    r = Range(1., 100., 28., )
    s = Range(1., 100., 10., )
    b = Range(1., 10., 2.66, )
    
    x, y, z = mgrid[-50:50:100j,-50:50:100j,-10:60:70j]
    scene = Instance(MlabSceneModel, ())
    plot = Instance(PipelineBase)

    @on_trait_change('r, s, b, scene.activated')
    def update_plot(self):
        u, v, w = lorenz_func(self.x, self.y, self.z, self.s,self.r, self.b)
        if self.plot is None:
                self.plot = self.scene.mlab.flow(self.x, self.y, self.z, u, v, w, 
                                             linetype='ribbon',seedtype='plane', integration_direction='forward',
                                             opacity=0.5, line_width=3, colormap='jet')
                
                #self.plot = self.scene.mlab.quiver3d(self.x, self.y, self.z, u, v, w)
        self.plot.mlab_source.set(x=self.x, y=self.y, z=self.z, u=u, v=v, w=w)


    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                Group(
                        '_', 'r', 's', 'b'
                     ), resizable=True,)

lorenz = Lorenz_Model()
lorenz.configure_traits()