import unittest
from context import autodependencies

class TestAutodependenciesFindDependencies(unittest.TestCase):

    def testFindNoDependenciesOftestFolder1(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findDependencies("testfiles/findDependencies/test1", ".py")
        self.assertEqual(results, set())

    def testFindOneDependenciesOftestFolder2(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findDependencies("testfiles/findDependencies/test2", ".py")
        self.assertEqual(results, set(["random"]))

    def testFindAllDependenciesOffindImportsTestFiles(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findDependencies("testfiles/findImportsTestFiles", ".py")
        self.assertEqual(results, set(["random", "os", "sys", "numpy", "optparse", "Days", "Utility", "unittest"]))


if __name__ == '__main__':
    unittest.main()
