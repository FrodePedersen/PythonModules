import os #allows os utilities
import re #allows regular expressions
import importlib #allows dynamical imports of modules
import inspect #allows inspection of modules

class AutoDependency():

    def __init__(self):
        self.insideMultilineComment = False

    def findFilesInFolder(self):
        #find all the files ending with a .py extension
        onlyPyfiles = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if (os.path.isfile(os.path.join("", f)) and (re.match("^.*\.py$",f) != None ))]
        print(onlyPyfiles)

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