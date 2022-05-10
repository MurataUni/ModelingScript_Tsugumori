from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    shin_back_length = 36.46
    shin_rotation_radius = 9.2
    module_length = shin_back_length + shin_rotation_radius
    y_move = 2.5 #rotated model's -y -> x
    
    shin_upper_thickness = 11.2
    shin_back_thickness = 8.2
    shin_front_thickness = 7.2
    shin_front_lower_cover_length = 7.

    shin_upper_edges = [(-4.97,-0.77),(-4.46,-1.78),(8.91,-5.33),(10.38,-3.98),(7.48,7.50),(1.60,8.56),(0.75,8.25)]
    shin_back_edges = [(1.49,6.36),(7.19,6.36),(7.19,23.34),(10.22,28.42),(10.22,36.42),(9.24,37.91),(8.62,37.62),(8.62,36.46),(3.88,36.46),(3.88,33.47),(1.49,30.90)]
    shin_front_edges = [(0.,0.5),(5.36,0.5),(10.55,8.08),(10.55,33.45),(13.01,36.06),(13.01,40.49),(6.33,40.49),(5.23,39.04),(5.23,11.73),(0.19,8.77),(0.,8.13)]
    shin_front_lower_cover_edges = [(-3.2,1.),(3.2,1.),(3.5,-1.2),(-3.5,-1.2)]

    shin_front_y_move = shin_back_length - 40.49
    shin_front_x_move = -7.

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    shin_geta_1 = sw.void(Const.shin_rotation_radius)
    shin_geta_2 = sw.parent(shin_geta_1).move_y(Const.y_move)
    shin_geta_3 = sw.parent(shin_geta_2).rotate(0., -np.pi/2.).void()
    shin_geta_4 = sw.parent(shin_geta_3).rotate_x(np.pi/2.)

    shin_upper = sw.parent(shin_geta_4).void(Const.shin_upper_thickness)
    shin_upper.add_ribs(edges=Const.shin_upper_edges)
    sw.deformation(shin_upper, lambda x,y,z: (x,y,z-Const.shin_upper_thickness/2.))

    shin_back = sw.parent(shin_geta_4).void(Const.shin_back_thickness)
    shin_back.add_ribs(edges=Const.shin_back_edges)
    sw.deformation(shin_back, lambda x,y,z: (x,y,z-Const.shin_back_thickness/2.))

    shin_front = sw.parent(shin_geta_4).void(Const.shin_front_thickness)
    shin_front.add_ribs(edges=Const.shin_front_edges)
    sw.deformation(shin_front,\
        lambda x,y,z: (x+Const.shin_front_x_move,y+Const.shin_front_y_move,z-Const.shin_front_thickness/2.))
    
    shin_front_lower_cover_geta_1 = sw.parent(shin_geta_2).void(35.5)
    shin_front_lower_cover_geta_2 = sw.parent(shin_front_lower_cover_geta_1).move_y(1.)
    shin_front_lower_cover_geta_3 = sw.parent(shin_front_lower_cover_geta_2).rotate_x(-np.pi/4.)
    shin_front_lower_cover = sw.parent(shin_front_lower_cover_geta_3).void(Const.shin_front_lower_cover_length)
    shin_front_lower_cover.add_ribs(edges=Const.shin_front_lower_cover_edges)
    sw.deformation(shin_front_lower_cover, shin_front_lower_cover_deformation)

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def shin_front_lower_cover_deformation(x,y,z):
    range = 0.1
    if Const.shin_front_lower_cover_length - range < z and z < Const.shin_front_lower_cover_length + range:
        if 0. < x:
            if 0. < y:
                return (x-1.5,y,z-0.5)
            else:
                return (x-1.,y+1.,z)
        else:
            if 0. < y:
                return (x+1.5,y,z-0.5)
            else:
                return (x+1.,y+1.,z)
    return None

if __name__ == "__main__":
    main()