from harbor3d import Dock, Shipwright
import numpy as np
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fname = path.split(os.sep)[-1] + '.stl'

sw = Shipwright(Dock())

ht_obj = 1. # thickness/2
length_obj = 4.

base = sw.rotate(np.pi).void(length_obj/10.)

obj2 = sw.rotate(-np.pi).parent(base).void(length_obj)
obj2.add_rib(0., [(ht_obj,0.5), (-ht_obj,0.5), (-ht_obj,-0.5), (ht_obj,-0.5)])
obj2.add_rib(0.1, [(ht_obj,1.), (-ht_obj,1.), (-ht_obj,-1.), (ht_obj,-1.)])
obj2.add_rib(1.-1.2/length_obj, [(ht_obj,1.), (-ht_obj,1.), (-ht_obj,-1.), (ht_obj,-1.)])
obj2.add_rib(1., [(ht_obj,0.9), (-ht_obj,0.9), (-ht_obj,0.1), (ht_obj,0.1)])

# sw.start_display()
sw.generate_stl_binary(path, fname, divided=False)