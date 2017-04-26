import os #allows os utilities
import re #allows regular expressions
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class AutoDependency():

    def __init__(self):
        self.modules = []

    def run(self):
        #loader = unittest.TestLoader()
        print(self.modules)

        # suites_list = []
        # for test_class in self.classes:
        #     suite = loader.loadTestsFromTestCase(test_class)
        #     suites_list.append(suite)

        # big_suite = unittest.TestSuite(suites_list)

        # unittest.TextTestRunner(verbosity=2).run(big_suite)

    def findFiles(self):
        #find all the files ending with a .py extension
        onlyPyfiles = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if (os.path.isfile(os.path.join("", f)) and (re.match("^.*\.py$",f) != None ))]

        #iterate over all the files found
        for f in onlyPyfiles:
            module = importlib.import_module(f[:-3]) #imports the module and returns it.
            self.modules.append(module)

if __name__ == '__main__':
    autodependency = AutoDependency()
    autodependency.findFiles()
    autodependency.run()