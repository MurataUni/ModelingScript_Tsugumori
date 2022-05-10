from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

rad_f1_j = (-np.pi/36, np.pi/9, np.pi/9)
rad_f2_j = (-np.pi/36, np.pi/8, np.pi/8)
rad_f3_j = (0., np.pi/7, np.pi/7)
rad_f4_j = (np.pi/36, np.pi/6, np.pi/6)

f_widt = 1.4
f_vert = 2.
f_side_gap = 0.1
palm_widt = (f_widt + f_side_gap)*4+f_side_gap
palm_vert = f_vert
palm_length = 10.
gauntlet_thickness = 0.6
gauntlet_widt = palm_widt + 0.8

f_subtended = np.pi/36

palm = sw.rectangular(palm_widt, palm_vert, palm_length)
path1 = sw.rotate(np.pi/2, 0.).parent(palm).void(palm_widt/2)
path2 = sw.rotate(-np.pi, 0.).parent(path1).void()
f_base = sw.parent(path2).void(palm_widt)
bases = []
for i in range(4):
    subtended = (1.5 - i) * f_subtended
    bases.append(sw.rotate(np.pi/2 + subtended, 0.).parent(f_base, (f_side_gap*(i+1) + f_widt*i + f_widt/2)/palm_widt).void())

rads = [rad_f1_j, rad_f2_j, rad_f3_j, rad_f4_j]

for i in range(4):
    f_j3 = sw.rotate(rads[i][0], -np.pi/2).parent(bases[i]).void(0.)
    f_p3 = sw.rotate(0., np.pi/2).parent(f_j3).load_submodule(os.path.join(path, 'finger_3')).align_keel_size_to_monocoque_shell()
    f_j2 = sw.rotate(rads[i][1], -np.pi/2).parent(f_p3).void(0.)
    f_p2 = sw.rotate(0., np.pi/2).parent(f_j2).load_submodule(os.path.join(path, 'finger_2')).align_keel_size_to_monocoque_shell()
    f_j1 = sw.rotate(rads[i][2], -np.pi/2).parent(f_p2).void(0.)
    f_p1 = sw.rotate(0., np.pi/2).parent(f_j1).load_submodule(os.path.join(path, 'finger_1')).align_keel_size_to_monocoque_shell()

#(-0.1, palm_vert/2), (0., palm_vert/2-0.1), (0.1, palm_vert/2)
gauntlet = sw.parent(palm, 0.1/palm_length).void(palm_length)
gauntlet.add_rib(0., [(gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, 0.), (gauntlet_widt/2, 0.)])
gauntlet.add_rib(0.45, [(gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, 0.), (gauntlet_widt/2, 0.)])
gauntlet.add_rib(0.55, [(gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, -palm_vert/2+0.1), (gauntlet_widt/2, -palm_vert/2+0.1)])
gauntlet.add_rib(1., [(gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, palm_vert/2+gauntlet_thickness), (-gauntlet_widt/2, -palm_vert/2+0.1), (gauntlet_widt/2, -palm_vert/2+0.1)])

for rib in gauntlet.ribs:
    rib.edges[1:1] = [(0.1, palm_vert/2+gauntlet_thickness), (0., palm_vert/2+gauntlet_thickness-0.1), (-0.1, palm_vert/2+gauntlet_thickness)]

# sw.start_display()
sw.generate_stl_binary(path, fname)