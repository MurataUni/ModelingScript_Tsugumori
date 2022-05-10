from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    rad_upper_fin = -np.pi/36.
    rad_under_fin = np.pi/36.

    tail_base_adapter = sw.pole(5., 1.5, 2.*np.pi, 32, True)

    tail_base_start_edges = [\
        (3.2, -2.8), (4.61, -2.8), (9.81, -2.8), (9.81, 2.8), (4.61, 2.8), \
        (3.2, 2.8), (0., 2.8), (0., -1.95), (0.8, -2.8)]
    tail_base_start_thickness = 4.4
    tail_base_start = sw.rotate(-np.pi/2.).parent(tail_base_adapter, 1.-1.5/5.).void(tail_base_start_thickness)
    tail_base_start.add_ribs([0.,1.], tail_base_start_edges)
    sw.deformation(tail_base_start, lambda x,y,z: (x,y,z-tail_base_start_thickness/2.))
    sw.deformation(tail_base_start, tail_base_start_deformation)

    tail_base_end_edges = [\
        (16.75,0.02),(18.82,1.01),(17.95,6.78),(15.98,6.71),(15.62,6.68),\
        (14.78,8.78),(12.59,10.07),(10.78,9.65),(9.58,8.38),(8.40,4.47),\
        (5.13,2.),(4.99,-0.68),(9.81,-2.9)]
    tail_base_end_thickness = 8.2
    tail_base_end = sw.rotate(-np.pi/2.).parent(tail_base_adapter, 1.-1.5/5.).void(tail_base_end_thickness)
    tail_base_end.add_ribs([0.,1.], tail_base_end_edges)
    sw.deformation(tail_base_end, lambda x,y,z: (x,y,z-tail_base_end_thickness/2.))
    sw.deformation(tail_base_end, tail_base_end_deformation)

    tail_upper_fin_base_edges = [\
        (0.,-0.89),(0.,2.07),(1.95,2.31),(3.55,2.8),(5.74,4.92),
        (10.78,4.8),(10.78,4.4),(15.88,4.1)]
    tail_upper_fin_base_thickness = 3.
    tail_upper_fin_base_geta_1 = sw.parent(tail_base_adapter, 1.-1.5/5.).void(12.19)
    tail_upper_fin_base_geta_2 = sw.parent(tail_upper_fin_base_geta_1).move_y(7.41)
    tail_upper_fin_base_geta_3 = sw.parent(tail_upper_fin_base_geta_2).rotate_x(rad_upper_fin)
    tail_upper_fin_base = sw.rotate(-np.pi/2.).parent(tail_upper_fin_base_geta_3).void(tail_upper_fin_base_thickness)
    tail_upper_fin_base.add_ribs([0.,1.], tail_upper_fin_base_edges)
    sw.deformation(tail_upper_fin_base, lambda x,y,z: (x,y,z-tail_upper_fin_base_thickness/2.))

    tail_upper_fin_edges = [(0.,0.), (-7.,7.6), (-1.3,89.), (0.,90.), (1.3,89.), (7.,7.6)]
    tail_upper_fin_thickness = 1.6
    tail_upper_fin = sw.rotate(np.pi/2., -np.pi/2.).parent(tail_upper_fin_base,0.).void(tail_upper_fin_thickness)
    tail_upper_fin.add_ribs([0.,1.], tail_upper_fin_edges)
    sw.deformation(tail_upper_fin, tail_upper_fin_deformation)
    sw.deformation(tail_upper_fin, lambda x,y,z: (x,y+(5.74+0.5),z-(4.4+0.4)))

    tail_under_fin_adapter_geta_1 = sw.parent(tail_base_adapter, 1.-1.5/5.).void(16.92)
    tail_under_fin_adapter_geta_2 = sw.parent(tail_under_fin_adapter_geta_1).move_y(3.5)
    tail_under_fin_adapter_geta_3 = sw.parent(tail_under_fin_adapter_geta_2).rotate_x(rad_under_fin)
    tail_under_fin_adapter = sw.parent(tail_under_fin_adapter_geta_3).rectangular(3.4, 4., 5.6)

    tail_under_fin_base_edges = [(0., 3.6), (4.5, -0.2), (3.6, -3.), (-3.6, -3.), (-4.5, -0.2)]
    tail_under_fin_base = sw.rotate(0., np.pi).parent(tail_under_fin_adapter, 0.5).void(9.)
    tail_under_fin_base.add_ribs((0.,1.), tail_under_fin_base_edges)

    tail_under_fin_edges = [\
        (0., 0.), (3.5, -0.5), (7., -5.6), (11.3, 9.), (4.8, 58.8), (0., 64.4),\
        (-4.8, 58.8), (-11.3, 9.), (-7., -5.6), (-3.5, -0.5)]
    tail_under_fin_thickness = 1.8
    tail_under_fin_geta_1 = sw.parent(tail_under_fin_base, 0.).rotate_x(-np.pi/2)
    tail_under_fin_geta_2 = sw.parent(tail_under_fin_geta_1, 0.).void(3.6)
    tail_under_fin = sw.rotate(0., np.pi).parent(tail_under_fin_geta_2).void(tail_under_fin_thickness)
    tail_under_fin.add_ribs([0.,1.], tail_under_fin_edges)
    sw.deformation(tail_under_fin, lambda x,y,z: (x,y,z-tail_under_fin_thickness/2.))
    sw.deformation(tail_under_fin, tail_under_fin_deformation)


    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def tail_base_start_deformation(x,y,z):
    range = 0.1
    z_mod = (4.6-3.)/2.
    if 3.2 + range < x:
        if z < 0.:
            return (x,y,z+z_mod)
        else:
            return (x,y,z-z_mod)
    return None

def tail_base_end_deformation(x,y,z):
    range = 0.1
    z_mod = (8.2-4.4)/2.
    if 16.75 + range < x:
        if z < 0.:
            return (x,y,z+z_mod)
        else:
            return (x,y,z-z_mod)
    return None

def tail_upper_fin_deformation(x,y,z):
    target = [(0.,0.), (-7.,7.6), (-1.3,89.), (0.,90.), (1.3,89.), (7.,7.6)]
    range = 0.01
    z_mod1_5 = 2.1
    z_mod2_4 = 0.39
    if target[1][0] - range < x and x < target[1][0] + range:
        return (x,y,z+z_mod1_5)
    elif target[2][0] - range < x and x < target[2][0] + range:
        return (x,y,z+z_mod2_4)
    elif target[4][0] - range < x and x < target[4][0] + range:
        return (x,y,z+z_mod2_4)
    elif target[5][0] - range < x and x < target[5][0] + range:
        return (x,y,z+z_mod1_5)
    return None

def tail_under_fin_deformation(x,y,z):
    range = 0.01
    z_mod_ratio = 3.8/4.5
    x_mod = 1.
    if x < 0. - range or 0. + range < x:
        if z < 0.:
            if x < 0.:
                return (x+x_mod,y,z-abs(x)*z_mod_ratio)
            else:
                return (x-x_mod,y,z-abs(x)*z_mod_ratio)
        else:
            return (x,y,z-abs(x)*z_mod_ratio)
    return None

if __name__ == "__main__":
    main()