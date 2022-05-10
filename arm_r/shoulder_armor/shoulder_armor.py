from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

rad_abduction_shoulder = 0. #np.pi/6.

adapter_length = 10.
adapter_edges = sw.rib_edges_circular(2.5, 2*np.pi, 8, True)
adapter_geta = sw.rotate(-np.pi).void(5.)
adapter = sw.rotate(np.pi).parent(adapter_geta).void(adapter_length)
adapter.add_rib(0., adapter_edges)
adapter.add_rib(1., adapter_edges)

adapter_base = sw.parent(adapter, 5.5/adapter_length).void(5.)
adapter_base.add_rib(0., [(2.5, 3.), (-2.5, 3.), (-2.5, -3.), (2.5, -3.)])
adapter_base.add_rib(0.4, [(2.5, 5.), (-2.5, 5.), (-2.5, -5.), (2.5, -5.)])
adapter_base.add_rib(1., [(2.5, 5.), (-2.5, 5.), (-2.5, -5.), (2.5, -5.)])

armor_base_length_top = 8.
armor_base_length_mid1 = 11.
armor_base_length_mid2 = 15.
armor_base_length_bottom = 13.

armor_base_edges = \
    [(-(armor_base_length_mid2-1.)/2, 2.5), (-armor_base_length_mid2/2., 2.5), (-armor_base_length_bottom/2., -2.5), (armor_base_length_bottom/2., -2.5), (armor_base_length_mid2/2., 2.5), ((armor_base_length_mid2-1.)/2., 2.5),\
    (armor_base_length_mid1/2., 7.5), (armor_base_length_top/2., 7.5), (armor_base_length_top/2., 11.5), (-armor_base_length_top/2., 11.5), (-armor_base_length_top/2., 7.5), (-armor_base_length_mid1/2., 7.5)]

armor_base = sw.parent(adapter, 6./adapter_length).void(5.)
armor_base.add_rib(0., armor_base_edges)
armor_base.add_rib(1., armor_base_edges)

core_geta_1 = sw.rotate(-np.pi/2, -np.pi/2).parent(armor_base, 0.5).void(7.5)

core_x_long_bottom = 15.
core_x_long_upper = 10.
core_x_short_bottom = 4.5
core_x_short_upper = 3.
core_y_long = 9.
core_y_short = 2.7
core_length = 34.

core_edges_long = [(core_x_long_upper/2., core_y_long), (-core_x_long_upper/2., core_y_long), (-core_x_long_bottom/2., 0.), (core_x_long_bottom/2., 0.)]
core_edges_short = [(core_x_short_upper/2., core_y_short), (-core_x_short_upper/2., core_y_short), (-core_x_short_bottom/2., 0.), (core_x_short_bottom/2., 0.)]

core = sw.rotate(0., -np.pi/2).parent(core_geta_1).void(core_length)
core.add_rib(0., core_edges_long)
core.add_rib(1., core_edges_short)

outer_front_edges = [(0., 0.), (2., 12.), (9., 20.), (18., 18.), (21., 15.), (47., 8.), (50., 0.)]
outer_front_edges = edges_util.translate(outer_front_edges, core_length-50.+3., -3.)
outer_front_edges_scaled = edges_util.scale(outer_front_edges.copy(), 0.9)
center_outer_front = edges_util.center(outer_front_edges)
center_outer_front_scaled = edges_util.center(outer_front_edges_scaled)
outer_front_edges_scaled = edges_util.translate(outer_front_edges_scaled, (center_outer_front[0]-center_outer_front_scaled[0])/2-1., (center_outer_front[1]-center_outer_front_scaled[1])/2)
outer_front_geta_1 = sw.rotate(-np.pi/2, 0.).parent(core, 0.).void(core_x_long_bottom/2-0.1)
outer_front_geta_2 = sw.rotate(np.pi/2-np.arctan2(core_length, (core_x_long_bottom-core_x_short_bottom)/2), 0.).parent(outer_front_geta_1).void(0.)
outer_front_geta_3 = sw.rotate(np.pi/2-np.arctan2(core_y_long, (core_x_long_bottom-core_x_long_upper)/2), np.pi/2).parent(outer_front_geta_2).void(0.)
outer_front = sw.rotate(0., -np.pi/2).parent(outer_front_geta_3).void(3.)
outer_front.add_rib(0., outer_front_edges)
outer_front.add_rib(1., outer_front_edges_scaled)

