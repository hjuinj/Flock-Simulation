"""
 TODO :
        - add line trajectory (static frame)
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class World():
    def __init__(self, dim = [[-1, 1], [-1, 1], [-1, 1]]):
        self.dim = dim

    def genRandPoint(self,  args ):
        coords = []
        print "genRandPoint"
        print args
        n = 1
        try:
            n = args[0]
        except IndexError:
            pass
        print n
        for d in range(len(self.dim)):
            coords.append(np.random.rand(n) * (self.dim[d][1] - self.dim[d][0]) + self.dim[d][0])
        return coords

    def drawDots3D(self, ax, coords):
        return ax.scatter(coords[0], coords[1], coords[2])

    def snapshot(self, func, *args):
        ax = self.worldSetup()
        func(ax, *args)
        plt.show()

    def worldSetup(self):
        self.fig = plt.figure()
        if len(self.dim)  == 2:
            ax = plt.axes(self.fig)
            ax.set_xlim(self.dim[0])
            ax.set_xlabel('X')
            ax.set_ylim(self.dim[1])
            ax.set_ylabel('Y')
            return ax

        if len(self.dim) == 3 :
            ax = p3.Axes3D(self.fig)
            ax.set_xlim3d(self.dim[0])
            ax.set_xlabel('X')
            ax.set_ylim3d(self.dim[1])
            ax.set_ylabel('Y')
            ax.set_zlim3d(self.dim[2])
            ax.set_zlabel('Z')
            return ax

    def animate3D_setup(self):
        ax = self.worldSetup()
        points  =  ax.plot([], [], [], 'o')[0]
        return points

    def animate3D(self, frame,  func, args ):
        print "animate3d"
        print args
        coord = func(args)
        self.points.set_data(coord[0], coord[1])
        self.points.set_3d_properties( coord[2])
        return [self.points]

    def playAnimation(self, func, *args ):
        self.points = self.animate3D_setup()

        anim = animation.FuncAnimation(self.fig, self.animate3D, frames = 20, fargs = (func,  args), blit = True)
        plt.show()



    #def genRandLine(self):
    #def test(self):

a = World();
"""
a.snapshot(a.drawDots3D,  a.genRandPoint(19))
"""

"""
points = a.animate3D_setup()
points  =  ax.plot([], [], [], 'o')[0]
def animate(i):
    coord = a.genRandPoint()
    points.set_data(coord[0], coord[1])
    points.set_3d_properties(coord[2])
    return [points]
anim = animation.FuncAnimation(fig, animate, frames = 20, blit = True)
anim = animation.FuncAnimation(a.fig, a.animate3D, frames = 20, fargs = (a.genRandPoint, 20), blit = True)
plt.show()

a.playAnimation(a.genRandPoint )

"""
#class Individual():
