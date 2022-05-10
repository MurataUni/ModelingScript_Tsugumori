from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

ht = 0.8 # thickness/2
length = 4.

base = sw.rotate(-np.pi, 0.).void(length*0.15)
obj = sw.rotate(np.pi, 0.).parent(base, 1.).void(length)
obj.add_rib(0., [(ht,0.5), (-ht,0.5), (-ht,-0.5), (ht,-0.5)])
obj.add_rib(0.15, [(ht,1.), (-ht,1.), (-ht,-1.), (ht,-1.)])
obj.add_rib(0.3, [(ht,1.), (-ht,1.), (-ht,-1.), (ht,-1.)])
obj.add_rib(1., [(0.,0.)])

# sw.start_display()
sw.generate_stl_binary(path, fname, divided=False)