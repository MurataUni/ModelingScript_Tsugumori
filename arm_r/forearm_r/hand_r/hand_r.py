from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

wrist_length = 2.
palm_bottom_length = 4.
palm_bottom_widt = 4.
palm_bottom_vert = 3.

rad_ft_j = (np.pi/4, np.pi/8, np.pi/8)
rad_ft_bending = np.pi*40/180
rad_ft_rotation = -np.pi/2

base = sw.rotate(np.pi).void(0.5)
wrist = sw.rotate(-np.pi).parent(base).pole(wrist_length, 1.5, 2*np.pi, 6, True)
palm_bottom = sw.parent(wrist, 1. - 0.1/wrist_length).rectangular(palm_bottom_widt, palm_bottom_vert, palm_bottom_length)

palm_adapter1 = sw.rotate(np.pi/2, np.pi/2).parent(wrist).void(palm_bottom_vert/4)
palm_adapter2 = sw.rotate(-np.pi/2).parent(palm_adapter1).void()
palm = sw.rotate(0., -np.pi/2).parent(palm_adapter2).load_submodule(os.path.join(path, 'palm')).align_keel_size_to_monocoque_shell()

thumb_base_adapter1 = sw.parent(wrist).void(palm_bottom_length-1.5)
thumb_base_adapter2 = sw.rotate(np.pi/2).parent(thumb_base_adapter1).void()
thumb_base_adapter3 = sw.rotate(-np.pi/2, np.pi/2).parent(thumb_base_adapter2).void(palm_bottom_vert/4)
thumb_base_adapter4 = sw.rotate(np.pi/2, 0.).parent(thumb_base_adapter3).void()
thumb_base = sw.rotate(0., -np.pi/2).parent(thumb_base_adapter4).void(3.5)
thumb_base.add_rib(0., [(0.8, 1.), (-1.5, 1.), (-1.5, -0.5), (0.8, -0.5)])
thumb_base.add_rib(1., [(0.3, 1.), (-1.5, 1.), (-1.5, -0.5), (0.3, -0.5)])

thumb_adapter_1 = sw.rotate(rad_ft_bending, -np.pi/2).parent(thumb_base).void()
thumb_adapter_2 = sw.rotate(0., np.pi/2).parent(thumb_adapter_1).void()
thumb_adapter_3 = sw.rotate(0., rad_ft_rotation).parent(thumb_adapter_2).void()

t_j3 = sw.rotate(rad_ft_j[0], -np.pi/2).parent(thumb_adapter_3).void(0.)
t_p3 = sw.rotate(0., np.pi/2).parent(t_j3).load_submodule(os.path.join(path, 'thumb_3')).align_keel_size_to_monocoque_shell()
t_j2 = sw.rotate(rad_ft_j[1], -np.pi/2).parent(t_p3).void(0.)
t_p2 = sw.rotate(0., np.pi/2).parent(t_j2).load_submodule(os.path.join(path, 'thumb_2')).align_keel_size_to_monocoque_shell()
t_j1 = sw.rotate(rad_ft_j[2], -np.pi/2).parent(t_p2, 1-1./7).void(0.)
t_p1 = sw.rotate(0., np.pi/2).parent(t_j1).load_submodule(os.path.join(path, 'palm' + os.sep + 'finger_1')).align_keel_size_to_monocoque_shell()

# sw.start_display()
sw.generate_stl_binary(path, fname)