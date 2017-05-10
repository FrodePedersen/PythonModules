import numpy as np
from Bio import Phylo 
import os

class Utility():

    def __init__(self):
        pass

    def readData(self, filename):
        f = open(filename).read().split("\n")
        dim = int(f[0])
        m = np.zeros(shape=(dim, dim))
        names = []
        i = 0
        for row in f[1:]:
            data = row.split(" ")
            if len(data[0])==0: break
            names.append(data[0])
            j = 0
            for d in data[1:]:
                if d=="0.00":
                    m[i,j] = 0
                else:
                    m[i,j] = float(d)
                j += 1
            i += 1
        return m, names

    def rowSums(self, matrix):
        r = []
        for i in range(0, matrix.shape[0]):
            r.append(float(np.sum(matrix[i,])))
        return r
    
    def relabelLeaves(self, T, name_map = {}):
        if name_map == {}:
            c = 0
            for leaf in T.get_terminals():
                name_map[leaf.name] = str(c)
                leaf.name = str(c)
                c += 1
        else:
            for leaf in T.get_terminals():
                leaf.dfs = name_map[leaf.name]

        return name_map

    def rootTrees(self, T1, T2):
        from random import randint
        terminals = T1.get_terminals()
        rand_index = randint(0,len(terminals)-1)
        root = terminals[rand_index].name
        T1.root_with_outgroup(root)
        T2.root_with_outgroup(root)

    def readTree(self, filename, filetype="newick"):
        return Phylo.read(filename, filetype)

    def getChildren(self, node):
        return [child for child in node]

    def getFileInTestdata(self,filename):
        return os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), "Testdata", filename)
    
