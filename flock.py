"""
TODO :
        - get individual creates a dictionary of all the properties
        - method for overlap detection
        - tranparency of the individuals
        - scale for the resolution   for the velocities
        - To make analysis more analytical by adding plotting of average distances functions 

"""
from individual import Individual
import numpy as np
from scipy import spatial

class Flock(object):
    def __init__(self, world , members = 7):
        self.positions, self.colors, self.shapes, self.sizes, self.traceStyle, self.traceSize= np.zeros((members, len(world.dim))),  ["green"] * members, ["^"] * members, [2] * members, ["-"] * members, [0.5] * members
        self.world, self.members = world, members

    def addIndividual(self, ind):
        self.positions = np.concatenate((self.positions, [ind.position]))
        self.colors.append(ind.color)
        self.shapes.append(ind.shape)

    def deleteIndividual(self, index = 0):
        self.positions = np.delete(self.postions, (index), axis = 0)
        self.colors.pop(index)
        self.shapes.pop(index)

    def getPositions(self): return self.positions
    def setPositions(self, positions): self.positions = positions
    def updatePositions(self, vel):
        self.positions = np.add(self.positions, vel)
        return self.positions
    # def getIndividual(self, index): return self.flock[index]

    def uniformVel(self):
        coords = []
        for d in range(len(self.world.dim)):
            tmp = np.abs(self.world.dim[d][1] - self.world.dim[d][0])/float(self.world.resolution)

            coords.append(np.random.uniform(-tmp, tmp, self.members) )
        return self.updatePositions(np.transpose(coords))

    def genRandPositions(self):
        coords = []
        for d in range(len(self.world.dim)):
            coords.append(np.random.rand(self.members) * (self.world.dim[d][1] - self.world.dim[d][0]) + self.world.dim[d][0])
        return np.transpose(coords)

    # def coord4plot(self):
    #     return np.transpose(self.positions)
