import os #allows os utilities
import re #allows regular expressions
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class AutoDependency():

    def __init__(self):
        pass

    def findFiles(self):
        #find all the files ending with a .py extension
        self.onlyPyfiles = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if (os.path.isfile(os.path.join("", f)) and (re.match("^.*\.py$",f) != None ))]

        module = importlib.import_module("watershed_Alg")
        for m in inspect.getmembers(module, inspect.ismodule):
            print("m: " + str(m[0]))
        #iterate over all the files found
        # for f in self.onlyPyfiles:
        #     module = importlib.import_module(f[:-3]) #imports the module and returns it.
        #     print("module: " + str(module))
        #     for m in inspect.getmembers(module, inspect.ismodule):
        #         print("m: " + str(m[0]))
        #     #self.modules.append(module)

    def findImports(self, inputString):

        #regEx = re.compile('import[\t\w]')
        regEx = re.compile(r'import[\s\t]+[a-zA-Z]+[a-zA-Z0-9]*[\s\t]*')
        # regEx = re.compile(r'((a|b))+')
        # m = re.search(r'\bAlgae\s+([0-9.]+)', s)
        result = regEx.findall(inputString)

        return result


if __name__ == '__main__':

    autodependency = AutoDependency()
    autodependency.findFiles()
    #autodependency.run()
    

    # finder = modulefinder.ModuleFinder(debug=1)
    # finder.run_script("test.py") 
    # finder.report()
    # #print('Loaded modules:')
    # # for name, mod in finder.modules.items():
    # #     print('%s: ' % name, end='')
    # #     #print(','.join(list(mod.globalnames.keys())[:3]))

    # # print('-'*50)
    # # print('Modules not imported:')
    # # print('\n'.join(finder.badmodules.keys()))


