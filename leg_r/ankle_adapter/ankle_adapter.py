from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    module_length = 5.82+1.

    ankle_adapter_thickness = 6.5

    ankle_adapter_edges = [(-2.78,3.12),(-3.28,2.89),(-3.28,0.42),(-2.78,0.00),(2.78,0.00),(3.22,0.42),(3.22,3.12),(3.22,8.58),(-0.81,8.58),(-0.81,3.12)]
    ankle_adapter_edges =  ankle_adapter_edges[6:] + ankle_adapter_edges[:6]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    ankle_adapter_joint_geta_1 = sw.move_z_back(2.)
    ankle_adapter_joint = sw.parent(ankle_adapter_joint_geta_1).pole(4., 2.5, np.pi*2, 8, True)

    ankle_adapter_geta_1 = sw.parent(ankle_adapter_joint, 1.-1./4.).rotate(0., -np.pi/2.).void()
    ankle_adapter_geta_2 = sw.parent(ankle_adapter_geta_1).rotate_x(np.pi/2.)

    ankle_adapter = sw.parent(ankle_adapter_geta_2).void(Const.ankle_adapter_thickness)
    ankle_adapter.add_ribs(edges=Const.ankle_adapter_edges)
    sw.deformation(ankle_adapter, lambda x,y,z: (x,y,z-Const.ankle_adapter_thickness/2.))
    sw.deformation(ankle_adapter, ankle_adapter_deoformation)

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def ankle_adapter_deoformation(x,y,z):
    target = Const.ankle_adapter_edges
    range = 0.01
    if target[7-6][1] - range < y and y < target[7-6][1] + range:
        if 0. < z:
            return (x,y,z-1.5)
        else:
            return (x,y,z+1.5)
    return None

if __name__ == "__main__":
    main()