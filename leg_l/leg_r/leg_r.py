import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

from coxa_joint.coxa_joint import Const as CoxaJointConst
from thigh.thigh import Const as ThighConst
from knee_joint.knee_joint import Const as KneeJointConst
from shin.shin import Const as ShinConst
from ankle_adapter.ankle_adapter import Const as AnkleAdapterConst
from ankle.ankle import Const as AnkleConst
from foot_adapter.foot_adapter import Const as FootAdapterConst

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    coxa_abdaction = -np.pi/64.
    coxa_flexion = 0.
    ankle_abdaction = -coxa_abdaction
    foot_adapter_flexion = -np.pi/2.+np.pi*8.25/36.
    foot_flexion = -np.pi*8.25/36.

    coxa_joint_geta_1 = sw.rotate_x(coxa_abdaction)
    coxa_joint = sw.rotate(0., -coxa_flexion).parent(coxa_joint_geta_1).load_submodule(os.path.join(path, 'coxa_joint'))
    coxa_joint_beam_1 = sw.parent(coxa_joint, 0.).void(CoxaJointConst.coxa_joint_thickness/2.)
    coxa_joint_beam_2 = sw.rotate(np.pi/2., -np.pi/2.).parent(coxa_joint_beam_1).void(CoxaJointConst.module_length)
    
    thigh = sw.parent(coxa_joint_beam_2, 1.-1./CoxaJointConst.module_length).load_submodule(os.path.join(path, 'thigh'))
    thigh.keel.set_length(ThighConst.module_length)
    thigh_beam_1 = sw.parent(thigh).move_y(ThighConst.y_move)

    leg_cover = sw.parent(thigh,0.).load_submodule(os.path.join(path, 'leg_cover'))

    knee_joint = sw.parent(thigh_beam_1).load_submodule(os.path.join(path, 'knee_joint'))
    knee_joint.keel.set_length(KneeJointConst.module_length)
    knee_joint_beam_1 = sw.parent(knee_joint).move_y(KneeJointConst.y_move)
    
    shin = sw.parent(knee_joint_beam_1).load_submodule(os.path.join(path, 'shin'))
    shin.keel.set_length(ShinConst.module_length)

    ankle_adapter = sw.parent(shin).load_submodule(os.path.join(path, 'ankle_adapter'))
    ankle_adapter.keel.set_length(AnkleAdapterConst.module_length)

    ankle_geta_1 = sw.parent(ankle_adapter).rotate(ankle_abdaction).void()
    ankle = sw.parent(ankle_geta_1).load_submodule(os.path.join(path, 'ankle'))
    ankle.keel.set_length(AnkleConst.module_length)
    ankle_beam_1 = sw.parent(ankle).move_y(AnkleConst.y_move)
    
    foot_adapter_geta_1 = sw.parent(ankle_beam_1).rotate_x(foot_adapter_flexion)
    foot_adapter = sw.parent(foot_adapter_geta_1).load_submodule(os.path.join(path, 'foot_adapter'))
    foot_adapter.keel.set_length(FootAdapterConst.module_length)

    foot_geta_1 = sw.parent(foot_adapter).rotate_x(foot_flexion)
    foot = sw.parent(foot_geta_1).load_submodule(os.path.join(path, 'foot'))
    
    # sw.start_display()
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()