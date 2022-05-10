from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    base_1 = sw.rotate(np.pi/2, np.pi/2).void(1.5)
    base_2 = sw.rotate(-np.pi/2).parent(base_1).void(0.)
    base_3 = sw.rotate(0, -np.pi/2).parent(base_2).void(0.)

    head_core_length = 12.6
    head_core_width = 2.7
    head_core_height = 3.4

    head_core_edges = [(head_core_width/2, head_core_height/2), (-head_core_width/2, head_core_height/2), (-head_core_width/2, -head_core_height/2), (head_core_width/2, -head_core_height/2)]
    head_core_edges_mid = [(0.1, head_core_height/2), (-0.1, head_core_height/2), (-head_core_width/4, -head_core_height/2), (head_core_width/4, -head_core_height/2)]
    head_core_edges_end = [(0., -head_core_height/2)]
    head_core = sw.parent(base_3).void(head_core_length)
    head_core.add_rib(0., head_core_edges)
    head_core.add_rib(1.-2.2/head_core_length, head_core_edges_mid)
    head_core.add_rib(1., head_core_edges_end)
    sw.deformation(head_core, lambda x,y,z : (x,y+1.3,z))

    head_core_cover_length = 13.
    head_core_cover_width = 4.6
    head_core_cover_width_mid = 3.4
    head_core_cover_width_end = 2.
    head_core_cover_height = 3.7

    head_core_cover_edges = [\
        (head_core_cover_width/2., head_core_cover_height/2.), (-head_core_cover_width/2., head_core_cover_height/2.),\
        (-head_core_cover_width/2., -head_core_cover_height/2.), (head_core_cover_width/2., -head_core_cover_height/2.)]
    head_core_cover_edges_mid = [\
        (head_core_cover_width_mid/2., head_core_cover_height/2.), (-head_core_cover_width_mid/2., head_core_cover_height/2.),\
        (-head_core_cover_width_mid/2., -head_core_cover_height/2.), (head_core_cover_width_mid/2., -head_core_cover_height/2.)]
    head_core_cover_edges_end = [\
        (head_core_cover_width_end/2., -head_core_cover_height/2.+0.1), (-head_core_cover_width_end/2., -head_core_cover_height/2.+0.1),\
        (-head_core_cover_width_end/2., -head_core_cover_height/2.), (head_core_cover_width_end/2., -head_core_cover_height/2.)]

    head_core_cover_geta = sw.rotate(np.pi).parent(base_3).void(3.8)
    head_core_cover = sw.rotate(-np.pi).parent(head_core_cover_geta).void(head_core_cover_length)
    head_core_cover.add_rib(0., head_core_cover_edges)
    head_core_cover.add_rib(6.5/head_core_cover_length, head_core_cover_edges_mid)
    head_core_cover.add_rib(1., head_core_cover_edges_end)
    sw.deformation(head_core_cover, lambda x,y,z : (x,y+1.3,z))

    head_bottom_geta = sw.rotate(np.pi/2).parent(base_3).void(0.)
    head_bottom_tickness = 8.2
    head_bottom_edges = [(-14.2, 0.), (-13.9, -2.), (-5.2, -3.6), (9.5, -2.4), (9.5, 2.), (8.1, 6.2), (4.8, 5.5), (0., -0.5)]
    head_bottom = sw.parent(head_bottom_geta).void(head_bottom_tickness)
    head_bottom.add_ribs([0., 1.], head_bottom_edges) 
    sw.deformation(head_bottom, lambda x,y,z : (x,y,z-head_bottom_tickness/2))
    sw.deformation(head_bottom, head_bottom_deformation)

    head_upper_length = 21.
    head_upper_width_upper = 3.5
    head_upper_width_bottom = 5.3
    head_upper_width_bottom_mid = 3.8
    head_upper_height_start = 3.1
    head_upper_height_end = 4.8
    head_upper_edges = [\
        (head_upper_width_upper/2, head_upper_height_start/2), (-head_upper_width_upper/2, head_upper_height_start/2),\
        (-head_upper_width_bottom/2, -head_upper_height_start/2), (head_upper_width_bottom/2, -head_upper_height_start/2)]
    head_upper_edges_mid = [\
        (0.1, head_upper_height_start/2), (-0.1, head_upper_height_start/2),\
        (-head_upper_width_bottom_mid/2, head_upper_height_start/2-head_upper_height_end),\
        (head_upper_width_bottom_mid/2, head_upper_height_start/2-head_upper_height_end)]
    head_upper_edges_end = [(0., head_upper_height_start/2-head_upper_height_end)]
    head_upper_up_modification = 3.6
    head_upper_back_modification = 5.2
    head_upper_geta_1 = sw.rotate(np.pi/2, np.pi/2).parent(base_3).void(head_upper_up_modification)
    head_upper_geta_2 = sw.rotate(-np.pi/2).parent(head_upper_geta_1).void(0.)
    head_upper_geta_3 = sw.rotate(0, -np.pi/2).parent(head_upper_geta_2).void(0.)
    head_upper_geta_4 = sw.rotate(-np.pi).parent(head_upper_geta_3).void(head_upper_back_modification)
    head_upper = sw.rotate(np.pi).parent(head_upper_geta_4).void(head_upper_length)
    head_upper.add_ribs([0., 1.-8.6/head_upper_length], head_upper_edges)
    head_upper.add_rib(1.-5.0/head_upper_length, head_upper_edges_mid)
    head_upper.add_rib(1., head_upper_edges_end)

    head_cover_edges = [\
        (0., 0.), (-2.5, 1.), (-3.5, 3.7), (-2.2, 4.3), (-4.9, 6.), (-4., 9.4), (19., 7.1), (20., 5.2),\
        (3., 6.), (1.1, 4.3), (3., 3.4), (15.7, 4.), (16.4, 3.)]
    head_cover_down_modification = 3.7
    head_cover_back_modification = 1.6
    head_cover_r_right_modification = 3.8
    head_cover_r = sw.rotate(-np.pi/2).parent(base_3).void(1.)
    head_cover_r.add_ribs([0., 1.], head_cover_edges)
    sw.deformation(head_cover_r, lambda x,y,z: (x, y, z-0.5))
    sw.deformation(head_cover_r, head_cover_deformation)
    sw.deformation(head_cover_r, lambda x,y,z: (x-head_cover_back_modification, y-head_cover_down_modification, z+head_cover_r_right_modification))

    head_cover_l = sw.rotate(-np.pi/2).parent(base_3).void(1.)
    head_cover_l.add_ribs([0., 1.], head_cover_edges)
    sw.deformation(head_cover_l, lambda x,y,z: (x, y, z-0.5))
    sw.deformation(head_cover_l, head_cover_deformation)
    sw.deformation(head_cover_l, lambda x,y,z: (x, y, -z))
    for triangle in head_cover_l.monocoque_shell.triangles:
        triangle.inverse()
    sw.deformation(head_cover_l, lambda x,y,z: (x-head_cover_back_modification, y-head_cover_down_modification, z-head_cover_r_right_modification))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def head_bottom_deformation(x,y,z):
    target = [(-14.2, 0.), (-13.9, -2.), (-5.2, -3.6), (9.5, -2.4), (9.5, 2.), (8.1, 6.2), (4.8, 5.5), (0., -0.5)]
    range = 0.1
    if target[0][1]-range < y and y < target[0][1]+range:
        tickness = 1.6
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[1][1]-range < y and y < target[1][1]+range:
        tickness = 1.6
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[2][1]-range < y and y < target[2][1]+range:
        tickness = 5.4
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[3][1]-range < y and y < target[3][1]+range:
        tickness = 8.
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[4][1]-range < y and y < target[4][1]+range:
        return None
    elif target[5][1]-range < y and y < target[5][1]+range:
        tickness = 7.5
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[6][1]-range < y and y < target[6][1]+range:
        tickness = 8.
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)
    elif target[7][1]-range < y and y < target[7][1]+range:
        tickness = 5.7
        if z < 0.:
            return (x, y, -tickness/2)
        else:
            return (x, y, tickness/2)

