
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
  if lineNumber == 1: getAttributes(columns)
  #getData(columns)
  writeFile("newTest.txt", columns, comment)

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

def writeFile(fileName, columns, comments):
  with open(fileName, "a") as f:
    f.write(",".join(getData(columns)[0]))
    f.write("," + getData(columns)[1])
    f.write("   %" + comments[1:])
    #f.write("\n")

readFile("test.txt")