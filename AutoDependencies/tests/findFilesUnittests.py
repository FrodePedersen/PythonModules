import unittest
from context import autodependencies

class TestAutodependenciesFindImports(unittest.TestCase):

    def setUp(self):
        self.x = "what"

    def testReadFileWithoutImports(self):
        testFile = open('testfiles/testWithOutImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [])