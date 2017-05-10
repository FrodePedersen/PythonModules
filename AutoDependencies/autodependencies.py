import os #allows os utilities
import re #allows regular expressions
import sys
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class AutoDependency():

    def __init__(self):
        self.insideMultilineComment = False

    def findDependencies(self, files):
        setOfDependencies = set()
        imports = []
        for fileName in files:
            file = open(fileName, "r")
            for line in file:
                result = self.findImports(line)
                if result:
                    for r in result:
                        setOfDependencies.add(r)
            file.close()

        return setOfDependencies

    def findExternalImports(self):
        pass

    def findLocalImports(self, filePaths, setOfDependencies):
        fileNames = set()
        for path in filePaths:
            fileNames.add(os.path.basename(path).split(".")[0])
        return setOfDependencies.intersection(set(fileNames))

    def findBuiltinImports(self, setOfDependencies):
        builtinImports = set()
        for module in setOfDependencies:
            if module in sys.builtin_module_names:
                builtinImports.add(module)

        return builtinImports

    def findFilesInFolder(self, inputPath, fileEnding=""):
        #find all the files ending with a fileEnding extension
        files = []
        results = []
        for(dirpath, dirnames, filenames) in os.walk(inputPath):
            for file in filenames:
                files.append(os.path.join(dirpath, file))
        

        for file in files:
            if file.endswith(fileEnding):
                results.append(file)

        return results

    def findImports(self, inputString):

        strippedInputString = inputString.strip()
        stringList = []
        stringListUpdated = []
        splitStrippedList = []
        splitStringList = strippedInputString.split(";") #incase they write imports like: import sys; import random


        for s in splitStringList:
            splitStrippedList.append(s.strip())         #Strip each of the strings seperated by ;

        for s in splitStrippedList:
            if(s.startswith("'''")):
                self.insideMultilineComment = not self.insideMultilineComment
            if(self.insideMultilineComment):
                return []    
            if(not (s.startswith("from") or s.startswith("import"))):
                continue
            stringList = s.split(",")                   #Split incase import sys, optparse, etc..

            for s in stringList:
                s = s.strip()
                
                comment = False
                if "#" in s:
                    comment = True

                if s.startswith('from'):
                    s = s.split(" ")
                    s = s[1]
                else:
                    s = s.replace("import", "")
                    s = s.strip()
                    s = s.split(" ")[0]

                s = s.split(".")[0]
                stringListUpdated.append(s)
                
                if comment:
                    return stringListUpdated

        return stringListUpdated


if __name__ == '__main__':

    autodependency = AutoDependency()
    print(autodependency.findDependencies("tests", ".py"))