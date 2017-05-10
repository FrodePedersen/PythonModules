import unittest
from context import autodependencies

class TestAutodependenciesFindExternalDependencies(unittest.TestCase):

    def testFindOneDependenciesOftestFolder1(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findLocalImports/test1", ".py")
        allDependencies = autoD.findDependencies(files)
        results = autoD.findLocalImports(files, allDependencies)
        self.assertEqual(results, set(["findNone"]))

    def testFindAllLocalModulesInTestFiles(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findLocalImports/test2", ".py")
        allDependencies = autoD.findDependencies(files)
        results = autoD.findLocalImports(files, allDependencies)
        self.assertEqual(results, set(["Utility", "context", "NJ", "TestEnvironment", "Matrix"]))

if __name__ == '__main__':
    unittest.main()
