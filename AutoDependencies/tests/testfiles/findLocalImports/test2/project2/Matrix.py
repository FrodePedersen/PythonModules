import numpy as np
from Utility import Utility

# Wrapper for numpy matrices
class Matrix(np.ndarray):

    names = []
    indices = []
    
    def __new__(cls, data):
        utility = Utility()
        if type(data)==str:
            m, names = utility.readData(data)
            obj = m.view(cls)
            obj.names = names
            obj.indices = list(range(0, len(names)))
            return obj
        obj = np.asarray(data).view(cls)
        return obj

    def __str__(self):
        s = ""
        c = 0
        for i in self.indices:
            s += " "*5*c
            s += "["
            for j in self.indices[c:]:
                s += " %.2f" % self[i,j]
            s += " ]\n"
            c += 1
        return s[:-1]
    
    def __iter__(self):
        c = 0
        for x in self.indices:
            for y in self.indices[c:]:
                if x!=y:
                    yield (x, y, self[x, y])
            c += 1
    
    def removeIndex(self, i):
        c = 0
        for j in self.indices:
            if j==i:
                self.indices = self.indices[:c]+self.indices[(c+1):]
                break
            c += 1

    def sortIndicesBy(self, l):
        self.indices = sorted(self.indices, key=lambda x: l[x], reverse=True)

    def sortIndices(self):
        self.indices = sorted(self.indices)
    
