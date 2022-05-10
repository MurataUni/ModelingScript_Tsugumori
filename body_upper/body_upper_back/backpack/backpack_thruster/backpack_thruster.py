from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())


    thuruster_edges = [(-12., 0.), (-14., 1.), (-10., 13.), (0., 20.), (10., 13.), (14., 1.), (12., 0.)]
    thuruster_thickness = 11.2
    thuruster = sw.void(thuruster_thickness)
    thuruster.add_ribs([0.,1.], thuruster_edges)
    sw.deformation(thuruster, lambda x,y,z: (x,y-1.,z))

    nozzle_skirt_outer_edges = [\
        (0., 0.),(0., 12.),(0., 19.5),(19., 22.8),(20.6, 17.3),\
        (16.8, 14.2),(16.5, 12.),(16.8, 7.),(19.8, 2.9),(19.4, 0.)]
    nozzle_skirt_outer_thickness = 1.8
    nozzle_skirt_outer_r_geta_1 = sw.move_x(13.)
    nozzle_skirt_outer_r = sw.rotate(-np.pi/2).parent(nozzle_skirt_outer_r_geta_1).void(nozzle_skirt_outer_thickness)
    nozzle_skirt_outer_r.add_ribs([0.,1.], nozzle_skirt_outer_edges)
    sw.deformation(nozzle_skirt_outer_r, lambda x,y,z: (x,y,z-nozzle_skirt_outer_thickness/2.))
    sw.deformation(nozzle_skirt_outer_r, nozzle_skirt_outer_r_deformation)
    sw.deformation(nozzle_skirt_outer_r, lambda x,y,z: (x,y+0.2,z))

    nozzle_skirt_outer_l_geta_1 = sw.move_x(-13.)
    nozzle_skirt_outer_l = sw.rotate(-np.pi/2).parent(nozzle_skirt_outer_l_geta_1).void(nozzle_skirt_outer_thickness)
    nozzle_skirt_outer_l.add_ribs([0.,1.], nozzle_skirt_outer_edges)
    sw.deformation(nozzle_skirt_outer_l, lambda x,y,z: (x,y,z-nozzle_skirt_outer_thickness/2.))
    sw.deformation(nozzle_skirt_outer_l, nozzle_skirt_outer_r_deformation)
    sw.deformation(nozzle_skirt_outer_l, lambda x,y,z: (x,y+0.2,-z))
    for triangle in nozzle_skirt_outer_l.monocoque_shell.triangles:
        triangle.inverse()

    nozzle_skirt_inner_edges = [\
        (0.,0.),(0.,11.),(0.,20.),(19.5,22.5),(22.,16.5),\
        (18.1,14.),(17.8,11.),(18.1,7.),(21.,2.6),(20.8,0.)]
    nozzle_skirt_inner_thickness = 1.8
    nozzle_skirt_inner_r_geta_1 = sw.move_x(5.4)
    nozzle_skirt_inner_r = sw.rotate(-np.pi/2).parent(nozzle_skirt_inner_r_geta_1).void(nozzle_skirt_inner_thickness)
    nozzle_skirt_inner_r.add_ribs([0.,1.], nozzle_skirt_inner_edges)
    sw.deformation(nozzle_skirt_inner_r, lambda x,y,z: (x,y,z-nozzle_skirt_inner_thickness/2.))
    sw.deformation(nozzle_skirt_inner_r, nozzle_skirt_inner_r_deformation)
    sw.deformation(nozzle_skirt_inner_r, lambda x,y,z: (x+2.,y+1.,z))
    
    nozzle_skirt_inner_l_geta_1 = sw.move_x(-5.4)
    nozzle_skirt_inner_l = sw.rotate(-np.pi/2).parent(nozzle_skirt_inner_l_geta_1).void(nozzle_skirt_inner_thickness)
    nozzle_skirt_inner_l.add_ribs([0.,1.], nozzle_skirt_inner_edges)
    sw.deformation(nozzle_skirt_inner_l, lambda x,y,z: (x,y,z-nozzle_skirt_inner_thickness/2.))
    sw.deformation(nozzle_skirt_inner_l, nozzle_skirt_inner_r_deformation)
    sw.deformation(nozzle_skirt_inner_l, lambda x,y,z: (x+2.,y+1.,-z))
    for triangle in nozzle_skirt_inner_l.monocoque_shell.triangles:
        triangle.inverse()

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def nozzle_skirt_outer_r_deformation(x,y,z):
    range = 0.1
    x_tilt = 2.5/20.
    y_tilt_under = 4./12.
    y_tilt_upper = 6./8.
    if 12. - range < y:
        return (x,y,z-x_tilt*x+y_tilt_upper*(y-12.)+y_tilt_under*12.)
    else:
        return (x,y,z-x_tilt*x+y_tilt_under*y)

def nozzle_skirt_inner_r_deformation(x,y,z):
    range = 0.1
    x_tilt = 1.5/20.
    y_tilt_under = 0.5/12.
    y_tilt_upper = 3.9/8.
    if 12. - range < y:
        return (x,y,z-x_tilt*x+y_tilt_upper*(y-12.)+y_tilt_under*12.)
    else:
        return (x,y,z-x_tilt*x+y_tilt_under*y)


if __name__ == "__main__":
    main()