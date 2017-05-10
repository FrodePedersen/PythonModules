import unittest
import TestEnvironment
import numpy as np
import Bio.Phylo
from context import Utility
from context import Matrix
from context import NJ

class testMatrix(unittest.TestCase):

    def setUp(self):
        self.utility = Utility.Utility()
        self.testData = self.utility.getFileInTestdata("example_slide4.phy")
        self.D = Matrix.Matrix(self.testData)

    def testConstruction(self):
        D = Matrix.Matrix(self.testData)
        self.assertEqual(str(D), str(self.D))

    def testTraversal(self):
        D = Matrix.Matrix(self.testData)
        AllEqual = True
        for values in D:
            i, j, v = values
            if D[i,j]!=v:
                AllEqual = False
        self.assertEqual(AllEqual, True)
        
    def testSymmetry(self):
        D = Matrix.Matrix(self.testData)
        AllEqual = True
        for values in D:
            i, j, v = values
            if D[j,i]!=v:
                AllEqual = False
        self.assertEqual(AllEqual, True)

    # Testing whether the index is removed
    def testDeletion1(self):
        from random import randint
        D = Matrix.Matrix(self.testData)
        indices = D.indices
        D.removeIndex(randint(0,len(indices)))
        self.assertEqual(len(indices)-1, len(D.indices))

    # Testing whether the traversal still holds
    def testDeletion2(self):
        from random import randint
        D = Matrix.Matrix(self.testData)
        D.removeIndex(randint(0,len(D.indices)))
        AllEqual = True
        for values in D:
            i, j, v = values
            if D[i,j]!=v:
                AllEqual = False
        self.assertEqual(AllEqual, True)

    # Testing whether the symmetry still holds
    def testDeletion3(self):
        from random import randint
        D = Matrix.Matrix(self.testData)
        D.removeIndex(randint(0,len(D.indices)))
        AllEqual = True
        for values in D:
            i, j, v = values
            if D[j,i]!=v:
                AllEqual = False
        self.assertEqual(AllEqual, True)

class testTreeBuilding(unittest.TestCase):

    def setUp(self):
        self.utility = Utility.Utility()
        self.testData = self.utility.getFileInTestdata("example_slide4.phy")
        self.NJ = NJ.NJ(self.testData)


    def test1(self):
        i, j = self.NJ.FindQmin()
        
        self.NJ.updateTree(i, j)

        print self.NJ.tree

        Bio.Phylo.NewickIO.write(self.NJ.tree, "test.new")

       # Bio.Phylo.draw_ascii(self.NJ.tree)