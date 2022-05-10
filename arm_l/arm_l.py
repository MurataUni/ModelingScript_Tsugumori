from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    arm_r = sw.load_submodule(os.path.join(path, 'arm_r'))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            sw.deformation(ship, lambda x,y,z: (-x,y,z))
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()