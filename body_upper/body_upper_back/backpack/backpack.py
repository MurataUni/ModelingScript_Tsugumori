from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    backpack_tip_slider = 0.-45. # max 60.

    base = sw.rotate(0., -np.pi/2.).void()

    base_panel_edges = [\
        (-39.91,-8.11),(-41.84,-9.68),(-40.41,-12.27),(23.64,-19.97),(66.18,-18.81),\
        (66.10,-16.39),(58.98,-14.64),(70.06,-9.65),(70.06,-7.20),(69.39,-6.79),\
        (69.39,6.79),(70.06,7.20),(70.06,9.65),(58.98,14.64),(66.10,16.39),\
        (66.18,18.81),(23.64,19.97),(-40.41,12.27),(-41.84,9.68),(-39.91,8.11)]
    base_panel_thickness = 2.
    base_panel = sw.parent(base).void(base_panel_thickness)
    base_panel.add_ribs([0.,1.], base_panel_edges)
    sw.deformation(base_panel, base_panel_deformation)

    base_side_r_edges = [\
        (-41.84,-9.68),(-40.41,-12.27),(23.64,-19.97),(66.18,-18.81),\
        (66.10,-16.39),(30.06,-9.85),(26.56,-14.37)]
    base_side_l_edges = [\
        (-41.84,9.68),(-40.41,12.27),(23.64,19.97),(66.18,18.81),\
        (66.10,16.39),(30.06,9.85),(26.56,14.37)]
    base_side_thickness = 2.

    base_side_r = sw.parent(base).void(base_side_thickness)
    base_side_r.add_ribs([0., 0.5, 1.], base_side_r_edges)
    sw.deformation(base_side_r, lambda x,y,z: (x,y,z-1.))
    sw.deformation(base_side_r, base_side_r_deformation)

    base_side_l = sw.parent(base).void(base_side_thickness)
    base_side_l.add_ribs([0., 0.5, 1.], base_side_l_edges)
    sw.deformation(base_side_l, lambda x,y,z: (x,y,z-1.))
    sw.deformation(base_side_l, base_side_l_deformation)

    accesory_panel_1_r_edges = [\
        (-38.37,-10.29),(-38.37,-5.95),(-36.71,-4.87),(-30.26,-4.87),(-26.71,-8.11),(-26.71,-10.29)]
    accesory_panel_1_l_edges = [\
        (-38.37,10.29),(-38.37,5.95),(-36.71,4.87),(-30.26,4.87),(-26.71,8.11),(-26.71,10.29)]
    accesory_panel_1_thickness = 2.
    accesory_panel_1_r = sw.parent(base).void(accesory_panel_1_thickness)
    accesory_panel_1_r.add_ribs([0.,1.], accesory_panel_1_r_edges)
    sw.deformation(accesory_panel_1_r, lambda x,y,z: (x,y,z-accesory_panel_1_thickness+1.))
    accesory_panel_1_l = sw.parent(base).void(accesory_panel_1_thickness)
    accesory_panel_1_l.add_ribs([0.,1.], accesory_panel_1_l_edges)
    sw.deformation(accesory_panel_1_l, lambda x,y,z: (x,y,z-accesory_panel_1_thickness+1.))

    accesory_panel_2_r_edges = [\
        (-26.39,-11.20),(-23.53,-5.95),(-14.84,-5.95),(-13.53,-11.20)]
    accesory_panel_2_l_edges = [\
        (-26.39,11.20),(-23.53,5.95),(-14.84,5.95),(-13.53,11.20)]
    accesory_panel_2_thickness = 3.
    accesory_panel_2_r = sw.parent(base).void(accesory_panel_2_thickness)
    accesory_panel_2_r.add_ribs([0.,1.], accesory_panel_2_r_edges)
    sw.deformation(accesory_panel_2_r, lambda x,y,z: (x,y,z-accesory_panel_2_thickness+1.))
    accesory_panel_2_l = sw.parent(base).void(accesory_panel_2_thickness)
    accesory_panel_2_l.add_ribs([0.,1.], accesory_panel_2_l_edges)
    sw.deformation(accesory_panel_2_l, lambda x,y,z: (x,y,z-accesory_panel_2_thickness+1.))

    accesory_panel_3_r_edges = [\
        (11.17,-13.38),(12.89,-8.19),(29.27,-8.89),(29.77,-9.97),(25.74,-15.10)]
    accesory_panel_3_l_edges = [\
        (11.17,13.38),(12.89,8.19),(29.27,8.89),(29.77,9.97),(25.74,15.10)]
    accesory_panel_3_thickness = 3.5
    accesory_panel_3_r = sw.parent(base).void(accesory_panel_3_thickness)
    accesory_panel_3_r.add_ribs([0.,1.], accesory_panel_3_r_edges)
    sw.deformation(accesory_panel_3_r, lambda x,y,z: (x,y,z-accesory_panel_3_thickness+1.))
    accesory_panel_3_l = sw.parent(base).void(accesory_panel_3_thickness)
    accesory_panel_3_l.add_ribs([0.,1.], accesory_panel_3_l_edges)
    sw.deformation(accesory_panel_3_l, lambda x,y,z: (x,y,z-accesory_panel_3_thickness+1.))

    accesory_panel_4_r_edges = [\
        (28.37,-2.65),(40.64,-2.65),(42.13,-3.59),(42.13,-6.59),(39.24,-9.56),(31.58,-8.16)]
    accesory_panel_4_l_edges = [\
        (28.37,2.65),(40.64,2.65),(42.13,3.59),(42.13,6.59),(39.24,9.56),(31.58,8.16)]
    accesory_panel_4_thickness = 2.
    accesory_panel_4_r = sw.parent(base).void(accesory_panel_4_thickness)
    accesory_panel_4_r.add_ribs([0.,1.], accesory_panel_4_r_edges)
    sw.deformation(accesory_panel_4_r, lambda x,y,z: (x,y,z-accesory_panel_4_thickness+1.))
    accesory_panel_4_l = sw.parent(base).void(accesory_panel_4_thickness)
    accesory_panel_4_l.add_ribs([0.,1.], accesory_panel_4_l_edges)
    sw.deformation(accesory_panel_4_l, lambda x,y,z: (x,y,z-accesory_panel_4_thickness+1.))

    accesory_panel_5_r_edges = [\
        (39.27,-12.54),(42.48,-8.80),(48.95,-10.32),(52.19,-14.93)]
    accesory_panel_5_l_edges = [\
        (39.27,12.54),(42.48,8.80),(48.95,10.32),(52.19,14.93)]
    accesory_panel_5_thickness = 2.
    accesory_panel_5_r = sw.parent(base).void(accesory_panel_5_thickness)
    accesory_panel_5_r.add_ribs([0.,1.], accesory_panel_5_r_edges)
    sw.deformation(accesory_panel_5_r, lambda x,y,z: (x,y,z-accesory_panel_5_thickness+1.))
    accesory_panel_5_l = sw.parent(base).void(accesory_panel_5_thickness)
    accesory_panel_5_l.add_ribs([0.,1.], accesory_panel_5_l_edges)
    sw.deformation(accesory_panel_5_l, lambda x,y,z: (x,y,z-accesory_panel_5_thickness+1.))

    shell_edges_r = [\
        (-47.39,0.),\
        (-48.88,-3.51),(-40.91,-8.11),(-42.84,-9.68),(-41.41,-12.27),(23.64,-19.97),\
        (66.18,-18.81),(69.83,-18.76),(70.22,-17.33),(68.21,-16.14),(80.67,-7.43),\
        (74.44,0.)]
    shell_edges_r = shell_edges_r[5:] + shell_edges_r[:5]
    shell_thickness = 2.8
    shell_geta_1 = sw.parent(base).void(base_panel_thickness - shell_thickness)
    shell_r = sw.parent(shell_geta_1).void(shell_thickness)
    shell_r.add_ribs([0.,1.], shell_edges_r)
    sw.deformation(shell_r, shell_r_deformation)

    shell_l = sw.parent(shell_geta_1).void(shell_thickness)
    shell_l.add_ribs([0.,1.], shell_edges_r)
    sw.deformation(shell_l, shell_r_deformation)
    sw.deformation(shell_l, lambda x,y,z: (x,-y,z))
    for triangle in shell_l.monocoque_shell.triangles:
        triangle.inverse()

    tip_edges_start = [(-11.,0.),(11.,0.),(0.,-13.5)]
    tip_edges_end = [(-2.9,0.),(2.9,0.),(0.,-3.2)]
    tip_base_thickness = 2.4
    tip_base_geta_1 = sw.move_y(backpack_tip_slider)
    tip_base_geta_2 = sw.parent(tip_base_geta_1).void(base_panel_thickness-0.4)
    tip_base = sw.parent(tip_base_geta_2).rectangular(8.,14.,tip_base_thickness)
    sw.deformation(tip_base, lambda x,y,z: (x,y+3.5,z))
    tip_geta_1 = sw.parent(tip_base, 1.-0.8/tip_base_thickness).rotate_x(-np.pi/2.)
    tip = sw.parent(tip_geta_1).void(95.)
    tip.add_rib(0., tip_edges_start)
    tip.add_rib(1., tip_edges_end)
    sw.deformation(tip, tip_deformation)

    thruster_geta_1 = sw.move_y(-50.)
    thruster_geta_2 = sw.parent(thruster_geta_1).void(2.)
    thruster_geta_3 = sw.parent(thruster_geta_2).rotate_x(np.pi/2.)
    thruster = sw.parent(thruster_geta_3).load_submodule(os.path.join(path, 'backpack_thruster'))

    accessory_geta_1 = sw.move_y(39.)
    accessory = sw.rotate(np.pi).parent(accessory_geta_1).load_submodule(os.path.join(path, 'backpack_accessory'))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def base_panel_deformation(x,y,z):
    range = 0.01
    if x < -38.:
        return (x-z/2.,y,z)
    return None

