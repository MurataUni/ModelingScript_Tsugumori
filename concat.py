from harbor3d import Dock, Shipwright
from harbor3d.util.concat_util import ConcatConfig, Concatinator
from harbor3d.util import stl_delete_shell_util
import os
import glob
import numpy as np

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname_remeshed ='scaled_remeshed.stl'
    fname_shell_cleared = 'scaled_shell_cleared.stl'
    
    list_fname = []
    if os.path.exists(os.path.join(path, "divided")):
        list_fname = glob.glob(os.path.join(path, "divided/*.stl"))
    if 0 == len(list_fname):
        return

    sw = Shipwright(Dock())
    catConfig = ConcatConfig(0.15, 0.15)
    c = Concatinator(catConfig, sw)
    c.init_shells_data(list_fname)
    c.border_data_load()
    c.output(os.path.join(path, fname_remeshed))
    stl_delete_shell_util.delete_separated_shell(sw, path, fname_remeshed, fname_shell_cleared, (0,0,-1))

if __name__ == "__main__":
    main()