outer_back_edges = edges_util.inversion(outer_front_edges, False, True)
outer_back_edges_scaled = edges_util.scale(outer_back_edges.copy(), 0.9)
center_outer_back = edges_util.center(outer_back_edges)
center_outer_back_scaled = edges_util.center(outer_back_edges_scaled)
outer_back_edges_scaled = edges_util.translate(outer_back_edges_scaled, (center_outer_back[0]-center_outer_back_scaled[0])/2-1., (center_outer_back[1]-center_outer_back_scaled[1])/2)
outer_back_geta_1 = sw.rotate(np.pi/2, 0.).parent(core, 0.).void(core_x_long_bottom/2-0.1)
outer_back_geta_2 = sw.rotate(-np.pi/2+np.arctan2(core_length, (core_x_long_bottom-core_x_short_bottom)/2), 0.).parent(outer_back_geta_1).void(0.)
outer_back_geta_3 = sw.rotate(-np.pi/2+np.arctan2(core_y_long, (core_x_long_bottom-core_x_long_upper)/2), -np.pi/2).parent(outer_back_geta_2).void(0.)
outer_back = sw.rotate(0., -np.pi/2).parent(outer_back_geta_3).void(3.)
outer_back.add_rib(0., outer_back_edges)
outer_back.add_rib(1., outer_back_edges_scaled)

inner_edges = [(0., 0.), (0., 7.), (-1., 11.), (2., 13.), (4., 10.), (32., 3.), (34., -3.), (2., -3.)]
inner_edges = edges_util.translate(inner_edges, 2.)
inner_center_geta_1 = sw.rotate(np.pi/2, 0.).parent(core, 0.).void(0.5)
inner_center_geta_2 = sw.rotate(-np.pi, 0.).parent(inner_center_geta_1).void(0.)
inner_center = sw.parent(inner_center_geta_2).void(1.)
inner_center.add_rib(0., inner_edges)
inner_center.add_rib(1., inner_edges)

inner_front_geta_1 = sw.rotate(-np.pi/2, 0.).parent(core, 0.).void(core_x_long_bottom/4-0.5)
inner_front_geta_2 = sw.rotate(np.pi/2-np.arctan2(core_length, (core_x_long_bottom-core_x_short_bottom)/4), 0.).parent(inner_front_geta_1).void(0.)
inner_front_geta_3 = sw.rotate(np.pi/2-np.arctan2(core_y_long, (core_x_long_bottom-core_x_long_upper)/4), np.pi/2).parent(inner_front_geta_2).void(0.)
inner_front = sw.rotate(0., -np.pi/2).parent(inner_front_geta_3).void(1.)
inner_front.add_rib(0., inner_edges)
inner_front.add_rib(1., inner_edges)

inner_back_geta_1 = sw.rotate(np.pi/2, 0.).parent(core, 0.).void(core_x_long_bottom/4+0.5)
inner_back_geta_2 = sw.rotate(-np.pi, 0.).parent(inner_back_geta_1).void(0.)
inner_back_geta_3 = sw.rotate(-np.pi/2+np.arctan2(core_length, (core_x_long_bottom-core_x_short_bottom)/4), 0.).parent(inner_back_geta_2).void(0.)
inner_back_geta_4 = sw.rotate(np.pi/2-np.arctan2(core_y_long, (core_x_long_bottom-core_x_long_upper)/4), -np.pi/2).parent(inner_back_geta_3).void(0.)
inner_back = sw.rotate(0., np.pi/2).parent(inner_back_geta_4).void(1.)
inner_back.add_rib(0., inner_edges)
inner_back.add_rib(1., inner_edges)

# sw.start_display()
sw.generate_stl_binary(path, fname)