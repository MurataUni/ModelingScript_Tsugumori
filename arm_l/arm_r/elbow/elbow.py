from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

elbow_length = 12.
elbow_width = 4.5
elbow_thickness = 3.

edges = [(0., -1.5), (0., 1.5), (2., elbow_width/2), (10., elbow_width/2), (elbow_length, 1.5), (elbow_length, -1.5), (10., -elbow_width/2), (2., -elbow_width/2)]

base_1 = sw.rotate(-np.pi).void(3.)
base_2 = sw.rotate(-np.pi/2+np.pi).parent(base_1).void(0.)

elbow_base = sw.rotate(-np.pi).parent(base_2).void(elbow_thickness/2)
elbow = sw.rotate(np.pi).parent(elbow_base).void(elbow_thickness)
elbow.add_rib(0., edges.copy())
elbow.add_rib(1., edges.copy())

# sw.start_display()
sw.generate_stl_binary(path, fname, divided=False)
