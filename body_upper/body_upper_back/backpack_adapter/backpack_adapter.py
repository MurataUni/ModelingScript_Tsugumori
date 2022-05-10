from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    adapter_edges =[\
        (4.82,-2.15),(-0.63,-4.33),(-3.20,-3.33),(-4.57,0.48),(-3.57,2.87),\
        (3.26,5.75),(20.26,5.75),(21.69,4.94),(22.52,4.00),(23.18,1.53),\
        (22.52,-0.52),(21.69,-1.38),(20.26,-2.15)]
    adapter_thickness = 2.6
    adapter = sw.rotate(-np.pi/2.).void(adapter_thickness)
    adapter.add_ribs([0.,1.], adapter_edges)
    sw.deformation(adapter, lambda x,y,z: (x,y,z-adapter_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()