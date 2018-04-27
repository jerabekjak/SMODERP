import math
from smoderp2d.main_classes.General import Globals as Gl


def shallowSurfaceKinematic(i,j,sur):

    a = Gl.mat_aa[i][j]
    b = Gl.mat_b[i][j]
    #print sur.h_total_pre, sur.h_crit
    h = min(sur.h_total_pre,sur.h_crit) 

    return math.pow(h, b) * a
