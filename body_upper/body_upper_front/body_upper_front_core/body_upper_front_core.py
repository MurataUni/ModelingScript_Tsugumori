from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())
    
    body_center_edges = \
        [(0., 0.), (13., 0.), (13., 3.), (31., 3.),\
        (43., 3.), (43., -12.), (24., -12.), (23., -15.), (22., -15.), (21., -12.), \
        (15., -12.)]

    body_center = sw.rotate(np.pi/2).void(14.)
    body_center.add_ribs([0., 1.], body_center_edges)
    sw.deformation(body_center, body_center_deformation_side_bo)
    sw.deformation(body_center, body_center_deformation_side_lr)
    sw.deformation(body_center, lambda x,y,z: (x, y, z-14./2.))

    body_front_cover_edges = [(0., 4.), (10., 0.), (20., 0.), (15., 8.)]
    body_front_cover = sw.rotate(np.pi/2).void(14.)
    body_front_cover.add_ribs([0., 1.], body_front_cover_edges)
    sw.deformation(body_front_cover, body_front_cover_deformation)
    sw.deformation(body_front_cover, lambda x,y,z: (x-2., y-4.4, z-14./2.))

    body_front_wing_edges = [(0., 4.), (10., 0.), (20., 0.), (37., 11.), (26., 11.)]
    body_front_wing_r = sw.rotate(np.pi/2).void(1.)
    body_front_wing_r.add_ribs([0., 1.], body_front_wing_edges)
    sw.deformation(body_front_wing_r, body_front_wing_r_deformation)
    sw.deformation(body_front_wing_r, lambda x,y,z: (x-2., y-4.4, z-14./2.))

    body_front_wing_l = sw.rotate(np.pi/2).void(1.)
    body_front_wing_l.add_ribs([0., 1.], body_front_wing_edges)
    sw.deformation(body_front_wing_l, body_front_wing_l_deformation)
    sw.deformation(body_front_wing_l, lambda x,y,z: (x-2., y-4.4, z-14./2.))

    body_front_accessory_edges = [(0., 0.), (2., -4.), (5., -3.), (6., 0.), (4., 2.), (1., 2.)]
    body_front_accessory = sw.rotate(np.pi/2).void(10.)
    body_front_accessory.add_ribs([0., 1.], body_front_accessory_edges)
    sw.deformation(body_front_accessory, body_accesory_deformation)
    sw.deformation(body_front_accessory, lambda x,y,z: (x+12, y-10, z-10./2.))

    front_core_accessory_small_edges_start = [(3.3, 0.8), (-3.3, 0.8), (-3.3, -0.8), (3.3, -0.8)]
    front_core_accessory_small_edges_end = [(2.2, 0.4), (-2.2, 0.4), (-2.2, -0.4), (2.2, -0.4)]
    front_core_accessory_geta_1 = sw.rotate(np.pi).void(15.)
    front_core_accessory_geta_2 = sw.rotate(-np.pi/2, np.pi/2).parent(front_core_accessory_geta_1).void(12)
    front_core_accessory_geta_3 = sw.rotate(0, -np.pi/2+np.pi).parent(front_core_accessory_geta_2).void()
    front_core_accessory_small = sw.parent(front_core_accessory_geta_3).void(10.)
    front_core_accessory_small.add_rib(0., front_core_accessory_small_edges_start)
    front_core_accessory_small.add_rib(1., front_core_accessory_small_edges_end)
    sw.deformation(front_core_accessory_small, lambda x,y,z: (x,y-1.5+0.5,z))
    sw.deformation(front_core_accessory_small, front_core_accessory_deformation)

    front_core_accessory_large_edges_start = [(3.6, 1.5), (-3.6, 1.5), (-3.6, -1.5), (3.6, -1.5)]
    front_core_accessory_large_edges_end = [(2.6, 0.8), (-2.6, 0.8), (-2.6, -0.8), (2.6, -0.8)]
    front_core_accessory_large = sw.parent(front_core_accessory_geta_3).void(10.5)
    front_core_accessory_large.add_rib(0., front_core_accessory_large_edges_start)
    front_core_accessory_large.add_rib(1., front_core_accessory_large_edges_end)
    sw.chamfering(front_core_accessory_large, 0.3)
    sw.deformation(front_core_accessory_large, front_core_accessory_deformation)

    # sw.start_display()
    sw.generate_stl_binary(path, fname)