def base_side_r_deformation(x,y,z):
    target = [\
        (-41.84,-9.68),(-40.41,-12.27),(23.64,-19.97),(66.18,-18.81),(66.10,-16.39),\
        (30.06,-9.85),(26.56,-14.37)]
    mod_xy = [\
        (-39.84,-9.12),(-38.41,-10.25),(36.36,-18.01),(68.22,-17.75),(67.79,-17.08),\
        (34.15,-16.41),(31.40,-16.03)]
    range = 0.01
    if z > 0.-range:
        if x < -38.:
            return (x-z/2.,y,z)
        return (x,y,z)
    if target[0][0] - range < x and x < target[0][0] + range:
        return (mod_xy[0][0],mod_xy[0][1],z-3.)
    elif target[1][0] - range < x and x < target[1][0] + range:
        return (mod_xy[1][0],mod_xy[1][1],z-3.)
    elif target[2][0] - range < x and x < target[2][0] + range:
        return (mod_xy[2][0],mod_xy[2][1],z-10.)
    elif target[3][0] - range < x and x < target[3][0] + range:
        return (mod_xy[3][0],mod_xy[3][1],z-4.)
    elif target[4][0] - range < x and x < target[4][0] + range:
        return (mod_xy[4][0],mod_xy[4][1],z-4.)
    elif target[5][0] - range < x and x < target[5][0] + range:
        return (mod_xy[5][0],mod_xy[5][1],z-9.)
    elif target[6][0] - range < x and x < target[6][0] + range:
        return (mod_xy[6][0],mod_xy[6][1],z-9.)

