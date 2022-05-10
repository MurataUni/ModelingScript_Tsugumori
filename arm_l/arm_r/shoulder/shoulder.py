from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

shoulder_adapter_length = 5.

shoulder_adapter_geta_1 = sw.rotate(np.pi).void(2.)
shoulder_adapter_geta_2 = sw.rotate(-np.pi).parent(shoulder_adapter_geta_1).void(0.)

edges_shoulder_adapter = sw.rib_edges_circular(2.5, 2*np.pi, 8, True)
shoulder_adapter = sw.parent(shoulder_adapter_geta_2).void(shoulder_adapter_length)
shoulder_adapter.add_rib(0., edges_shoulder_adapter)
shoulder_adapter.add_rib(1., edges_shoulder_adapter)

edges_outer = sw.rib_edges_circular(5., np.pi, 16, True)
edges_outer.insert(0, (4., -4))
edges_outer.append((-4, -4.))

outer = sw.parent(shoulder_adapter, 0.8).void(6.)
outer.add_rib(0.5/5., edges_outer)
outer.add_rib(1.0-0.5/5., edges_outer)
outer.add_rib(0., edges_util.scale(edges_outer, (10.-0.5)/10.))
outer.add_rib(1., edges_util.scale(edges_outer, (10.-0.5)/10.))
outer.order_ribs()

inner_geta = sw.parent(outer, 0.).void(1.)
edges_inner = [(4.5, 0.), (-4.5, 0.), (-5., -4+0.1), (5., -4+0.1)]
inner = sw.parent(inner_geta).void(4.)
inner.add_rib(0., edges_inner)
inner.add_rib(1., edges_inner)

edges_adapter = sw.rib_edges_circular(2., 2*np.pi, 8, True)
adapter_geta_1 = sw.parent(outer, 0.).void(2.5)
adapter_geta_2 = sw.rotate(np.pi/2, -np.pi/2).parent(adapter_geta_1).void(3.5)
adapter = sw.rotate().parent(adapter_geta_2).void(2.)
adapter.add_rib(0., edges_adapter)
adapter.add_rib(1., edges_adapter)

# sw.start_display()
sw.generate_stl_binary(path, fname)