import os #allows os utilities
import re #allows regular expressions
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class AutoDependency():

    def __init__(self):
        self.insideMultilineComment = False

    def findDependencies(self, inputPath, fileEnding=""):
        setOfDependencies = set()

        fileNames = self.findFilesInFolder(inputPath, fileEnding)
        imports = []
        for fileName in fileNames:
            file = open(fileName, "r")
            for line in file:
                result = self.findImports(line)
                if result:
                    for r in result:
                        setOfDependencies.add(r)
            file.close()

        return setOfDependencies

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

                stringListUpdated.append(s)
                
                if comment:
                    return stringListUpdated

        return stringListUpdated


if __name__ == '__main__':

    autodependency = AutoDependency()
    autodependency.findFiles()