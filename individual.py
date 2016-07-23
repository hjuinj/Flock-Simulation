"""
 TODO :
        -move
"""
from world import World

class Individual(object):
    def __init__(self, dim, pos = None, color = "green", shape = "^"):
        self.dim, self.color, self.shape = dim, color, shape
        if pos is None:
            self.position = np.random.rand(len(self.dim)) * (self.dim[d][1] - self.dim[d][0]) + self.dim[d][0]
        else: self.position = pos


    def setColor(self, col): self.color = col
    def getColor(self): return self.color

    def setPos(self, pos): self.position = pos
    def getPos(self): return self.position

    def setdim(self, dim): self.dim = dim
    def getdim(self): return self.dim
