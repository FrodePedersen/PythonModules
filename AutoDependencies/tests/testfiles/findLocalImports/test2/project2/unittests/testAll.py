import unittest #allows unittest framework
import os #allows os utilities
import re #allows regular expressions
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class TestAll():

    def __init__(self):
        self.classes = []

    def runTests(self):
        loader = unittest.TestLoader()
        
        suites_list = []
        for test_class in self.classes:
            suite = loader.loadTestsFromTestCase(test_class)
            suites_list.append(suite)

        big_suite = unittest.TestSuite(suites_list)

        unittest.TextTestRunner(verbosity=2).run(big_suite)

    def findFiles(self):
        #find all the files ending with a .py extension
        onlyPyfiles = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if (os.path.isfile(os.path.join("", f)) and (re.match("^.*\.py$",f) != None ))]

        modules = []
        #iterate over all the files found
        for f in onlyPyfiles:
            modules.append(f[:-3]) #removes the .py extension
           

            module = importlib.import_module(f[:-3]) #imports the module and returns it.
            members = inspect.getmembers(module, inspect.isclass) #get the classes from each module

            for member in members:
                #member is a 2-tuple: (name of the class, type)
                if issubclass(member[1], unittest.TestCase): #if the class is a subclass of unittest.TestCase, then we want to store the class.
                    self.classes.append(member[1])
          

if __name__ == '__main__':
    tester = TestAll()
    tester.findFiles()
    tester.runTests()