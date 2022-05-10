from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    module_length = 10.5

    foot_adapter_thickness = 4.
    foot_adapter_height = 7.2

    foot_adapter_edges = [\
        (-0.8*foot_adapter_height/2.,-foot_adapter_height/(2.*2.)),(-0.8*foot_adapter_height/2.,foot_adapter_height/(2.*2.)),\
        (0.,foot_adapter_height/2.),(module_length,foot_adapter_height/2.),\
        (module_length+0.8*foot_adapter_height/2.,foot_adapter_height/(2.*2.)),(module_length+0.8*foot_adapter_height/2.,-foot_adapter_height/(2.*2.)),\
        (module_length,-foot_adapter_height/2.),(0.,-foot_adapter_height/2.)]

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    foot_adapter = sw.rotate(-np.pi/2.).void(Const.foot_adapter_thickness)
    foot_adapter.add_ribs(edges=Const.foot_adapter_edges)
    sw.deformation(foot_adapter, lambda x,y,z: (x,y,z-Const.foot_adapter_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()