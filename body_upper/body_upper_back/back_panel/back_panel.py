from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    rad_tail = np.pi/2.-np.pi/36.

    back_panel_thickness = 12.
    back_panel_edges = [\
        (-9.59, 3.49), (-10.58, 4.34), (-10.24, 12.17), (-8.74, 13.47), (-8.91, 15.09), \
        (-7.81, 18.2), (-7.87, 19.37), (-3.79, 25.12), (-0.22, 26.74), (0.96, 26.4), \
        (5.27, 21.78), (5.27, 21.25), (5.27, 0.3), (1.08, 0.3)]

    back_panel = sw.rotate(np.pi/2., np.pi).void(back_panel_thickness)
    back_panel.add_ribs((0., 1.), back_panel_edges)
    sw.deformation(back_panel, lambda x,y,z: (x,y,z-back_panel_thickness/2.))
    sw.deformation(back_panel, back_panel_deformation)

    back_panel_cover_thickness = 12.6
    back_panel_cover_edges = [\
        (1.43, -0.26), (0.69, -2.8), (-11.58, 1.86), (-8.91, 3.56), (-7.01, 4.56), (1.78, 1.35)]
    back_panel_cover = sw.rotate(np.pi/2., np.pi).void(back_panel_cover_thickness)
    back_panel_cover.add_ribs((0., 1.), back_panel_cover_edges)
    sw.deformation(back_panel_cover, lambda x,y,z: (x,y,z-back_panel_cover_thickness/2.))
    sw.deformation(back_panel_cover, back_panel_cover_deformation)

    back_panel_cover_r_geta_1 = sw.move_x(-6.)
    back_panel_cover_r = sw.parent(back_panel_cover_r_geta_1).load_submodule(os.path.join(path, 'back_panel_cover_r'))

    back_panel_cover_l_geta_1 = sw.move_x(6.)
    back_panel_cover_l = sw.parent(back_panel_cover_l_geta_1).load_submodule(os.path.join(path, 'back_panel_cover_r'))
    sw.deformation(back_panel_cover_l, lambda x,y,z: (-x,y,z))
    for triangle in back_panel_cover_l.monocoque_shell.triangles:
        triangle.inverse()

    back_panel_cover_center_thickess = 6.2+1.6
    back_panel_cover_center_edges = [(-5.11, 11.58), (-11.7, 14.39), (-9.66, 17.36)]
    back_panel_cover_center = sw.rotate(np.pi/2., np.pi).void(back_panel_cover_center_thickess)
    back_panel_cover_center.add_ribs([0.,1.], back_panel_cover_center_edges)
    sw.deformation(back_panel_cover_center, lambda x,y,z: (x,y,z-back_panel_cover_center_thickess/2.))

    tail_geta_1 = sw.void(1.6)
    tail_geta_2 = sw.parent(tail_geta_1).move_y(-24.73)
    tail_geta_3 = sw.parent(tail_geta_2).rotate_x(rad_tail)
    tail = sw.parent(tail_geta_3).load_submodule(os.path.join(path, 'tail'))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def back_panel_deformation(x,y,z):
    target = [\
        (-9.59, 3.49), (-10.58, 4.34), (-10.24, 12.17), (-8.74, 13.47), (-8.91, 15.09), \
        (-7.81, 18.2), (-7.87, 19.37), (-3.79, 25.12), (-0.22, 26.74), (0.96, 26.4), \
        (5.27, 21.78), (5.27, 21.25), (5.27, 0.3), (1.08, 0.3)]
    range = 0.01
    z_mod0_3 = (12.-8.4)/2.
    z_mod1_2 = (12.-6.2)/2.
    z_mod4 = (12.-8.)/2.
    z_mod5 = (12.-7.6)/2.
    z_mod6_7_8_9 = (12.-6.)/2.
    z_mod13 = (12.-11.)/2.
    if target[0][0]-range < x and x < target[0][0]+range:
        if z < 0.:
            return (x,y,z+z_mod0_3)
        else:
            return (x,y,z-z_mod0_3)
    elif target[1][0]-range < x and x < target[1][0]+range\
        or target[2][0]-range < x and x < target[2][0]+range:
        if z < 0.:
            return (x,y,z+z_mod1_2)
        else:
            return (x,y,z-z_mod1_2)
    elif target[3][0]-range < x and x < target[3][0]+range:
        if z < 0.:
            return (x,y,z+z_mod0_3)
        else:
            return (x,y,z-z_mod0_3)
    elif target[4][0]-range < x and x < target[4][0]+range:
        if z < 0.:
            return (x,y,z+z_mod4)
        else:
            return (x,y,z-z_mod4)
    elif target[5][0]-range < x and x < target[5][0]+range:
        if z < 0.:
            return (x,y,z+z_mod5)
        else:
            return (x,y,z-z_mod5)
    elif target[6][0]-range < x and x < target[6][0]+range\
        or target[7][0]-range < x and x < target[7][0]+range\
        or target[8][0]-range < x and x < target[8][0]+range\
        or target[9][0]-range < x and x < target[9][0]+range:
        if z < 0.:
            return (x,y,z+z_mod6_7_8_9)
        else:
            return (x,y,z-z_mod6_7_8_9)
    elif target[13][0]-range < x and x < target[13][0]+range:
        if z < 0.:
            return (x,y,z+z_mod13)
        else:
            return (x,y,z-z_mod13)
    return None

def back_panel_cover_deformation(x,y,z):
    target = [\
        (1.43, -0.26), (0.69, -2.8), (-11.58, 1.86), (-8.91, 3.56), (-7.01, 4.56), (1.78, 1.35)]
    range = 0.01
    z_mod1_2 = (12.6-7.2)/2.
    z_mod3_4 = (12.6-9.5)/2.
    if target[1][0]-range < x and x < target[1][0]+range:
        if z < 0.:
            return (x,y,z+z_mod1_2)
        else:
            return (x,y,z-z_mod1_2)
    elif target[2][0]-range < x and x < target[2][0]+range:
        if z < 0.:
            return (x,y,z+z_mod1_2)
        else:
            return (x,y,z-z_mod1_2)
    elif target[3][0]-range < x and x < target[3][0]+range:
        if z < 0.:
            return (x,y,z+z_mod3_4)
        else:
            return (x,y,z-z_mod3_4)
    elif target[4][0]-range < x and x < target[4][0]+range:
        if z < 0.:
            return (x,y,z+z_mod3_4)
        else:
            return (x,y,z-z_mod3_4)
    return None

if __name__ == "__main__":
    main()