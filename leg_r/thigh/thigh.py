from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    thigh_thickness = 10.
    module_length = 19.84
    knee_joint_radius = module_length - 14.37
    knee_joint_edges = (lambda r,y_o:\
        [(-r*np.sin((n/8)*np.pi/2.), y_o-r*np.cos((n/8)*np.pi/2.)) for n in range(8 + 1)])(knee_joint_radius, module_length)
    thigh_edges = [(-3.25,0.00),(5.78,0.00),(10.48,2.44),(10.48,9.10),(4.04,14.04),(2.44,14.37)]\
        + knee_joint_edges\
        + [(-5.47,24.07),(-9.76,24.07),(-10.52,22.30),(-10.52,-10.30),(-6.63,-12.96),(-6.15,-3.07)]
    y_move = 1. #rotated model's y -> -x

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    thigh_geta_1 = sw.rotate(0., -np.pi/2.).void()
    thigh_geta_2 = sw.parent(thigh_geta_1).rotate_x(np.pi/2.)
    thigh = sw.parent(thigh_geta_2).void(Const.thigh_thickness)
    thigh.add_ribs(edges=Const.thigh_edges)
    sw.deformation(thigh, lambda x,y,z: (x-Const.y_move,y,z-Const.thigh_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()