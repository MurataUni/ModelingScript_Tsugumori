from harbor3d import Dock, Shipwright
from harbor3d.util import bpy_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

body_upper_front = sw.load_submodule(os.path.join(path, 'body_upper'))

lower_body_geta_1 = sw.rotate_x(np.pi/2.)
lower_body_geta_2 = sw.parent(lower_body_geta_1).void(24.1)
lower_body = sw.rotate(0.,np.pi).parent(lower_body_geta_2).load_submodule(os.path.join(path, 'body_lower'))

leg_geta_1 = sw.parent(lower_body_geta_2).void(16.)
leg_geta_2 = sw.parent(leg_geta_1).move_y(1.)
leg_geta_l_1 = sw.rotate(np.pi/2.).parent(leg_geta_2).void(12.)
leg_l = sw.rotate(0., -np.pi/2.).parent(leg_geta_l_1).load_submodule(os.path.join(path, 'leg_l'))

leg_geta_r_1 = sw.rotate(-np.pi/2.).parent(leg_geta_2).void(12.)
leg_r = sw.rotate(0., np.pi/2.).parent(leg_geta_r_1).load_submodule(os.path.join(path, 'leg_r'))

body_cover_back_move = 7.
body_cover_down_move = 2.
body_cover_adapter_length = 14.
body_cover_geta_1 = sw.rotate(-np.pi).void(body_cover_back_move)
body_cover_geta_2 = sw.rotate(np.pi).parent(body_cover_geta_1).void()
body_cover_geta_3 = sw.rotate(-np.pi/2, np.pi/2).parent(body_cover_geta_2).void(body_cover_down_move)
body_cover_geta_4 = sw.rotate(np.pi/2).parent(body_cover_geta_3).void()
body_cover_geta_5 = sw.rotate(0., -np.pi/2).parent(body_cover_geta_4).void()

body_shoulder_panel_adapter_r = sw.rotate(-np.pi/2).parent(body_cover_geta_5).rectangular(8., 8., body_cover_adapter_length)
shoulder_armor = sw.parent(body_shoulder_panel_adapter_r, 1.-2.5/body_cover_adapter_length).load_submodule(os.path.join(path, 'arm_r'))

body_shoulder_panel_adapter_l = sw.rotate(np.pi/2).parent(body_cover_geta_5).rectangular(8., 8., body_cover_adapter_length)
shoulder_armor = sw.parent(body_shoulder_panel_adapter_l, 1.-2.5/body_cover_adapter_length).load_submodule(os.path.join(path, 'arm_l'))

# sw.start_display()
sw.generate_stl_binary(path, fname)
# bpy_util.union_in_dir(os.path.join(path, "divided"), os.path.join(path, fname))

sw.clear_dock()
model = sw.load_submodule(path)
scale = 1/2
sw.deformation_all(lambda x,y,z: (x*scale,y*scale,z*scale))
sw.generate_stl_binary(path, "scaled_"+fname)
