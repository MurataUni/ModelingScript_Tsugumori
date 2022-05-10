from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

ht_obj1 = 0.95 # thickness/2
length_obj1 = 6.

base = sw.rotate(-np.pi, 0.).void(length_obj1*0.1)
obj1 = sw.rotate(np.pi, 0.).parent(base, 1.).void(length_obj1)
obj1.add_rib(0., [(ht_obj1,0.25), (-ht_obj1,0.25), (-ht_obj1,-0.25), (ht_obj1,-0.25)])
obj1.add_rib(0.25/length_obj1, [(ht_obj1,0.5), (-ht_obj1,0.5), (-ht_obj1,-0.6), (ht_obj1,-0.6)])
obj1.add_rib(1.-0.25/length_obj1, [(ht_obj1,0.5), (-ht_obj1,0.5), (-ht_obj1,-0.6), (ht_obj1,-0.6)])
obj1.add_rib(1., [(ht_obj1,0.25), (-ht_obj1,0.25), (-ht_obj1,-0.25), (ht_obj1,-0.25)])

ht_obj2 = 1. # thickness/2
length_obj2 = 4.

base2 = sw.rotate(np.pi, 0.).parent(base, 1.).void((length_obj1 - length_obj2)/2.)
obj2 = sw.rotate(0., 0.).parent(base2, 1.).void(length_obj2)
obj2.add_rib(0., [(ht_obj2,0.9), (-ht_obj2,0.9), (-ht_obj2,0.1), (ht_obj2,0.1)])
obj2.add_rib(0.9/length_obj2, [(ht_obj2,1.), (-ht_obj2,1.), (-ht_obj2,-1.), (ht_obj2,-1.)])
obj2.add_rib(1.-0.7/length_obj2, [(ht_obj2,1.), (-ht_obj2,1.), (-ht_obj2,-1.), (ht_obj2,-1.)])
obj2.add_rib(1., [(ht_obj2,0.9), (-ht_obj2,0.9), (-ht_obj2,0.1), (ht_obj2,0.1)])

# sw.start_display()
sw.generate_stl_binary(path, fname)