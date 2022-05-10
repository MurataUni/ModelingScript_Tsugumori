from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

upperarm_length = 20.
upperarm_thickness = 9.
upperarm_width = 7.

edges = [(upperarm_width/2., upperarm_thickness/2.), (-upperarm_width/2., upperarm_thickness/2.), (-upperarm_width/2., -upperarm_thickness/2.), (upperarm_width/2., -upperarm_thickness/2.)]

upperarm = sw.void(20.)
upperarm.add_rib(0., edges.copy())
upperarm.add_rib(1.-4./upperarm_length, edges.copy())
end_edge = edges.copy()
end_edge[0] = (end_edge[0][0], end_edge[0][1]-1.5)
end_edge[1] = (end_edge[1][0], end_edge[1][1]-1.5)
end_edge[2] = (end_edge[2][0], end_edge[2][1]+2.5)
end_edge[3] = (end_edge[3][0], end_edge[3][1]+2.5)

upperarm.add_rib(1., end_edge)

sw.chamfering(upperarm, 0.5)

# sw.start_display()
sw.generate_stl_binary(path, fname)