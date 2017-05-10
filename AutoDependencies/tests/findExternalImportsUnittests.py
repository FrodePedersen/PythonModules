import unittest
from context import autodependencies

class TestAutodependenciesFindExternalDependencies(unittest.TestCase):

    def testNoExternalImports(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findExternalImports/test1", ".py")
        results = autoD.findExternalImports(files)
        self.assertEqual(results, set())

    def testOneExternalImports(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findExternalImports/test2", ".py")
        results = autoD.findExternalImports(files)
        self.assertEqual(results, set(["numpy"]))

    def testTwoExternalImports(self):
        autoD = autodependencies.AutoDependency()
        files = autoD.findFilesInFolder("testfiles/findExternalImports/test3", ".py")
        results = autoD.findExternalImports(files)
        self.assertEqual(results, set(["random", "numpy"]))

if __name__ == '__main__':
    unittest.main()
