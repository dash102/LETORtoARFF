
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
      processLine(line, lineNumber)
      lineNumber+=1

def processLine(line, lineNumber):
  columns, comment = joinComments(line)
  writeFile("newTest.txt", columns, comment, lineNumber)

def getAttributes(columns):
  attributes = []
  for id in columns[2:]:
    attr = id.split(":")[0]
    attributes.append(attr)
  return attributes

def getData(columns):
  values = []
  relevanceLabel = columns[0]
  for id in columns[2:]:
    data = id.split(":")[1]
    values.append(data)
  return values, relevanceLabel

def processLabels(columns):
    useless, relevanceLabel = getData(columns)
    if relevanceLabel=="0":
        relevanceLabel= "NONE"
    elif relevanceLabel=="1":
        relevanceLabel= "LOW"
    elif relevanceLabel=="2":
        relevanceLabel = "HIGH"
    return relevanceLabel

def writeFile(fileName, columns, comments, lineNumber):
  with open(fileName, "a") as f:
      if lineNumber==1:
          for piece in getAttributes(columns):
              f.write("@ATTRIBUTE " + piece + "\t REAL\n")
          f.write("@ATTRIBUTE class     {NONE,LOW,HIGH}")
          f.write("\n\n")

      f.write(",".join(getData(columns)[0]))
      f.write("," + processLabels(columns))
      f.write("\t%" + comments[1:])

readFile("test.txt")