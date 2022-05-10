from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    accesssory_edges = [(0.,-0.5),(0.,0.8),(4.,3.),(11.,3.),(12.6,5.6),(14.4,5.6),(16.,0.),(16.,-0.5)]
    accessory_thickness = 1.
    accessory_interval = 0.8

    base_1 = sw.rotate(-np.pi/2.).void()
    base_2 = sw.rotate(0.,-np.pi/2.).parent(base_1).void()

    accessory_1 = sw.parent(base_2).void(accessory_thickness)
    accessory_1.add_ribs([0.,1.], accesssory_edges)
    sw.deformation(accessory_1, lambda x,y,z: (x,y,z-1.5*accessory_interval-2*accessory_thickness))

    accessory_2 = sw.parent(base_2).void(accessory_thickness)
    accessory_2.add_ribs([0.,1.], accesssory_edges)
    sw.deformation(accessory_2, lambda x,y,z: (x,y,z-0.5*accessory_interval-accessory_thickness))

    accessory_3 = sw.parent(base_2).void(accessory_thickness)
    accessory_3.add_ribs([0.,1.], accesssory_edges)
    sw.deformation(accessory_3, lambda x,y,z: (x,y,z+0.5*accessory_interval))

    accessory_4 = sw.parent(base_2).void(accessory_thickness)
    accessory_4.add_ribs([0.,1.], accesssory_edges)
    sw.deformation(accessory_4, lambda x,y,z: (x,y,z+1.5*accessory_interval+accessory_thickness))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()