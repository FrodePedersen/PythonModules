import unittest
from context import autodependencies

class TestAutodependencies(unittest.TestCase):

    def setUp(self):
        self.x = "what"

    def testNoImport(self):
        testString = """hello world
                        this is a multiline String, but without any i mports
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, [])

    def testNoImport2(self):
        testString = """hello world
                        this is a multiline String, but without any simports
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, [])

    def testOneImport(self):
        testString = """hello world
                        this is a multiline String, but WITH one import, namely:
                        importsys
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, [])

    def testOneImport2(self):
        testString = """hello world
                        this is a multiline String, but WITH one import, namely:
                        import sys
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, ['import sys'])


    def testOneImportWithManySpaces(self):
        testString = """hello world
                        this is a multiline String, but WITH one import, namely:
                        import                      sys
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, ['import                      sys'])

    def testTwoImport(self):
        testString = """hello world
                        this is a multiline String, but WITH one import, namely:
                        import sys
                        import random
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, ['import sys', 'import random'])

    def testTwoImportCommaSeperated(self):
        testString = """hello world
                        this is a multiline String, but WITH two import, namely:
                        import sys, random
                        """
        autoD = autodependencies.AutoDependency()
        result = autoD.findImports(testString)
        self.assertEqual(result, ['import sys, random'])

# class test(unittest.TestCase):
    
#     def test(self):
#         testString = "aabb"
#         autoD = autodependencies.AutoDependency()
#         result = autoD.findImports(testString)
#         self.assertEqual(result, ['aabb'])

if __name__ == '__main__':
    unittest.main()