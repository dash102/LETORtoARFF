# Creators: Stephanie Fu & Luann Jung
# 10 September 2017
import sys

def joinComments(line):
    columns = line.split(" ")
    for el in range(len(columns)):
      if columns[el][0] == '#':
        comment = " ".join(columns[el:])
        for i in range(len(columns) - el): columns.pop()
        return columns, comment

def readFile(fileName):
    lineNumber = 1
    with open(fileName) as fp:
      for line in fp:
        processLine(fileName, line, lineNumber)
        lineNumber+=1

def processLine(readFileName, line, lineNumber):
    columns, comment = joinComments(line)
    writeFile(readFileName, columns, comment, lineNumber)

def getAttributes(columns):
    attributes = []
    for a in columns[2:]:
      attr = a.split(":")[0]
      attributes.append(attr)
    return attributes

def getData(columns):
    values = []
    relevanceLabel = columns[0]
    for a in columns[2:]:
      data = a.split(":")[1]
      values.append(data)
    return values, relevanceLabel

def processLabels(columns):
    relevanceArr = ["NONE", "LOW", "HIGH"]
    relevanceLabel = getData(columns)[1]
    return relevanceArr[int(relevanceLabel)]

def writeFile(readFileName, columns, comments, lineNumber):
    root = readFileName[:len(readFileName)-4]
    writeFileName = root + "-new.arff"
    if lineNumber == 1:
        with open(writeFileName, "w+"): pass
    with open(writeFileName, "a+") as f:
      if lineNumber == 1:
        f.write("@RELATION " + root + "\n\n")
        for piece in getAttributes(columns):
          f.write("@ATTRIBUTE " + piece + "\t REAL\n")
        f.write("@ATTRIBUTE class     {NONE,LOW,HIGH}")
        f.write("\n\n@DATA\n")

      f.write(",".join(getData(columns)[0]))
      f.write("," + processLabels(columns))
      f.write("\t%" + comments[1:])

readFile(sys.argv[1])