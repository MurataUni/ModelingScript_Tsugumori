from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    base_edges = [(-3.71,-5.46),(-3.71,4.13),(4.30,15.74),(6.02,15.74),(6.02,-7.17)]
    base_thickness = 6.
    base = sw.rotate(-np.pi/2.).void(base_thickness)
    base.add_ribs([0.,1.], base_edges)
    sw.deformation(base, lambda x,y,z: (x,y,z-base_thickness/2.))

    adapter_edges = [(7.,-3.22),(7.,7.87),(3.31,7.87),(3.31,-3.22)]
    adapter_thickness = 3.2
    adapter = sw.rotate(-np.pi/2.).void(adapter_thickness)
    adapter.add_ribs([0.,1.], adapter_edges)
    sw.deformation(adapter, lambda x,y,z: (x,y,z-adapter_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()