def body_center_deformation_side_bo(x,y,z):
    if y < -0.1:
        if z < 14./2.:
            z_new = - y*(14.-7.)/(15.*2)
            return (x, y, z_new)
        else:
            z_new = 14. + y*(14.-7.)/(15.*2)
            return (x, y, z_new)
    return None

def body_center_deformation_side_lr(x,y,z):
    if x < 31. - 0.1:
        if z < 14./2.:
            z_new = (31.-x)*(14.-5.)/(31.*2)
            if z_new > z:
                return (x, y, z_new)
        else:
            z_new = 14. -(31.-x)*(14.-5.)/(31.*2)
            if z_new < z:
                return (x, y, z_new)
    return None

def body_front_cover_deformation(x,y,z):
    range = 0.5
    if 15.-range < x and x < 15.+range:
        if z < 14./2.:
            return (x, y, (14.-10.)/2.)
        else:
            return (x, y, 14.-(14.-10.)/2.)
    elif 10.-range < x and x < 10.+range:
        if z < 14./2.:
            return (x, y, (14.-10.)/2.)
        else:
            return (x, y, 14.-(14.-10.)/2.)
    elif 0.-range < x and x < 0.+range:
        if z < 14./2.:
            return (x, y, (14.-7.)/2.)
        else:
            return (x, y, 14.-(14.-7.)/2.)
        
def body_front_wing_r_deformation(x,y,z):
    range = 0.5
    if 0.-range < x and x < 0.+range:
        if z < 1./2.:
            return (x, y, (14.-7.)/2.-0.5)
        else:
            return (x, y, (14.-7.)/2.+0.5)
    elif 10.-range < x and x < 10.+range:
        if z < 1./2.:
            return (x, y, (14.-10.)/2.-0.5)
        else:
            return (x, y, (14.-10.)/2.+0.5)
    elif 26.-range < x and x < 26.+range:
        if z < 1./2.:
            return (x, y, (14.-11.)/2.-0.5)
        else:
            return (x, y, (14.-11.)/2.+0.5)
    elif 37.-range < x and x < 37.+range:
        if z < 1./2.:
            return (x, y, (14.-16.)/2.-0.5)
        else:
            return (x, y, (14.-16.)/2.+0.5)

def body_front_wing_l_deformation(x,y,z):
    range = 0.5
    if 0.-range < x and x < 0.+range:
        if z < 1./2.:
            return (x, y, 14.-(14.-7.)/2.-0.5)
        else:
            return (x, y, 14.-(14.-7.)/2.+0.5)
    elif 10.-range < x and x < 10.+range:
        if z < 1./2.:
            return (x, y, 14.-(14.-10.)/2.-0.5)
        else:
            return (x, y, 14.-(14.-10.)/2.+0.5)
    elif 20.-range < x and x < 20.+range:
        if z < 1./2.:
            return (x, y, 14.-0.5)
        else:
            return (x, y, 14.+0.5)
    elif 26.-range < x and x < 26.+range:
        if z < 1./2.:
            return (x, y, 14.-(14.-11.)/2.-0.5)
        else:
            return (x, y, 14.-(14.-11.)/2.+0.5)
    elif 37.-range < x and x < 37.+range:
        if z < 1./2.:
            return (x, y, 14.-(14.-16.)/2.-0.5)
        else:
            return (x, y, 14.-(14.-16.)/2.+0.5)

def body_accesory_deformation(x,y,z):
    if y < 2. - 0.1:
        if z < 12./2.:
            z_new = - (y-2)*(10.-8.)/(6.*2.)
            return (x, y, z_new)
        else:
            z_new = 10. + (y-2)*(10.-8.)/(6.*2.)
            return (x, y, z_new)
    return None

def front_core_accessory_deformation(x,y,z):
    if z > 0.:
        return (x, y+2.4, z)
    return None


if __name__ == "__main__":
    main()