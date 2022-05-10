from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

forearm_length = 30.
forearm_width = 7.
forearm_height = 6.

base = sw.rotate(np.pi).void(1.5)

edges = [(forearm_width/2, forearm_height/2), (-forearm_width/2, forearm_height/2), (-forearm_width/2, -forearm_height/2), (forearm_width/2, -forearm_height/2)]

edge_beginning = edges.copy()
edge_beginning[0] = (edge_beginning[0][0], edge_beginning[0][1] - 1.5)
edge_beginning[1] = (edge_beginning[1][0], edge_beginning[1][1] - 1.5)
scaled_edges_beginning = edges_util.scale(edge_beginning, 0.8)
center_edges_beginning = edges_util.center(edge_beginning)
center_scaled_edges_beginning = edges_util.center(scaled_edges_beginning)
y_translate = center_edges_beginning[1]-center_scaled_edges_beginning[1]
edges_util.translate(scaled_edges_beginning, y=y_translate)

forearm = sw.rotate(-np.pi).parent(base).void(forearm_length)
forearm.add_rib(0., scaled_edges_beginning)
forearm.add_rib(0.5/forearm_length, edge_beginning)
forearm.add_rib(3./forearm_length, edges.copy())
forearm.add_rib((forearm_length - 1.)/forearm_length, edges.copy())
forearm.add_rib(1., edges_util.scale(edges, 0.8))

mid_edges_1 = edges.copy()
mid_edges_1[0] = (mid_edges_1[0][0] - 1.5, mid_edges_1[0][1])
mid_edges_1[3] = (mid_edges_1[3][0] - 1.5, mid_edges_1[3][1])
forearm.add_rib(11./forearm_length, edges.copy())
forearm.add_rib(13./forearm_length, mid_edges_1)
forearm.add_rib(24./forearm_length, mid_edges_1.copy())
forearm.add_rib(26./forearm_length, edges.copy())

forearm.order_ribs()
sw.chamfering(forearm, 0.5)

armguard_attachment_1 = sw.parent(forearm, 0.).void(10.)
armguard_attachment_2 = sw.rotate(np.pi/2, np.pi/2).parent(armguard_attachment_1).void(forearm_height/2-1.)
armguard = sw.rotate(0., -np.pi/2).parent(armguard_attachment_2).load_submodule(os.path.join(path, 'armguard_r')).align_keel_size_to_monocoque_shell()

hand = sw.rotate(0., np.pi/2).parent(forearm).load_submodule(os.path.join(path, 'hand_r')).align_keel_size_to_monocoque_shell()

# sw.start_display()
sw.generate_stl_binary(path, fname)