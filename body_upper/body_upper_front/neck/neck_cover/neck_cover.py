from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

back_length = 7.
lr_length = 18.-0.5
lr_cham_length = 2.

half_t = 1.

adapter_edges = [(1., half_t), (-1., half_t), (-1., -half_t), (1., -half_t), ]
adapter = sw.rotate(np.pi).void(3.5)
adapter.add_ribs([0., 1.], adapter_edges)

back_geta = sw.rotate(-np.pi+np.pi/2).parent(adapter).void(3.5)
back_edges = [(0.5, half_t), (-0.5, half_t), (-0.5, -half_t), (0.5, -half_t)]
back = sw.rotate(-np.pi).parent(back_geta).void(7.)
back.add_ribs([0., 1.], back_edges)

right_geta = sw.rotate(-np.pi-np.pi/2).parent(adapter).void(3.)
right_edges = [(0.5, half_t), (-0.5, half_t), (-0.5, -half_t), (0.5, -half_t)]
right_edges_end = [(0.5, 0.), (0., 0.), (0., -half_t), (0.5, -half_t)]
left = sw.rotate(np.pi/2).parent(right_geta).void(lr_length)
left.add_ribs([0., 1.-2./lr_length], right_edges)
left.add_rib(1., right_edges_end)

left_geta = sw.rotate(-np.pi+np.pi/2).parent(adapter).void(3.)
left_edges = [(0.5, half_t), (-0.5, half_t), (-0.5, -half_t), (0.5, -half_t)]
left_edges_end = [(0., 0.), (-0.5, 0.), (-0.5, -half_t), (0., -half_t)]
left = sw.rotate(-np.pi/2).parent(left_geta).void(lr_length)
left.add_ribs([0., 1.-2./lr_length], left_edges)
left.add_rib(1., left_edges_end)

# sw.start_display()
sw.generate_stl_binary(path, fname)