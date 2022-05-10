from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    leg_cover_front_upper_thickness = 10.
    leg_cover_front_upper_width = 7.
    leg_cover_front_upper_edges = [\
        (-8.34,-11.31), (-9.15,-1.43), (-3.32,3.54), (-3.32+leg_cover_front_upper_width,-1.43), (-8.34+leg_cover_front_upper_width,-11.31)]
    
    leg_cover_front_thickness = 3.2
    leg_cover_front_edges_start = [\
        (-4.5, -5.), (4.5, -5.), (4.5, 40.), (2.6, 58.), (-2.6, 58.), (-4.5, 40.)]
    leg_cover_front_edges_start = leg_cover_front_edges_start[2:] + leg_cover_front_edges_start[:2]
    leg_cover_front_edges_end = [\
        (-3.2, -5.), (3.2, -5.), (3.2, 40.), (1.5, 58.), (-1.5, 58.), (-3.2, 40.)]
    leg_cover_front_edges_end = leg_cover_front_edges_end[2:] + leg_cover_front_edges_end[:2]

    leg_cover_thickness = 2.
    leg_cover_r_outer_edges = [\
        (-3.32,3.54),(-5.93,-11.31),(-8.34,-11.31),(-9.15,-1.43),(-7.33,31.48),(-5.29,29.56),(-4.99,30.30),(-6.32,33.49),(1.89,38.83),(2.48,35.78),(3.52,35.78),(3.98,39.47),(15.32,37.52),(16.60,33.52),(15.93,31.45),(17.02,30.69),(19.87,32.80),(21.74,33.25),(23.56,30.79),(19.75,19.72)]
    leg_cover_r_inner_edges = [\
        (-3.32,3.54),(-5.93,-11.31),(-8.34,-11.31),(-9.15,-1.43),(-7.33,31.48),(-7.28,31.97),(-7.03,34.08),(-6.84,34.28),(1.65,39.84),(2.31,40.30),(3.66,40.48),(4.01,40.43),(16.20,38.36),(17.56,34.80),(16.92,32.70),(17.88,31.72),(21.02,34.13),(22.60,34.35),(24.61,31.30),(20.48,20.04)]
    leg_cover_r_deform_r = 3.

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    leg_cover_geta_1 = sw.move_y(8.)
    leg_cover_geta_2 = sw.parent(leg_cover_geta_1).rotate(0., -np.pi/2.).void(5.5)
    leg_cover_geta_3 = sw.parent(leg_cover_geta_2).rotate_x(np.pi/2.)
    leg_cover_geta_4 = sw.parent(leg_cover_geta_3).move_z_back(Const.leg_cover_front_upper_thickness/2.)

    leg_cover_front_upper = sw.parent(leg_cover_geta_4).void(Const.leg_cover_front_upper_thickness)
    leg_cover_front_upper.add_ribs(edges=Const.leg_cover_front_upper_edges)

    leg_cover_r = sw.parent(leg_cover_front_upper, 1.-1./Const.leg_cover_front_upper_thickness).void(Const.leg_cover_thickness)
    leg_cover_r.add_ribs([0.,0.2],Const.leg_cover_r_inner_edges)
    leg_cover_r.add_rib(1.,Const.leg_cover_r_outer_edges)
    sw.deformation(leg_cover_r, leg_cover_r_deformation)
    
    leg_cover_l = sw.parent(leg_cover_front_upper, 1./Const.leg_cover_front_upper_thickness).void(Const.leg_cover_thickness)
    leg_cover_l.add_ribs([0.,0.2],Const.leg_cover_r_inner_edges)
    leg_cover_l.add_rib(1.,Const.leg_cover_r_outer_edges)
    sw.deformation(leg_cover_l, leg_cover_r_deformation)
    sw.deformation(leg_cover_l,lambda x,y,z: (x,y,-z))
    for triangle in leg_cover_l.monocoque_shell.triangles:
        triangle.inverse()

    leg_cover_front_gata_1 = sw.parent(leg_cover_front_upper, 0.5).rotate(-np.pi/2.).void()
    leg_cover_front_geta_2 = sw.parent(leg_cover_front_gata_1).void(4.)
    leg_cover_ftont = sw.parent(leg_cover_front_geta_2).void(Const.leg_cover_front_thickness)
    leg_cover_ftont.add_rib(0., Const.leg_cover_front_edges_start)
    leg_cover_ftont.add_rib(1., Const.leg_cover_front_edges_end)
    sw.deformation(leg_cover_ftont, leg_cover_front_deformation)

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def leg_cover_r_deformation(x,y,z):
    if Const.leg_cover_r_outer_edges[0][0] < x:
        return (x,y,z+Const.leg_cover_r_deform_r)
    return None

def leg_cover_front_deformation(x,y,z):
    if Const.leg_cover_front_edges_start[3-2][0] == x\
        and Const.leg_cover_front_edges_start[3-2][1] == y:
        return (x,y,z+Const.leg_cover_front_thickness/2.)
    elif Const.leg_cover_front_edges_start[4-2][0] == x\
        and Const.leg_cover_front_edges_start[4-2][1] == y:
        return (x,y,z+Const.leg_cover_front_thickness/2.)
    return None

if __name__ == "__main__":
    main()