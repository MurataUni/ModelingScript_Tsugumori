from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    body_upper_front_core = sw.load_submodule(os.path.join(path, 'body_upper_front_core'))
    sw.deformation(body_upper_front_core, lambda x,y,z: (x,y,z+31))
    body_upper_front_core.align_keel_size_to_monocoque_shell()

    body_front_top_geta_1 = sw.void(20.)
    body_front_top_geta_2 = sw.rotate(np.pi/2, np.pi/2).parent(body_front_top_geta_1).void()
    body_front_top_geta_3 = sw.rotate(0., -np.pi/2).parent(body_front_top_geta_2).void()
    body_front_top_edges = [(3.5, 0), (-3.5, 0.), (-3.5, 6.), (-2.5, 13.), (2.5, 13.), (3.5, 6.)]
    body_front_top_edges_end = [(2.5, 4.), (-2.5, 4.), (-2.5, 6.), (-1., 10.), (1., 10.), (2.5, 6.)]
    body_front_top = sw.parent(body_front_top_geta_3).void(3.9)
    body_front_top.add_ribs([0., 1.-1/3.9], body_front_top_edges)
    body_front_top.add_rib(1., body_front_top_edges_end)

    head_geta_1 = sw.rotate(np.pi).void(7.)
    head_geta_2 = sw.rotate(np.pi/2, np.pi/2).parent(head_geta_1).void(2.)
    neck = sw.rotate(0., np.pi/2).parent(head_geta_2).load_submodule(os.path.join(path, 'neck'))

    body_cover_tickness = 6.
    body_cover_edge = [\
        (3., 0.), (1., 1.8), (1., 4.9), (0., 5.4), (0., 7.7), (1., 8.2), (1., 14.5), (0., 15.),\
        (0., 17.3), (1., 20.5), (16., 20.5), (30., 12.5), (30., 9.), (21., 0.)]
    body_cover_edge_end = [\
        (3., 1.7), (1., 1.8+1.7), (1., 4.9), (0., 5.4), (0., 7.7), (1., 8.2), (1., 14.5), (0., 15.),\
        (0., 17.3), (1., 20.3-1.3), (16.-4., 20.3-1.3), (30.-3., 12.5-1.), (30.-3., 9.+1.), (21.-2., 1.7)]
    body_cover_back_move = 7.
    body_cover_down_move = 2.
    body_cover_r_right_move = 5.
    body_cover_geta_1 = sw.rotate(-np.pi).void(body_cover_back_move)
    body_cover_geta_2 = sw.rotate(np.pi).parent(body_cover_geta_1).void()
    body_cover_geta_3 = sw.rotate(-np.pi/2, np.pi/2).parent(body_cover_geta_2).void(body_cover_down_move)
    body_cover_geta_4 = sw.rotate(np.pi/2).parent(body_cover_geta_3).void()
    body_cover_geta_5 = sw.rotate(0., -np.pi/2).parent(body_cover_geta_4).void()
    body_cover_r_geta = sw.rotate(-np.pi/2).parent(body_cover_geta_5).void(body_cover_r_right_move)
    body_cover_r = sw.parent(body_cover_r_geta).void(body_cover_tickness)
    body_cover_r.add_rib(0., body_cover_edge)
    body_cover_r.add_rib(1.-2./6., body_cover_edge)
    body_cover_r.add_rib(1., body_cover_edge_end)
    body_cover_down_modification = 7.5+4.2
    body_cover_back_modification = 7.+3.5
    sw.deformation(body_cover_r, lambda x,y,z: (x-body_cover_back_modification, y-body_cover_down_modification, z))

    body_shoulder_panel_adapter_sticking_out = 3.

    body_shoulder_panel_adapter_length = body_cover_r_right_move+body_cover_tickness+body_shoulder_panel_adapter_sticking_out
    body_shoulder_panel_adapter_r = sw.rotate(-np.pi/2).parent(body_cover_geta_5).rectangular(8., 8., body_shoulder_panel_adapter_length)

    body_cover_l_left_move = 5.
    body_cover_l_geta = sw.rotate(np.pi/2).parent(body_cover_geta_5).void(body_cover_l_left_move+body_cover_tickness)
    body_cover_l = sw.rotate(np.pi).parent(body_cover_l_geta).void(body_cover_tickness)
    body_cover_l.add_rib(0., body_cover_edge_end)
    body_cover_l.add_rib(2./6., body_cover_edge)
    body_cover_l.add_rib(1., body_cover_edge)
    sw.deformation(body_cover_l, lambda x,y,z: (x-body_cover_back_modification, y-body_cover_down_modification, z))

    body_shoulder_panel_adapter_l = sw.rotate(np.pi/2).parent(body_cover_geta_5).rectangular(8., 8., body_shoulder_panel_adapter_length)

    body_shoulder_accessory_edges = [(1.1, 1.1), (-1.1, 1.1), (-1.1, -1.1), (1.1, -1.1)]

    body_shoulder_accessory_r_geta_1 = sw.rotate(-np.pi/2.).parent(body_cover_geta_5).void(body_cover_r_right_move+(body_cover_tickness-2.)/2)
    body_shoulder_accessory_r_geta_2 = sw.rotate(-np.pi/2.).parent(body_shoulder_accessory_r_geta_1).void(body_cover_back_modification-2.)
    body_shoulder_accessory_r_geta_3 = sw.rotate(-np.pi).parent(body_shoulder_accessory_r_geta_2).void()
    body_shoulder_accessory_r_geta_4 = sw.rotate(np.pi/2., np.pi/2.).parent(body_shoulder_accessory_r_geta_3).void(body_cover_down_modification-3.5)
    body_shoulder_accessory_r_geta_5 = sw.rotate(-np.pi/2., np.pi/2.).parent(body_shoulder_accessory_r_geta_4).void(0.)
    body_shoulder_accessory_r_geta_6 = sw.rotate(-np.pi/2., -np.pi/2.).parent(body_shoulder_accessory_r_geta_5).void(0.)
    body_shoulder_accessory_r = sw.parent(body_shoulder_accessory_r_geta_6).void(4.)
    body_shoulder_accessory_r.add_ribs([0., 1./4., 2./4., 3./4., 1.], body_shoulder_accessory_edges)
    sw.deformation(body_shoulder_accessory_r, shoulder_accessory_deformation)

    body_shoulder_accessory_l_geta_1 = sw.rotate(np.pi/2.).parent(body_cover_geta_5).void(body_cover_r_right_move+(body_cover_tickness-2.)/2)
    body_shoulder_accessory_l_geta_2 = sw.rotate(np.pi/2.).parent(body_shoulder_accessory_l_geta_1).void(body_cover_back_modification-2.)
    body_shoulder_accessory_l_geta_3 = sw.rotate(np.pi).parent(body_shoulder_accessory_l_geta_2).void()
    body_shoulder_accessory_l_geta_4 = sw.rotate(np.pi/2., np.pi/2.).parent(body_shoulder_accessory_l_geta_3).void(body_cover_down_modification-3.5)
    body_shoulder_accessory_l_geta_5 = sw.rotate(-np.pi/2., np.pi/2.).parent(body_shoulder_accessory_l_geta_4).void(0.)
    body_shoulder_accessory_l_geta_6 = sw.rotate(-np.pi/2., -np.pi/2.).parent(body_shoulder_accessory_l_geta_5).void(0.)
    body_shoulder_accessory_l = sw.parent(body_shoulder_accessory_l_geta_6).void(4.)
    body_shoulder_accessory_l.add_ribs([0., 1./4., 2./4., 3./4., 1.], body_shoulder_accessory_edges)
    sw.deformation(body_shoulder_accessory_l, shoulder_accessory_deformation)
    
    waist_adapter_edges = [\
        (-7.2, 0.), (-7.2, 7.8), (-6.4, 10.), (7.3, 10.), (7.3, 12.5), (10.8, 12.5), (10.8, 7.5), (6.3, 7.5), (6.3, 0.)]
    waist_adapter_thickness = 4.
    waist_adapter_down_modification = 10.
    waist_adapter_geta_1 = sw.rotate(-np.pi/2, np.pi/2).void(0.)
    waist_adapter_geta_2 = sw.rotate(0., -np.pi/2.).parent(waist_adapter_geta_1).void(waist_adapter_down_modification)
    waist_adapter_geta_3 = sw.rotate(np.pi/2).parent(waist_adapter_geta_2).void(waist_adapter_thickness/2.)
    waist_adapter_geta_4 = sw.rotate(-np.pi).parent(waist_adapter_geta_3).void(0.)
    waist_adapter = sw.rotate(0., -np.pi/2).parent(waist_adapter_geta_4).void(waist_adapter_thickness)
    waist_adapter.add_ribs([0., 1.], waist_adapter_edges)

    waist_radius = 6.6
    lower_body_adapter_radius = 6.
    waist_geta_1 = sw.parent(waist_adapter_geta_2).void(5.)
    waist = sw.parent(waist_geta_1).pole(9., waist_radius, np.pi*2, 32, True)
    waist.ribs[0].position = 1./9.
    waist.add_rib(0., edges_util.scale(waist.ribs[0].edges.copy(), 0.9))

    waist = sw.parent(waist_adapter_geta_2).parent(waist, 5./9.).pole((9.-5.)+2., lower_body_adapter_radius, np.pi*2, 32, True)

    waist_cover_geta_1 = sw.parent(waist_adapter_geta_2).void(10.)
    waist_cover_geta_2 = sw.rotate(-np.pi/2., np.pi/2.).parent(waist_cover_geta_1).void()
    waist_cover_geta_3 = sw.rotate(0., -np.pi/2.+np.pi).parent(waist_cover_geta_2).void(10.)
    waist_cover_left_geta = sw.rotate(-np.pi/2.).parent(waist_cover_geta_3).void(9.)
    waist_cover_base = sw.rotate(np.pi).parent(waist_cover_left_geta).void(18.)
    waist_cover_base.add_ribs([0., 1.], [(1.8, -2.0), (1.8, 2.0), (-1.2, 3.), (-1.8, 2.5), (-1.8, -2.5), (-1.2, -3.)])

    waist_cover_accessory_edges = [\
        (5.59, 6.50), (10.81, 6.16), (12.59, 3.47), (29.80, -0.17), (29.83, -2.19), \
        (11.58, -3.), (9.12, -3.5), (4.58, -3.5), (-1.9, -2.19), (-1.9, 3.87)]
    waist_cover_l = sw.rotate(0., np.pi).parent(waist_cover_left_geta).void(2.)
    waist_cover_l.add_ribs([0., 1.], waist_cover_accessory_edges)
    sw.deformation(waist_cover_l, lambda x,y,z: (x,y-1.,z-1.))
    sw.deformation(waist_cover_l, waist_cover_l_deformation)

    waist_cover_r = sw.rotate(np.pi, np.pi).parent(waist_cover_base).void(2.)
    waist_cover_r.add_ribs([0., 1.], waist_cover_accessory_edges)
    sw.deformation(waist_cover_r, lambda x,y,z: (x,y-1.,z-1.))
    sw.deformation(waist_cover_r, waist_cover_l_deformation)
    sw.deformation(waist_cover_r, lambda x,y,z: (x,y,-z))
    for triangle in waist_cover_r.monocoque_shell.triangles:
        triangle.inverse()

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def waist_cover_l_deformation(x,y,z):
    deform_z1 = 0.8
    deform_z2 = 0.8
    deform_z3 = -1.
    deform_y1 = 0.5
    deform_x = 0.5
    target = [\
        (5.59, 6.50), (10.81, 6.16), (12.59, 3.47), (29.80, -0.17), (29.83, -2.19), \
        (11.58, -3.), (9.12, -3.5), (4.58, -3.5), (-1.8, -2.19), (-1.8, 3.87)]
    range = 0.01
    if target[0][0]-range < x and x < target[0][0]+range:
        if z < 0.:
            return (x, y, z+deform_z1)
        else:
            return (x, y-deform_y1, z+deform_z1)
    elif target[1][0]-range < x and x < target[1][0]+range:
        if z < 0.:
            return (x, y, z+deform_z1)
        else:
            return (x, y-deform_y1, z+deform_z1)
    elif target[2][0]-range < x and x < target[2][0]+range:
        if z < 0.:
            return (x, y, z+deform_z2)
        else:
            return (x-deform_x, y-deform_y1, z+deform_z2)
    elif target[3][0]-range < x and x < target[3][0]+range:
        if z < 0.:
            return (x, y, z+deform_z3)
        else:
            return (x-deform_x, y-deform_y1, z+deform_z3)
    elif target[4][0]-range < x and x < target[4][0]+range:
        if z < 0.:
            return (x, y, z+deform_z3)
        else:
            return (x-deform_x, y+deform_y1, z+deform_z3)
    elif target[5][0]-range < x and x < target[5][0]+range:
        if z < 0.:
            return (x, y, z+deform_z2)
        else:
            return (x-deform_x, y+deform_y1, z+deform_z2)
    elif target[6][0]-range < x and x < target[6][0]+range:
        if z < 0.:
            return (x, y, z+deform_z2)
        else:
            return (x, y+deform_y1, z+deform_z2)
    elif target[7][0]-range < x and x < target[7][0]+range:
        if z < 0.:
            return (x, y, z+deform_z2)
        else:
            return (x, y+deform_y1, z+deform_z2)
    return None

