import unittest
from context import autodependencies

class TestAutodependenciesFindExternalDependencies(unittest.TestCase):

    def testFindNoDependenciesInTestFolder1(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findBuiltinImports/test1", ".py")
        allDependencies = autoD.findDependencies(files)
        results = autoD.findBuiltinImports(allDependencies)
        self.assertEqual(results, set())

    def testFindOneDependenciesInTestFolder2(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findBuiltinImports/test2", ".py")
        allDependencies = autoD.findDependencies(files)
        results = autoD.findBuiltinImports(allDependencies)
        self.assertEqual(results, set(["sys"]))

    def testFindTwoDependenciesInTestFolder2(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findBuiltinImports/test3", ".py")
        allDependencies = autoD.findDependencies(files)
        results = autoD.findBuiltinImports(allDependencies)
        self.assertEqual(results, set(["sys", "math"]))

if __name__ == '__main__':
    unittest.main()
