from harbor3d import Dock, Shipwright
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    rad_upperarm_elbow = 0. #np.pi/4
    rad_elbow_forearm = np.pi/36.
    rad_rotation_upperarm = 0. #np.pi/6. # + --> external rotation

    rad_shoulder_abduction = np.pi/36. #np.pi/6.

    body_shoulder_panel_tickness = 5.7
    body_shoulder_panel_down_modification = 10.5
    body_shoulder_panel_back_modification = 12.5
    body_shoulder_panel_edge = [\
        (0., 0.), (0., 13.3), (-1.3, 15.), (-1.3, 20.5), (16., 20.5), (30., 9.), (19.2, 0.)]
    body_shoulder_panel = sw.void(body_shoulder_panel_tickness)
    body_shoulder_panel.add_ribs([0., 1.], body_shoulder_panel_edge)
    sw.deformation(body_shoulder_panel, body_shoulder_panel_adapter_r_deformation)
    sw.deformation(body_shoulder_panel, lambda x,y,z: (x-body_shoulder_panel_back_modification, y-body_shoulder_panel_down_modification, z))

    shoulder_armor_geta_upward = 12.5 - body_shoulder_panel_down_modification
    shoulder_armor_geta_backward = body_shoulder_panel_back_modification - 9.
    shoulder_armor_geta_1 = sw.rotate(-np.pi/2).parent(body_shoulder_panel).void(shoulder_armor_geta_backward)
    shoulder_armor_geta_2 = sw.rotate(np.pi/2).parent(shoulder_armor_geta_1).void()
    shoulder_armor_geta_3 = sw.rotate(np.pi/2, np.pi/2).parent(shoulder_armor_geta_2).void(shoulder_armor_geta_upward)
    shoulder_armor_geta_4 = sw.rotate(-np.pi/2).parent(shoulder_armor_geta_3).void()
    shoulder_armor_geta_5 = sw.rotate(0., -np.pi/2).parent(shoulder_armor_geta_4).void()

    shoulder_armor = sw.parent(shoulder_armor_geta_5).load_submodule(os.path.join(path, 'shoulder_armor')).align_keel_size_to_monocoque_shell()

    shoulder_adapter_geta_1 = sw.parent(shoulder_armor, 0.).void(5.)
    shoulder_adapter_geta_2 = sw.rotate(-rad_shoulder_abduction, -np.pi/2).parent(shoulder_adapter_geta_1).void(0.)
    shoulder_adapter_geta_3 = sw.rotate(0., np.pi/2).parent(shoulder_adapter_geta_2).void(0.)

    shoulder = sw.parent(shoulder_adapter_geta_3).load_submodule(os.path.join(path, 'shoulder')).align_keel_size_to_monocoque_shell()
    shoulder_adapter1 = sw.parent(shoulder, 0.).void(4.5)
    shoulder_adapter2 = sw.rotate(np.pi/2, -np.pi/2).parent(shoulder_adapter1).void(4.5)

    upperarm = sw.rotate(0., rad_rotation_upperarm).parent(shoulder_adapter2).load_submodule(os.path.join(path, 'upperarm_r')).align_keel_size_to_monocoque_shell()
    upperarm_adapter1 = sw.rotate(np.pi/2, np.pi/2).parent(upperarm, 1.-3./upperarm.keel.length).void(1.5)
    upperarm_adapter2 = sw.rotate(rad_upperarm_elbow-np.pi/2).parent(upperarm_adapter1).void()

    elbow = sw.rotate(0., -np.pi/2).parent(upperarm_adapter2).load_submodule(os.path.join(path, 'elbow')).align_keel_size_to_monocoque_shell()
    elbow_adapter = sw.rotate(rad_elbow_forearm, np.pi/2).parent(elbow, 1.-2./elbow.keel.length).void()
    forearm = sw.rotate(0., -np.pi/2).parent(elbow_adapter).load_submodule(os.path.join(path, 'forearm_r')).align_keel_size_to_monocoque_shell()

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def body_shoulder_panel_adapter_r_deformation(x,y,z):
    target = [\
        (0., 0.), (0., 13.3), (-1.3, 15.), (-1.3, 20.5), (16., 20.5), (30., 9.), (19.2, 0.)]
    range = 0.1
    tickness = 5.7
    if target[4][0]-range < x and x < target[4][0]+range:
        if z < tickness/2.:
            return (x+1.5, y, z-1.5)
    elif target[5][0]-range < x and x < target[5][0]+range:
        if z < tickness/2.:
            return (x+2.2, y, z-1.6)
        else:
            return (x, y, z-0.5)
    elif target[6][0]-range < x and x < target[6][0]+range:
        if z < tickness/2.:
            return (x+1.5, y, z-1.5)
    else:
        if z < tickness/2.:
            return (x, y, z-1.5)
    return None

if __name__ == "__main__":
    main()