def base_side_l_deformation(x,y,z):
    target = [\
        (-41.84,9.68),(-40.41,12.27),(23.64,19.97),(66.18,18.81),(66.10,16.39),\
        (30.06,9.85),(26.56,14.37)]
    mod_xy = [\
        (-39.84,9.12),(-38.41,10.25),(36.36,18.01),(68.22,17.75),(67.79,17.08),\
        (34.15,16.41),(31.40,16.03)]
    range = 0.01
    if z > 0.-range:
        if x < -38.:
            return (x-z/2.,y,z)
        return (x,y,z)
    if target[0][0] - range < x and x < target[0][0] + range:
        return (mod_xy[0][0],mod_xy[0][1],z-3.)
    elif target[1][0] - range < x and x < target[1][0] + range:
        return (mod_xy[1][0],mod_xy[1][1],z-3.)
    elif target[2][0] - range < x and x < target[2][0] + range:
        return (mod_xy[2][0],mod_xy[2][1],z-10.)
    elif target[3][0] - range < x and x < target[3][0] + range:
        return (mod_xy[3][0],mod_xy[3][1],z-4.)
    elif target[4][0] - range < x and x < target[4][0] + range:
        return (mod_xy[4][0],mod_xy[4][1],z-4.)
    elif target[5][0] - range < x and x < target[5][0] + range:
        return (mod_xy[5][0],mod_xy[5][1],z-9.)
    elif target[6][0] - range < x and x < target[6][0] + range:
        return (mod_xy[6][0],mod_xy[6][1],z-9.)

