import unittest
from context import autodependencies

class TestAutodependenciesFindFiles(unittest.TestCase):

    def testNoFiles(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findFilesInFolder("testfiles/findFilesTestFiles/testNoFiles", ".py")
        self.assertEqual(results, [])

    def testOneFile(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findFilesInFolder("testfiles/findFilesTestFiles/testOneFile")
        self.assertEqual(results, ["testfiles/findFilesTestFiles/testOneFile\\oneFile.py"])

    def testTwoFiles(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findFilesInFolder("testfiles/findFilesTestFiles/testTwoFiles", ".py")
        self.assertEqual(results, ['testfiles/findFilesTestFiles/testTwoFiles\\1File.py', 'testfiles/findFilesTestFiles/testTwoFiles\\2File.py'])

    def testTwoFilesInSeperateFolders(self):
        autoD = autodependencies.AutoDependency()
        results = autoD.findFilesInFolder("testfiles/findFilesTestFiles/testTwoFilesInSeperateFolders", ".py")
        self.assertEqual(results, ['testfiles/findFilesTestFiles/testTwoFilesInSeperateFolders\\folder1\\1File.py', 'testfiles/findFilesTestFiles/testTwoFilesInSeperateFolders\\folder2\\2File.py'])


if __name__ == '__main__':
    unittest.main()