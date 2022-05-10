from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    waist_radius = 6.6
    
    waist = sw.pole(10., waist_radius, np.pi*2, 32, True)
    waist.add_rib(6.5/10., waist.ribs[0].edges.copy())
    waist.ribs[1].edges = edges_util.scale(waist.ribs[0].edges.copy(), 7.5/6.6)
    waist.order_ribs()

    waist_front_cover_geta_1 = sw.parent(waist).rotate_x(np.pi/2.)
    waist_front_cover_geta_2 = sw.parent(waist_front_cover_geta_1).void(5.)
    waist_front_cover = sw.parent(waist_front_cover_geta_2).void(8.)
    waist_front_cover.add_rib(0., [(-1.9,0.),(1.9,0.),(1.9,-5.),(-1.9,-5.)])
    waist_front_cover.add_rib(1., [(-1.9,0.),(1.9,0.),(1.9,-2.4),(-1.9,-2.4)])

    waist_back_cover_geta_1 = sw.parent(waist).rotate_x(-np.pi/2.)
    waist_back_cover_geta_2 = sw.parent(waist_back_cover_geta_1).void(5.)
    waist_front_cover_outer = sw.parent(waist_back_cover_geta_2).void(3.)
    waist_front_cover_outer.add_ribs([0.,1.], [(-3.,0.),(3.,0.),(3.,9.),(-3.,9.)])

    waist_front_cover_inner_edges = [(-2.,0.),(2.,0.),(2.,3.),(-2.,3.)]
    waist_front_cover_inner = sw.parent(waist_back_cover_geta_2).void(5.6)
    waist_front_cover_inner.add_ribs([0.,0.8], waist_front_cover_inner_edges)
    waist_front_cover_inner.add_rib(1., edges_util.scale(waist_front_cover_inner_edges, 0.8))

    waist_base_edges = [\
        (-4.,-12.),(-4,-8.5),(-7.,-8.5),(-9.,0.),(-8.,7.),(-4.,8.5),\
        (4.,8.5),(8.,7.),(9.,0.),(7.,-8.5),(4.,-8.5),(4.,-12.),]
    waist_base_thickness = 4.
    waist_base = sw.parent(waist, 9./10.).void(waist_base_thickness)
    waist_base.add_ribs([0.,1.], waist_base_edges)

    waist_base_cover_edges = [(0.7,0.7),(-0.7,0.7),(-0.7,4.),(0.7,4.)]
    waist_base_cover_length = 20.
    waist_base_cover_rib_positions = [\
        0.,1.5/waist_base_cover_length,2.5/waist_base_cover_length,8.5/waist_base_cover_length,\
        13.5/waist_base_cover_length,17./waist_base_cover_length,1.]
    waist_base_cover_r_geta_1 = sw.parent(waist, 9./10.).move_x(9.)
    waist_base_cover_r_geta_2 = sw.parent(waist_base_cover_r_geta_1).rotate_x(np.pi/2)
    waist_base_cover_r = sw.parent(waist_base_cover_r_geta_2).void(waist_base_cover_length)
    waist_base_cover_r.add_ribs(waist_base_cover_rib_positions, waist_base_cover_edges)
    sw.deformation(waist_base_cover_r, lambda x,y,z: (x,y,z-8.5))
    sw.deformation(waist_base_cover_r, waist_base_cover_r_deformation)

    waist_base_cover_l_geta_1 = sw.parent(waist, 9./10.).move_x(-9.)
    waist_base_cover_l_geta_2 = sw.parent(waist_base_cover_l_geta_1).rotate_x(np.pi/2)
    waist_base_cover_l = sw.parent(waist_base_cover_l_geta_2).void(waist_base_cover_length)
    waist_base_cover_l.add_ribs(waist_base_cover_rib_positions, waist_base_cover_edges)
    sw.deformation(waist_base_cover_l, lambda x,y,z: (x,y,z-8.5))
    sw.deformation(waist_base_cover_l, waist_base_cover_r_deformation)
    sw.deformation(waist_base_cover_l, lambda x,y,z: (-x,y,z))
    for triangle in waist_base_cover_l.monocoque_shell.triangles:
        triangle.inverse()

    waist_base_vert_edges_start = [(-3.6, 13.),(3.6, 13),(3.6, -13.),(-3.6, -13.)]
    waist_base_vert_edges_mid = [(-3.6, 9.),(3.6, 9.),(3.6, -13.),(-3.6, -13.)]
    waist_base_vert_edges_end = [(-3.6, 5.),(3.6, 5.),(3.6, -7.),(-3.6, -7.)]
    waist_base_vert_thickness = 14.
    waist_base_vert = sw.parent(waist, 9./10.).void(waist_base_vert_thickness)
    waist_base_vert.add_ribs([0., 4./14.], waist_base_vert_edges_start)
    waist_base_vert.add_rib(9./14., waist_base_vert_edges_mid)
    waist_base_vert.add_rib(1., waist_base_vert_edges_end)

    waist_accessory_front_geta_1 = sw.parent(waist, 9./10.).rotate_x(np.pi/2.)
    waist_accessory_front_geta_2 = sw.rotate(0.,np.pi).parent(waist_accessory_front_geta_1).void(12.)
    waist_accessory_front_geta_3 = sw.parent(waist_accessory_front_geta_2).rotate_x(np.pi/2.)
    waist_accessory_edges = [(1.,1.),(-1.,1.),(-1.,-1.),(1.,-1.)]
    waist_accessory = sw.parent(waist_accessory_front_geta_3).void(4.)
    waist_accessory.add_ribs([0.,0.25,0.5,0.75,1.], waist_accessory_edges)
    sw.deformation(waist_accessory, waist_accessory_deformation)

    coxa_base_edge_start = [(10.,5.),(-10.,5.),(-10.,-5.),(10.,-5.)]
    coxa_base_edge_end = [(7.,5.),(-7.,5.),(-7.,-5.),(7.,-5.)]
    coxa_base_thickness = 8.1
    coxa_base_geta_1 = sw.parent(waist_base, 1.-0.1/waist_base_thickness).move_y(-1.)
    coxa_base = sw.parent(coxa_base_geta_1).void(coxa_base_thickness)
    coxa_base.add_ribs([0., 5.1/coxa_base_thickness], coxa_base_edge_start)
    coxa_base.add_rib(1., coxa_base_edge_end)

    coxa_edges = [(2.7,2.7),(-2.7,2.7),(-2.7,-2.7),(2.7,-2.7)]
    coxa_length = 28.
    coxa_geta_1 = sw.rotate(-np.pi/2.).parent(coxa_base, 3.1/coxa_base_thickness).void(coxa_length/2.)
    coxa = sw.rotate(np.pi).parent(coxa_geta_1).void(coxa_length)
    coxa.add_ribs([0.,1.], coxa_edges)
    sw.chamfering(coxa, 1.)

    coxa_accessory_edges = [\
        (4.7,-10.),(4.7,-8.),(6.6,-6.),(8.6,-6.),(8.6,6.),(2.,8.),\
        (-2.,8.),(-8.6,6.),(-8.6,-6.),(-6.6,-6.),(-4.7,-8.),(-4.7,-10.)]
    coxa_accessory_thickness = 3.2
    coxa_accessory = sw.parent(coxa_base, 3.1/coxa_base_thickness).void(coxa_accessory_thickness)
    coxa_accessory.add_ribs([0.,1.], coxa_accessory_edges)
    sw.deformation(coxa_accessory, lambda x,y,z: (x,y,z-coxa_accessory_thickness/2.))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def waist_base_cover_r_deformation(x,y,z):
    target_z_position = [-8.5,-7.,-6.,0.,5.,8.5,11.5]
    range = 0.1
    y_center = 2.
    if target_z_position[0] - range < z and z < target_z_position[0] + range:
        if y < y_center:
            if x < 0.:
                return (x-7,-0.6,z+0.7)
            else:
                return (x-7,-0.6+0.2,z-0.7)
        else:
            if x < 0.:
                return (x-7,y,z+0.7)
            else:
                return (x-7,y,z-0.7)
    elif target_z_position[1] - range < z and z < target_z_position[1] + range:
        if y < y_center:
            if x < 0.:
                return (x+z*2./8.5,-0.6,z+0.7)
            else:
                return (x+z*2./8.5,-0.6+0.2,z-0.7)
        else:
            if x < 0.:
                return (x+z*2./8.5,y,z+0.7)
            else:
                return (x+z*2./8.5,y,z-0.7)
    elif target_z_position[2] - range < z and z < target_z_position[2] + range:
        if y < y_center:
            if x < 0.:
                return (x+z*1./7.,-2.8,z+0.7)
            else:
                return (x+z*1./7.,-2.8+0.2,z-0.7)
        else:
            if x < 0.:
                return (x+z*1./7.,y,z+0.7)
            else:
                return (x+z*1./7.,y,z-0.7)
    elif target_z_position[3] - range < z and z < target_z_position[3] + range:
        if y < y_center:
            if x < 0.:
                return (x,-2.8,z)
            else:
                return (x,-2.8+0.2,z)
        else:
            return None
    elif target_z_position[4] - range < z and z < target_z_position[4] + range:
        if y < y_center:
            if x < 0.:
                return (x-z*2./8.5,y,z)
            else:
                return (x-z*2./8.5,y,z)
        else:
            if x < 0.:
                return (x-z*2./8.5,y,z)
            else:
                return (x-z*2./8.5,y,z)
    elif target_z_position[5] - range < z and z < target_z_position[5] + range:
        if y < y_center:
            if x < 0.:
                return (x-z*2./8.5,y,z-0.7)
            else:
                return (x-z*2./8.5,y,z+0.7)
        else:
            if x < 0.:
                return (x-z*2./8.5,y,z-0.7)
            else:
                return (x-z*2./8.5,y,z+0.7)
    elif target_z_position[6] - range < z and z < target_z_position[6] + range:
        if y < y_center:
            if x < 0.:
                return (x-7.,y,z-2.5)
            else:
                return (x-7.,y,z-1.)
        else:
            if x < 0.:
                return (x-7.,y,z-2.5)
            else:
                return (x-7.,y,z-1.)
    return None

