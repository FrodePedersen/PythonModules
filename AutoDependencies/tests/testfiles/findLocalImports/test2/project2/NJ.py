from Matrix import Matrix
from Utility import Utility
import Bio.Phylo

class NJ():

    def __init__(self, filename):
        self.utility = Utility()
        self.D = Matrix(filename)
        self.r = self.utility.rowSums(self.D)
        self.tree = self.initStarTree()
        self.uniqueId = 0
        
    def start(self):
        self.constructTree()

    def constructTree(self, outfile, heuristic=True):
        #print "Constructing the tree"
        NumberofClusters = self.D.shape[0]
        while NumberofClusters>3:
            if heuristic==True:
                self.D.sortIndicesBy(self.r)
                i, j = self.findQminHeuristic()
            else:
                i, j = self.findQmin()
            k = self.updateTree(i, j)
            self.updateMatrix(i, j, k)
            NumberofClusters -= 1 #Hopefully
        self.finishTree()
        self.clearDummies()
        #print self.tree
        Bio.Phylo.write(self.tree, outfile, "newick")

    def findQmin(self):
        divr = len(self.D.indices)-2
        first_time = True
        for m in self.D:
            q = m[2]
            ri = self.r[m[0]]/divr
            rj = self.r[m[1]]/divr
            if first_time:
                qmin = [q-(ri+rj), m[0], m[1]]
                first_time = False
            else:
                new_q = q-(ri+rj)
                if qmin[0] > new_q:
                    qmin = [new_q, m[0], m[1]]
        return qmin[1], qmin[2]

    def findQminHeuristic(self):
        divr = len(self.D.indices)-2
        qmin = float("inf")
        ij = [0,0]
        c = 0
        for i in self.D.indices:
            for j in self.D.indices[c:]:
                if i!=j:
                    q = self.D[i,j]-(self.r[i]/divr-self.r[j]/divr)
                    if qmin>q:
                        qmin = q
                        ij[0], ij[1] = i, j
                    else:
                        break
            c += 1
        return ij
    
    def updateTree(self, i, j):
        # i and j are indices to the names list of the matrix.
        newCladeName = "intermediateNode" + str(self.uniqueId)

        child1 = Bio.Phylo.Newick.Clade(name = self.D.names[i],
                                        branch_length = (self.D[i,j] + self.r[i] - self.r[j]) * 0.5,
                                        clades = self.tree.root[i].clades)
        child2 = Bio.Phylo.Newick.Clade(name = self.D.names[j],
                                        branch_length = (self.D[i,j] + self.r[j] - self.r[i]) * 0.5,
                                        clades = self.tree.root[j].clades)
        
        intermediateNode = Bio.Phylo.Newick.Clade(name = newCladeName, clades = [child1, child2])

        maxIndex = max(i,j)
        minIndex = min(i,j) 

        self.tree.root.clades[minIndex] = intermediateNode 
        self.tree.root.clades[maxIndex].name = "DUMMY"

        self.D.names[minIndex] = newCladeName

        self.uniqueId += 1
        
        return maxIndex

    def updateMatrix(self, i, j, k):
        if i == k:
            other = i
        else:
            other = j
            
        for m in self.D.indices:
            if (m != k) and (m != other):
                self.r[m] -= (self.D[m, k] + self.D[m, other])
                dkm = (self.D[m,k] + self.D[m,other] - self.D[k,other])/2
                self.D[k,m] = dkm
                self.D[m,k] = dkm
                self.r[m] += dkm

        self.D.removeIndex(k)

    #Constructing the star tree.
    def initStarTree(self):

        #Creates a rooted tree with all the sequences being children of root
        return Bio.Phylo.Newick.Tree(root=Bio.Phylo.Newick.Clade(clades=[Bio.Phylo.Newick.Clade(name=i) for i in self.D.names]))


    def clearDummies(self):

        dummies = []

        i = 0
        for clade in self.tree.root.clades:
            if clade.name=="DUMMY":
                dummies.append(i)
            i += 1

        for i in dummies[::-1]:
            self.tree.root.clades.pop(i)

        for i in self.tree.get_nonterminals():
            i.name = None

    def finishTree(self):

        i, j, m = self.D.indices

        self.tree.root.clades[i].branch_length = (self.D[i,j] + self.D[i,m] - self.D[j,m])/2
        self.tree.root.clades[j].branch_length = (self.D[i,j] + self.D[j,m] - self.D[i,m])/2
        self.tree.root.clades[m].branch_length = (self.D[i,m] + self.D[j,m] - self.D[i,j])/2
        
        # Gamma(v,i) = d_ij + dim - djm / 2
