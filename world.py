"""
 TODO :
        - add line trajectory (static frame) DONE
        - allow shape and color change for members in aniamte3d_setup
        - move random move to flock.py
        - modify resolution to account for non-cubic box
        - line trace should fade after certain iteration
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class World(object):
    def __init__(self, resolution = 64,  dim = [[-1, 1], [-1, 1], [-1, 1]], trace_lim = 7):
        self.dim, self.resolution = dim, resolution
        # the trace for the trajectory shouldn't be too large to avoid storing too much data
        self.trace_lim = trace_lim


    def setDim(self, dim): self.dim = dim
    def getDim(self): return self.dim

    # def genRandPoint(self,  fields ): #fields will be deprecated
    #     coords = []
    #     n = self.members
    #     if isinstance(fields, int):
    #         n = fields
    #     elif len(fields) != 0 :
    #         n = fields[0]
    #
    #
    #     for d in range(len(self.dim)):
    #         #np.random.seed(20)
    #         coords.append(np.random.rand(n) * (self.dim[d][1] - self.dim[d][0]) + self.dim[d][0])
    #     return np.transpose(coords)

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

    def animate3D_setup(self, flock):
        self.members = flock.members
        ax = self.worldSetup()
        self.traj = [[[0 for i in range(self.trace_lim)] for j in range(len(self.dim))] for k in range(self.members)] # keep track of line trajectory
        points  =  [ax.plot([], [], [],flock.shapes[i], c = flock.colors[i], ms = flock.sizes[i])[0] for i in range(self.members)]
        lines = [ax.plot([], [], [],  ls = flock.traceStyle[i], lw = flock.traceSize[i], c = flock.colors[i])[0] for i in range(self.members)]
        return points, lines

    def animate3D(self, frame,  fields ):
        if fields[1 : ] == () :
            coord = fields[0]()
        else:
            coord = fields[0](fields[1 : ])
        for i in range(self.members):
            self.points[i].set_data(coord[i][0], coord[i][1])
            self.points[i].set_3d_properties( coord[i][2])
        return self.points

    def animate3D_trace(self, frame, fields):
        if fields[1 : ] == () :
            coord = fields[0]()
        else:
            coord = fields[0](fields[1 : ])
        for i in range(self.members):
            self.points[i].set_data(coord[i][0], coord[i][1])
            self.points[i].set_3d_properties( coord[i][2])
            for j in range(len(self.dim)):
                self.traj[i][j].pop(0)
                self.traj[i][j].append(coord[i][j])
            self.lines[i].set_data(self.traj[i][0][-self.trace_lim : ], self.traj[i][1][-self.trace_lim : ])
            self.lines[i].set_3d_properties( self.traj[i][2][-self.trace_lim : ])

        return self.points + self.lines

    def playAnimation(self, members, func, *args, **kwargs ):
        self.points, self.lines = self.animate3D_setup(members)
        frames = 20
        if "frames" in kwargs:
            frames = kwargs["frames"]
        anim = animation.FuncAnimation(self.fig, func, frames = frames, fargs = (args, ), blit = True)
        plt.show()

    #def genRandLine(self):
    #def test(self):
