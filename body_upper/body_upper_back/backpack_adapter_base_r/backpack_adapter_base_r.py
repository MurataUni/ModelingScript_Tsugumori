from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    thickness = 5.5

    base_edges = [\
        (2.86, 2.82), (-4.94, -6.42), (-9.8, -7.), (-10.56, -5.46), (-10.56, 1.3), \
        (-7.52, 7.46), (-4.23, 10.48), (-2., 17.83), (2.86, 18.93), (2.86, 10.48)]

    base_r = sw.rotate(np.pi/2., np.pi).void(thickness)
    base_r.add_ribs([0., 1.], base_edges)
    sw.deformation(base_r, lambda x,y,z: (x,y,z-thickness/2.))
    sw.deformation(base_r, base_r_deformation)

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def base_r_deformation(x,y,z):
    range = 0.1
    if 10.48 + range < y:
        if z > 0.:
            return (x, y, z-2.)
    return None

if __name__ == "__main__":
    main()