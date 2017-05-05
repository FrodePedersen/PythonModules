import unittest
from context import autodependencies

class TestAutodependencies(unittest.TestCase):

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

    def testReadFileWithTwoImports(self):
        testFile = open('testfiles/testWithTwoImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [['sys'], ['random']])

    def testReadFileWithTwoCommaImports(self):
        testFile = open('testfiles/testWithTwoCommaSeperatedImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)
        testFile.close()
        self.assertEqual(results, [['sys', 'random']])

    def testReadFileWithFiveCommaImports(self):
        testFile = open('testfiles/testWith5CommaSeperatedImports.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['sys','random','numpy','skyfield','gps']])

    def testReadFileWithOneFromImport(self):
        testFile = open('testfiles/testWithOneFromImport.txt', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['numpy']])

    def testReadMainpyFile(self):
        testFile = open('testfiles/testMain.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['sys'], ['optparse'], ['Days'], ['Utility']])

    def testReadImportWithinFunctionFile(self):
        testFile = open('testfiles/testImportsWithinFunction.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testReadFromImportWithinFunctionFile(self):
        testFile = open('testfiles/testFromImportWithinFunction.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testMultipleImportsOneLine(self):
        testFile = open('testfiles/testMultipleImportsOneLine.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random', 'numpy']])

    def testMultipleImportsOneLinex5(self):
        testFile = open('testfiles/testMultipleImportsOneLinex5.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random', 'numpy', 'os', 'unittest', 'sys']])

    def testWithCommentedImport(self):
        testFile = open('testfiles/testWithCommentedImport.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [])

    def testWithCommentedImport2(self):
        testFile = open('testfiles/testWithCommentedImport2.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [])

    def testWithPrintBeforeImport(self):
        testFile = open('testfiles/testWithPrintBeforeImport.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])

    def testImportInsideMultilineComment(self):
        testFile = open('testfiles/testImportInsideMultilineComment.py', 'r')
        autoD = autodependencies.AutoDependency()
        results = []
        for line in testFile:
            result = autoD.findImports(line)
            if result:
                results.append(result)

        testFile.close()
        self.assertEqual(results, [['random']])


    

# class test(unittest.TestCase):
    
#     def test(self):
#         testString = "aabb"
#         autoD = autodependencies.AutoDependency()
#         result = autoD.findImports(testString)
#         self.assertEqual(result, ['aabb'])

if __name__ == '__main__':
    unittest.main()