def shell_r_deformation(x,y,z):
    target = [\
        (-47.39,0.),\
        (-48.88,-3.51),(-40.91,-8.11),(-42.84,-9.68),(-41.41,-12.27),(23.64,-19.97),\
        (66.18,-18.81),(69.83,-18.76),(70.22,-17.33),(68.21,-16.14),(80.67,-7.43),\
        (74.44,0.)]
    range = 0.01
    thickness = 2.8
    if 0.-range < y and y < 0.+range:
        if x < 0.:
            if thickness/2. < z:
                return (x,y,z+17.9)
            else:
                return (x-2.,y,z+17.9-1.)
        else:
            if thickness/2. < z:
                return (x,y,z+32.1)
            else:
                return (x-2.,y+0.5,z+32.1-1.)
    if target[1][0] - range < x and x < target[1][0] + range:
        if thickness/2. < z:
            return (x,y-1.,z+11.5)
        else:
            return (x-2.,y,z+11.5)
    elif target[2][0] - range < x and x < target[2][0] + range:
        if thickness/2. < z:
            return (x,y-1.,z+4.8)
        else:
            return (x-2.,y,z+4.8)
    elif target[10][0] - range < x and x < target[10][0] + range:
        if thickness/2. < z:
            return (x,y-1.,z+22.)
        else:
            return (x,y,z+22.)
    elif target[7][0] - range < x and x < target[7][0] + range:
        if thickness/2. < z:
            return (x,y,z+8.6)
        else:
            return (x,y+1.5,z+8.6)
    elif target[8][0] - range < x and x < target[8][0] + range:
        if thickness/2. < z:
            return (x,y-1.5,z+11.)
        else:
            return (x,y,z+11.)
    elif target[9][0] - range < x and x < target[9][0] + range:
        if thickness/2. < z:
            return (x,y-1.,z+12.2)
        else:
            return (x,y,z+12.2)
    elif target[5][0] - range < x and x < target[5][0] + range\
        or target[6][0] - range < x and x < target[6][0] + range:
        if z < thickness/2.:
            return (x,y+2.,z)
    elif target[4][0] - range < x and x < target[4][0] + range:
        if thickness/2. < z:
            return (x,y-0.5,z)
        else:
            return (x,y+0.5,z)
    elif target[3][0] - range < x and x < target[3][0] + range:
        if thickness/2. < z:
            return (x,y-0.5,z+3.6)
        else:
            return (x,y+0.5,z+3.6)
    return None
    
def tip_deformation(x,y,z):
    range = 0.1
    if z < 0. + range:
        if y < 0. - range:
            return (x,y,z+6.)
    else:
        if y < 0. - range:
            return (x,y,z+4.)
    return None

if __name__ == "__main__":
    main()