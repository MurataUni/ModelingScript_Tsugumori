from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    module_length = 13.54
    y_move = -3.31 #rotated model's -y -> x
    
    knee_joint_outer_thickness = 9.5
    upper_arc_radius = 5.99
    upper_arc_edges = (lambda r: \
        [(-r*np.cos((n/16)*np.pi), -r*np.sin((n/16)*np.pi)) for n in range(16 + 1)])(upper_arc_radius)
    lower_arc_radius = 7.93
    lower_arc_origin = (3.31, 13.54)
    lower_arc_edges = (lambda r, o: \
        [(o[0]+r*np.cos((n/16)*np.pi), o[1]+r*np.sin((n/16)*np.pi)) for n in range(16 + 1)])(lower_arc_radius, lower_arc_origin)
    knee_joint_edges = upper_arc_edges[:len(upper_arc_edges)-2] + lower_arc_edges\
        + [(lower_arc_origin[0]-lower_arc_radius, 4.7),(-upper_arc_radius, 2.7)]
    
    knee_joint_inner_thickness = 7.5
    knee_joint_inner_edges = [(0.,18.77),(-9.07,18.77),(-9.07,12.47),(-8.54,12.31),(-8.54,4.7),(0.,4.7)]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    knee_joint_geta_1 = sw.rotate(0., -np.pi/2.).void()
    knee_joint_geta_2 = sw.parent(knee_joint_geta_1).rotate_x(np.pi/2.)

    knee_joint_outer = sw.parent(knee_joint_geta_2).void(Const.knee_joint_outer_thickness)
    knee_joint_outer.add_ribs(edges=Const.knee_joint_edges)
    sw.deformation(knee_joint_outer, lambda x,y,z: (x,y,z-Const.knee_joint_outer_thickness/2.))

    knee_joint_inner = sw.parent(knee_joint_geta_2).void(Const.knee_joint_inner_thickness)
    knee_joint_inner.add_ribs(edges=Const.knee_joint_inner_edges)
    sw.deformation(knee_joint_inner, lambda x,y,z: (x,y,z-Const.knee_joint_inner_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()