def shoulder_accessory_deformation(x,y,z):
    range = 0.1
    if 0.-range < z and z < 0.+range:
        if y > 0.:
            return (x, 0., 0.)
        else:
            return (x, 0., 2.2)
    elif 1.-range < z and z < 1.+range:
        if y > 0.:
            return (x, 4.6, 0.5)
        else:
            return (x, 3., 2.7)
    elif 2.-range < z and z < 2.+range:
        if y > 0.:
            return (x, 4.6, 12.)
        else:
            return (x, 3., 10.7)
    elif 3.-range < z and z < 3.+range:
        if y > 0.:
            return (x, 0.5, 15.5)
        else:
            return (x, 0.5, 13.3)
    elif 4.-range < z and z < 4.+range:
        if y > 0.:
            return (x, -2., 15.5)
        else:
            return (x, -2., 13.3)
    return None

def shoulder_accessory_deformation(x,y,z):
    range = 0.1
    if 0.-range < z and z < 0.+range:
        if y > 0.:
            return (x, 0., 0.)
        else:
            return (x, 0., 2.2)
    elif 1.-range < z and z < 1.+range:
        if y > 0.:
            return (x, 4.6, 0.5)
        else:
            return (x, 3., 2.7)
    elif 2.-range < z and z < 2.+range:
        if y > 0.:
            return (x, 4.6, 12.)
        else:
            return (x, 3., 10.7)
    elif 3.-range < z and z < 3.+range:
        if y > 0.:
            return (x, 0.5, 15.5)
        else:
            return (x, 0.5, 13.3)
    elif 4.-range < z and z < 4.+range:
        if y > 0.:
            return (x, -2., 15.5)
        else:
            return (x, -2., 13.3)
    return None

if __name__ == "__main__":
    main()