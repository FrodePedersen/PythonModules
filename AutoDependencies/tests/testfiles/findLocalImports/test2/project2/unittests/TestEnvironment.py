import Bio.Phylo
import os
from context import Utility

class RootedNumberedTree():

    def __init__(self):
        self.utility = Utility.Utility()

    def create3LeafedTreeA(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("threeLeafedTreeA.new"), "newick")

    def create3LeafedTreeB(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("threeLeafedTreeB.new"), "newick")

    def createInvalidLabelTreeA(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("invalidLabelTreeA.new"), "newick")

    def createInvalidLabelTreeB(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("invalidLabelTreeB.new"), "newick")

    def createTree1(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("tree1.new"), "newick")

    def createTree2(self):
        return Bio.Phylo.read(self.utility.getFileInTestdata("tree2.new"), "newick")




if __name__ == "__main__":
    rootedNumberedTree().create3LeafedTreeA()
