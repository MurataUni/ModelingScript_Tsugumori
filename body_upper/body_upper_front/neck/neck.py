from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

rad_neck_joint_1 = 0.
rad_neck_joint_2 = 0.
rad_neck_joint_3 = 0.
rad_head_left = 0.
rad_head_abduction = np.pi/24.

# neck_base_length = 2.

neck_thickness = 4.
neck_depth = 4.
neck_joint_length = 6.
neck_thickness_cham = 2.
neck_depth_cham = 2.

neck_edge = [(neck_depth/2, neck_thickness/2), (-neck_depth/2, neck_thickness/2), (-neck_depth/2, -neck_thickness/2), (neck_depth/2, -neck_thickness/2)]
neck_edge_end = [\
    ((neck_depth-neck_depth_cham)/2, (neck_thickness-neck_thickness_cham)/2), \
    (-(neck_depth-neck_depth_cham)/2, (neck_thickness-neck_thickness_cham)/2), \
    (-(neck_depth-neck_depth_cham)/2, -(neck_thickness-neck_thickness_cham)/2), \
    ((neck_depth-neck_depth_cham)/2, -(neck_thickness-neck_thickness_cham)/2)]

neck_geta_1 = sw.rotate(np.pi, -np.pi/2).void(1.5)
neck_joint_1 = sw.rotate(rad_neck_joint_1-np.pi, 0.).parent(neck_geta_1).void(neck_joint_length)
neck_joint_1.add_ribs([0., 1.], neck_edge_end)
neck_joint_1.add_ribs([2./neck_joint_length, 1.-(2./neck_joint_length)], neck_edge)
neck_joint_1.order_ribs()

neck_joint_2_geta = sw.rotate(np.pi).parent(neck_joint_1).void(1.5)
neck_joint_2 = sw.rotate(rad_neck_joint_2-np.pi, 0.).parent(neck_joint_2_geta).void(neck_joint_length)
neck_joint_2.add_ribs([0., 1.], neck_edge_end)
neck_joint_2.add_ribs([2./neck_joint_length, 1.-(2./neck_joint_length)], neck_edge)
neck_joint_2.order_ribs()

neck_joint_3_geta = sw.rotate(np.pi).parent(neck_joint_2).void(1.5)
neck_joint_3 = sw.rotate(rad_neck_joint_3-np.pi, 0.).parent(neck_joint_3_geta).void(neck_joint_length)
neck_joint_3.add_ribs([0., 1.], neck_edge_end)
neck_joint_3.add_ribs([2./neck_joint_length, 1.-(2./neck_joint_length)], neck_edge)
neck_joint_3.order_ribs()

neck_cover_joint_1_geta = sw.rotate(np.pi/2).parent(neck_joint_1, 0.).void(0.)
neck_cover_joint_1 = sw.rotate(0.,np.pi/2).parent(neck_cover_joint_1_geta).load_submodule(os.path.join(path, 'neck_cover'))

neck_cover_joint_2_geta = sw.rotate(np.pi/2).parent(neck_joint_2, 0.).void(0.)
neck_cover_joint_2 = sw.rotate(0.,np.pi/2).parent(neck_cover_joint_2_geta).load_submodule(os.path.join(path, 'neck_cover'))

neck_cover_joint_3_geta = sw.rotate(np.pi/2).parent(neck_joint_3, 0.).void(0.)
neck_cover_joint_3 = sw.rotate(0.,np.pi/2).parent(neck_cover_joint_3_geta).load_submodule(os.path.join(path, 'neck_cover'))

head_geta_1 = sw.rotate(-np.pi/2, np.pi/2).parent(neck_joint_3, 1.-1.5/neck_joint_length).void()
head_geta_2 = sw.rotate(np.pi/2, -np.pi/2).parent(head_geta_1, 1.-1.5/neck_joint_length).void()
head_geta_3 = sw.rotate(rad_head_left).parent(head_geta_2, 1.-1.5/neck_joint_length).void()
head_geta_4 = sw.rotate(-rad_head_abduction, np.pi/2).parent(head_geta_3, 1.-1.5/neck_joint_length).void()
head = sw.rotate(0., -np.pi/2).parent(head_geta_4).load_submodule(os.path.join(path, 'head'))

# sw.start_display()
sw.generate_stl_binary(path, fname)