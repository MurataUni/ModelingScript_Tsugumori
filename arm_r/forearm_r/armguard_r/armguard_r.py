from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

attachment_thickness = 2.
attachment_length = 10.
attachment_width = 3.

upper_thickness = 1.
upper_length = 22.5
upper_width = 9.

outer_thickness = 2.
outer_length = 40.
outer_width = 13.

attachment = sw.rectangular(attachment_width, attachment_length, attachment_thickness)
attachment_adapter_1 = sw.rotate(-np.pi/2, -np.pi/2).parent(attachment, 0.75).void(6.)
attachment_adapter_2 = sw.rotate(np.pi/2).parent(attachment_adapter_1).void(0.)
attachment_adapter_3 = sw.rotate(np.pi/2, np.pi/2).parent(attachment_adapter_2).void(4.)

edge_upper = [(0., 0.), (0., -9.), (-upper_width, -upper_length), (-upper_width, 0.)]

obj_upper = sw.rotate(-np.pi/2).parent(attachment_adapter_3).void(upper_thickness)
obj_upper.add_rib(0., edge_upper)
obj_upper.add_rib(1., edge_upper)

adapter = sw.rotate(-np.pi/2).parent(obj_upper).void(8.)

edges_outer = [(0., 0.), (0., -outer_length), (-9., -outer_length), (-outer_width, -30), (-outer_width, 0.)]
edges_outer_2 = [(0., 0.), (0., -outer_length+0.7), (-9.+2., -outer_length+0.7), (-outer_width+2., -30), (-outer_width+2., 0.)]

obj_outer = sw.parent(adapter).void(outer_thickness)
obj_outer.add_rib(0., edges_util.translate(edges_outer, y=8))
obj_outer.add_rib(1., edges_util.translate(edges_outer_2, y=8))

# sw.start_display()
sw.generate_stl_binary(path, fname)