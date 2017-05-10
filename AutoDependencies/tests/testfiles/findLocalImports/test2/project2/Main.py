import NJ
import sys
from optparse import OptionParser

def help():

    print
    print "---------------------------------- H E L P --------------------------------------"
    print 
    print "Main.py <Distance Matrix.phy> [targets]"
    print
    print "Targets: "
    print
    print "-o <filename>               outputs the tree in newick format"
    print "-heu                        toggles the heuristic"
    print 
    print "Made by: Marni Tausen, Meinhard Dam, Frode S. N. Pedersen and Moises Coll Macia"
    print



if __name__=="__main__":

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    parser.add_option('-o', type="string", nargs=1, dest="output", help="<filename.phy>")
    parser.add_option('--heu', action="store_true", dest="heuristic", help="Toggle heuristic")
    parser.add_option('-H', action="store_true", dest="help", help="Displays help screen")
    options, args = parser.parse_args()

    if options.help!=None:
        help()
    
    nj = NJ.NJ(sys.argv[1])
    if options.heuristic!=None:
        heuristic = True
    else:
        heuristic = False
    if options.output!=None:
        output = options.output
    else:
        output = "output.newick"
    nj.constructTree(output, heuristic)
