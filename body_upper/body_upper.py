from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

body_upper_front = sw.load_submodule(os.path.join(path, 'body_upper_front'))

body_upper_back = sw.rotate(np.pi).load_submodule(os.path.join(path, 'body_upper_back'))

# sw.start_display()
sw.generate_stl_binary(path, fname)