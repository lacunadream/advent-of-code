data = open('data/d8.txt', 'r')
totalCount = 0
for line in data:
	totalCount = totalCount + len(line)

print(totalCount)

a = "asdss"
print(a.find("s"))