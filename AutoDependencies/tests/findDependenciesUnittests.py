import unittest
from context import autodependencies

class TestAutodependenciesFindDependencies(unittest.TestCase):

    def testFindNoDependenciesOftestFolder1(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findDependencies/test1", ".py")
        results = autoD.findDependencies(files)
        self.assertEqual(results, set())

    def testFindOneDependenciesOftestFolder2(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findDependencies/test2", ".py")
        results = autoD.findDependencies(files)
        self.assertEqual(results, set(["random"]))

    def testFindAllDependenciesOffindImportsTestFiles(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findImportsTestFiles", ".py")
        results = autoD.findDependencies(files)
        self.assertEqual(results, set(["random", "os", "sys", "numpy", "optparse", "Days", "Utility", "unittest"]))


if __name__ == '__main__':
    unittest.main()