def waist_accessory_deformation(x,y,z):
    range = 0.1
    if z < 0.+range:
        if x < 0.:
            if y < 0.:
                return (-4.4,0.,0.)
            else:
                return (-2.7,8.8,0.)
        else:
            if y < 0.:
                return (4.4,0.,0.)
            else:
                return (2.7,8.8,0.)
    elif 1.-range < z and z < 1.+range:
        if x < 0.:
            if y < 0.:
                return (-4.4,0.,4.)
            else:
                return (-2.7,8.8,4.)
        else:
            if y < 0.:
                return (4.4,0.,4.)
            else:
                return (2.7,8.8,4.)
    elif 2.-range < z and z < 2.+range:
        if x < 0.:
            if y < 0.:
                return (-4.,2.,5.)
            else:
                return (-2.7,8.8,5.)
        else:
            if y < 0.:
                return (4.,2.,5.)
            else:
                return (2.7,8.8,5.)
    elif 3.-range < z and z < 3.+range:
        if x < 0.:
            if y < 0.:
                return (-4.,2.,30.5)
            else:
                return (-2.7,8.8,30.5)
        else:
            if y < 0.:
                return (4.,2.,30.5)
            else:
                return (2.7,8.8,30.5)
    elif 4.-range < z and z < 4.+range:
        if x < 0.:
            if y < 0.:
                return (-4.4,0.,32.5)
            else:
                return (-2.7,0.,38.5)
        else:
            if y < 0.:
                return (4.4,0.,32.5)
            else:
                return (2.7,0.,38.5)

if __name__ == "__main__":
    main()