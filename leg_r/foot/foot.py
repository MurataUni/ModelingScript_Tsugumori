from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

class Const:
    module_length = 6.5

    foot_side_thickness = 1.
    foot_center_thickness = 1.2+2.
    toe_anker_thickness = 1.5

    foot_side_edges = [(3.,3.5),(17.,7.),(18.,9.),(23.,10.5),(28.,10.5),(30.,6.5),(28.,3.),(23.,0.),(2.,0.),(0.,0.)]
    foot_center_edges = list(map(lambda t: (t[0]*1.01, t[1]*1.01), foot_side_edges[1:len(foot_side_edges)-2]))
    toe_anker_edges = [(2.,2.),(3.,3.),(15.,6.),(16.5,8.),(16.5,5.)] 

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    foot_geta_1 = sw.rotate_x(np.pi/2.)
    foot_geta_2 = sw.parent(foot_geta_1).rotate(np.pi).void()
    foot_geta_3 = sw.parent(foot_geta_2).rotate(0., -np.pi/2.).void()
    foot_geta_4 = sw.parent(foot_geta_3).rotate_x(np.pi/2.)
    foot_geta_5 = sw.parent(foot_geta_4).move_z_back(Const.foot_center_thickness/2.)

    foot_center = sw.parent(foot_geta_5).void(Const.foot_center_thickness)
    foot_center.add_ribs(edges=Const.foot_center_edges)

    foot_side_r = sw.parent(foot_center, 1.-1./Const.foot_center_thickness).void(Const.foot_side_thickness)
    foot_side_r.add_ribs(edges=Const.foot_side_edges)
    sw.deformation(foot_side_r, foot_side_r_deformation)

    foot_side_l = sw.parent(foot_center, 1./Const.foot_center_thickness).void(Const.foot_side_thickness)
    foot_side_l.add_ribs(edges=Const.foot_side_edges)
    sw.deformation(foot_side_l, foot_side_r_deformation)
    sw.deformation(foot_side_l, lambda x,y,z: (x,y,-z))
    for triangle in foot_side_l.monocoque_shell.triangles:
        triangle.inverse()

    toe_anker = sw.parent(foot_center, 0.5).void(Const.toe_anker_thickness)
    toe_anker.add_ribs(edges=Const.toe_anker_edges)
    sw.deformation(toe_anker, lambda x,y,z: (x,y,z-Const.toe_anker_thickness/2.))
    sw.deformation(toe_anker, toe_anker_deformation)

    sw.deformation_all(lambda x,y,z: (x-25.5,y-6.5,z))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def foot_side_r_deformation(x,y,z):
    target = Const.foot_side_edges
    range = 0.01
    thickness_center = Const.foot_side_thickness/2.
    x_ratio = 2./21.
    y_ratio = 1.2/(10.5-3.)
    if target[len(target)-1][0] - range < x and x < target[len(target)-1][0] + range:
        return None
    if thickness_center < z:
            return (x,y,z+x*x_ratio-(y-10.5)*y_ratio)
    return None

def toe_anker_deformation(x,y,z):
    target = Const.toe_anker_edges
    range = 0.01
    x_ratio = 2./21.
    y_ratio = 1.2/(10.5-3.)
    if target[3][1] - range < y and y < target[3][1] + range:
        if 0. < z:
            return (x,y,z-0.3)
        else:
            return (x,y,z+0.3)
    return None

if __name__ == "__main__":
    main()