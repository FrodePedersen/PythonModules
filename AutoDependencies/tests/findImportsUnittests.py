import unittest
from context import autodependencies

class TestAutodependenciesFindImports(unittest.TestCase):

    def testReadFileWithoutImports(self):
        testFile = open('testfiles/findImportsTestFiles/testWithOutImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [])

    def testReadFileWithTwoImports(self):
        testFile = open('testfiles/findImportsTestFiles/testWithTwoImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [['sys'], ['random']])

    def testReadFileWithTwoCommaImports(self):
        testFile = open('testfiles/findImportsTestFiles/testWithTwoCommaSeperatedImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [['sys', 'random']])

    def testReadFileWithFiveCommaImports(self):
        testFile = open('testfiles/findImportsTestFiles/testWith5CommaSeperatedImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['sys','random','numpy','skyfield','gps']])

    def testReadFileWithOneFromImport(self):
        testFile = open('testfiles/findImportsTestFiles/testWithOneFromImport.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['numpy']])

    def testReadMainpyFile(self):
        testFile = open('testfiles/findImportsTestFiles/testMain.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['sys'], ['optparse'], ['Days'], ['Utility']])

    def testReadImportWithinFunctionFile(self):
        testFile = open('testfiles/findImportsTestFiles/testImportsWithinFunction.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testReadFromImportWithinFunctionFile(self):
        testFile = open('testfiles/findImportsTestFiles/testFromImportWithinFunction.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testMultipleImportsOneLine(self):
        testFile = open('testfiles/findImportsTestFiles/testMultipleImportsOneLine.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random', 'numpy']])

    def testMultipleImportsOneLinex5(self):
        testFile = open('testfiles/findImportsTestFiles/testMultipleImportsOneLinex5.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random', 'numpy', 'os', 'unittest', 'sys']])

    def testWithCommentedImport(self):
        testFile = open('testfiles/findImportsTestFiles/testWithCommentedImport.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [])

    def testWithCommentedImport2(self):
        testFile = open('testfiles/findImportsTestFiles/testWithCommentedImport2.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [])

    def testWithPrintBeforeImport(self):
        testFile = open('testfiles/findImportsTestFiles/testWithPrintBeforeImport.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testImportInsideMultilineComment(self):
        testFile = open('testfiles/findImportsTestFiles/testImportInsideMultilineComment.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testCommentAfterImport(self):
        testFile = open('testfiles/findImportsTestFiles/testCommentAfterImport.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

if __name__ == '__main__':
    unittest.main()