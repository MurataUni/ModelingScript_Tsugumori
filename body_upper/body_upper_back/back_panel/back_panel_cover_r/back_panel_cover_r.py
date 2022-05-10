from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    back_panel_cover_r_edges = [\
        (6.02, 3.39), (-4.11, 3.39), (-4.11, 12.58), (-10.7, 15.39), (-2.27, 26.99),\
        (2.33, 28.44), (6.61, 23.68), (5.27, 21.42), (0.51, 25.13), (-4.83, 16.61),\
        (6.02, 13.22)]
    
    back_panel_cover_r = sw.rotate(np.pi/2., np.pi).void(1.6)
    back_panel_cover_r.add_ribs([0.,1.], back_panel_cover_r_edges)
    sw.deformation(back_panel_cover_r, lambda x,y,z: (x,y,z-0.2))
    sw.deformation(back_panel_cover_r, back_panel_cover_r_deformation)
    sw.deformation(back_panel_cover_r, lambda x,y,z: (x-1.,y-1.,z))

    # sw.start_display()
    sw.generate_stl_binary(path, fname)

def back_panel_cover_r_deformation(x,y,z):
    target = [\
        (6.02, 3.39), (-4.11, 3.39), (-4.11, 12.58), (-10.7, 15.39), (-2.27, 26.99),\
        (2.33, 28.94), (6.61, 24.18), (5.27, 21.42), (0.51, 25.13), (-4.83, 16.61),\
        (6.02, 13.22)]
    range = 0.01
    z_mod1_2 = (12.-8.5)/2.
    z_mod3 = (12.-6.2)/2.
    z_mod4 = (12.-6.)/2.
    z_mod5 = (12.-6.)/2.
    z_mod6 = (12.-11.)/2.
    z_mod7 = (12.-11.)/2.
    z_mod8 = (12.-6.)/2.
    z_mod9 = (12.-6.5)/2.
    if target[1][0]-range < x and x < target[1][0]+range:
        return (x,y,z-z_mod1_2)
    elif target[3][0]-range < x and x < target[3][0]+range:
        return (x,y,z-z_mod3)
    elif target[4][0]-range < x and x < target[4][0]+range:
        return (x,y,z-z_mod4)
    elif target[5][0]-range < x and x < target[5][0]+range:
        return (x,y,z-z_mod5)
    elif target[6][0]-range < x and x < target[6][0]+range:
        return (x,y,z-z_mod6)
    elif target[7][0]-range < x and x < target[7][0]+range:
        return (x,y,z-z_mod7)
    elif target[8][0]-range < x and x < target[8][0]+range:
        return (x,y,z-z_mod8)
    elif target[9][0]-range < x and x < target[9][0]+range:
        return (x,y,z-z_mod9)
    return None

if __name__ == "__main__":
    main()