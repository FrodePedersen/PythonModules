import sys
from optparse import OptionParser

import Days
import Utility

class Main():

    #Constructor
    def __init__(self, alg):
        self.alg = alg
        self.utility = Utility.Utility()
        self.consoleInputDic = {}

    #method that starts the entire program
    def start(self):
        print self.consoleInput()
        treeALoc = self.consoleInputDic['-d'][0]
        treeBLoc = self.consoleInputDic['-d'][1]

        treeA = self.utility.readTree(treeALoc)
        treeB = self.utility.readTree(treeBLoc)

        distance = self.alg.calculateDistance(treeA, treeB)

        print "The distance between the two trees is: " + str(distance)

    def consoleInput(self):
        usage = "usage: %prog [options] arg"
        parser = OptionParser(usage)

        #Assigning cmd arguments
        parser.add_option('-d', type="string", nargs=2, dest="days", help="<treeFileName> <treeFileName>")
        parser.add_option('-H', action="store_true", dest="help", help="Displays proper help")
        (options, args) = parser.parse_args()

        print str(options.days)
        self.consoleInputDic['-d'] = options.days


if __name__ == "__main__":
    #change to be console specified
    m = Main(Days.Days())
    m.consoleInput()
    m.start()
