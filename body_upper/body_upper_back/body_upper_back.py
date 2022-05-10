from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    rad_backpack_adapter = np.pi/3.
    rad_backpack_base = -np.pi/3.

    backpack_base_geta_1 = sw.void(16.5)
    backpack_base_geta_2 = sw.parent(backpack_base_geta_1).move_y(6.6)

    backpack_base_l_geta = sw.parent(backpack_base_geta_2).move_x(8.)
    backpack_base_r_geta = sw.parent(backpack_base_geta_2).move_x(-8.)

    backpack_base_l = sw.parent(backpack_base_l_geta).load_submodule(os.path.join(path, 'backpack_adapter_base_r'))
    sw.deformation(backpack_base_l, lambda x,y,z: (-x,y,z))
    for triangle in backpack_base_l.monocoque_shell.triangles:
        triangle.inverse()
    
    backpack_base_r = sw.parent(backpack_base_r_geta).load_submodule(os.path.join(path, 'backpack_adapter_base_r'))

    back_panel = sw.parent(backpack_base_geta_2).load_submodule(os.path.join(path, 'back_panel'))

    backpack_adapter_geta_1 = sw.parent(backpack_base_geta_2).void(10.56-3.2)
    backpack_adapter_geta_2 = sw.parent(backpack_adapter_geta_1).move_y(7.-5.2)
    backpack_adapter_geta_3 = sw.parent(backpack_adapter_geta_2).rotate_x(rad_backpack_adapter)

    backpack_adapter_l_geta = sw.parent(backpack_adapter_geta_3).move_x(8.)
    backpack_adapter_r_geta = sw.parent(backpack_adapter_geta_3).move_x(-8.)

    backpack_adapter_l = sw.parent(backpack_adapter_l_geta).load_submodule(os.path.join(path, 'backpack_adapter'))
    backpack_adapter_r = sw.parent(backpack_adapter_r_geta).load_submodule(os.path.join(path, 'backpack_adapter'))

    backpack_base_geta_1 = sw.parent(backpack_adapter_geta_3).move_y(1.79)
    backpack_base_geta_2 = sw.parent(backpack_base_geta_1).void(19.24)
    backpack_base_geta_3 = sw.parent(backpack_base_geta_2).rotate_x(rad_backpack_base)

    backpack_base_l_geta = sw.parent(backpack_base_geta_3).move_x(8.)
    backpack_base_r_geta = sw.parent(backpack_base_geta_3).move_x(-8.)

    backpack_adapter_l = sw.parent(backpack_base_l_geta).load_submodule(os.path.join(path, 'backpack_base'))
    backpack_adapter_r = sw.parent(backpack_base_r_geta).load_submodule(os.path.join(path, 'backpack_base'))

    backpack_geta_1 = sw.parent(backpack_base_geta_3).move_y(2.33)
    backpack_geta_2 = sw.parent(backpack_geta_1).void(6.)

    backpack = sw.parent(backpack_geta_2).load_submodule(os.path.join(path, 'backpack'))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)


if __name__ == "__main__":
    main()