def head_cover_deformation(x,y,z):
    target = [\
        (0., 0.), (-2.5, 1.), (-3.5, 3.7), (-2.2, 4.3), (-4.9, 6.), (-4., 9.4), (19., 7.1), (20., 5.2),\
        (3., 6.), (1.1, 4.3), (3., 3.4), (15.7, 4.), (16.4, 3.)]
    range = 0.1
    if target[3][0]-range < x and x < target[3][0]+range:
        if z < 0.:
            return (x, y, z-0.3)
        else:
            return None
    elif target[9][0]-range < x and x < target[9][0]+range:
        if z < 0.:
            return (x, y, z-0.3)
        else:
            return None
    elif target[0][0]-range < x and x < target[0][0]+range:
        return (x, y, z-0.4)
    elif target[5][0]-range < x and x < target[5][0]+range:
        return (x, y, z-0.4)
    elif target[6][0]-range < x and x < target[6][0]+range:
        return (x, y, z-0.8)
    elif target[7][0]-range < x and x < target[7][0]+range:
        return (x, y, z-1.)
    elif target[11][0]-range < x and x < target[11][0]+range:
        return (x, y, z-0.5)
    elif target[12][0]-range < x and x < target[12][0]+range:
        return (x, y, z-0.5)
    return None

if __name__ == "__main__":
    main()