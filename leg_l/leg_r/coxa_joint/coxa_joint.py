from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    joint_length = 6.4
    joint_adapter_length = 5.
    module_gap_1_2 = 3.
    module_length = joint_adapter_length + module_gap_1_2
    coxa_joint_thickness = 9.

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    coxa_joint_radius_end = 5.
    coxa_joint_radius_mid = Const.joint_length
    coxa_joint = sw.pole(Const.coxa_joint_thickness, coxa_joint_radius_end, 2*np.pi, 32)
    coxa_joint.add_ribs(\
        [1./Const.coxa_joint_thickness, 1.-1./Const.coxa_joint_thickness],\
        edges_util.scale(coxa_joint.get_rib_start(coxa_joint).edges.copy(), coxa_joint_radius_mid/coxa_joint_radius_end))
    coxa_joint.order_ribs()

    coxa_joint_adapter_edges_start = [(2.,6.),(-2.,6.),(-2.,-6.),(2.,-6.)]
    coxa_joint_adapter_edges_end = [(2.,4.6),(-2.,4.6),(-2.,-4.6),(2.,-4.6)]
    coxa_joint_adapter_geta_1 = sw.rotate(np.pi/2., -np.pi/2.).parent(coxa_joint, 0.5).void(Const.module_gap_1_2)
    coxa_joint_adapter = sw.parent(coxa_joint_adapter_geta_1).void(Const.joint_adapter_length)
    coxa_joint_adapter.add_rib(0., coxa_joint_adapter_edges_start)
    coxa_joint_adapter.add_rib(1., coxa_joint_adapter_edges_end)
    
    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()