"""
Reference sites :
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/
Example Doc String:


    Produce a one-hot-encoding from a list of features and an OHE dictionary.

    Note:
        You should ensure that the indices used to create a SparseVector are sorted.

    Args:
        raw_feats (list of (int, str)): The features corresponding to a single observation.  Each
            feature consists of a tuple of featureID and the feature's value. (e.g. sample_one)
        ohe_dict_broadcast (Broadcast of dict): Broadcast variable containing a dict that maps
            (featureID, value) to unique integer.
        num_ohe_feats (int): The total number of unique OHE features (combinations of featureID and
            value).

    Returns:
        SparseVector: A SparseVector of length num_ohe_feats with indices equal to the unique
            identifiers for the (featureID, value) combinations that occur in the observation and
            with values equal to 1.0.
"""
from world import World
from flock import Flock
import numpy as np
"""
1. shows a frame given what type of graphics


a = World();
a.snapshot(a.drawDots3D,  a.genRandPoint(19))
"""

"""
"""
"""
points = a.animate3D_setup()
points  =  ax.plot([], [], [], 'o')[0]
def animate(i):
    coord = a.genRandPoint()
    points.set_3d_properties(coord[2])
    return [points]
anim = animation.FuncAnimation(a.fig, a.animate3D, frames = 20, fargs = (a.genRandPoint, 20), blit = True)
plt.show()
"""
w = World();
f = Flock(world = w, members = 100, orientation = np.pi/4)
w.setTraceLim(100)

#w.playAnimation(f, w.animate3D_trace, f.genRandPositions, frames = 1)
#w.playAnimation(f, w.animate3D_trace, f.uniformVel, frames = 100)
#w.playAnimation(f, w.animate3D, f.uniformVel, frames = 100)
w.playAnimation(f, w.animate3D, f.directionalVel, frames = 100)
#w.plotAvgDist(f, f.uniformVel)
#w.saveAnimation(f, w.animate3D_trace, f.uniformVel, frames = 1000)
