columns = line.split(" ")

attributes = []
values = []
relevanceLabel = columns[0]

for id in columns[2:]:
    attr, data = id.split(":")
    attributes.append(attr)
    values.append(data)

print(attributes)
print(values)