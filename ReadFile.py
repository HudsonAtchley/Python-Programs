Numbers = open("Numbers.txt", "r")
f = Numbers.readlines()

newList = []
for line in f:
    newList.append(line.strip())

print(newList)