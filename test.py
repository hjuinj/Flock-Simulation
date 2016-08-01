"""
Reference sites :
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/

"""
from world import World
from flock import Flock

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
f = Flock(world = w, members = 200)

#w.playAnimation(f, w.animate3D_trace, f.genRandPositions, frames = 1)
#w.playAnimation(f, w.animate3D_trace, f.uniformVel, frames = 100)
#w.playAnimation(f, w.animate3D, f.uniformVel, frames = 100)
w.plotAvgDist(f, f.uniformVel)
#w.saveAnimation(f, w.animate3D_trace, f.uniformVel, frames = 1000)
