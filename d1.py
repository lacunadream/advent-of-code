raw = open('data/d1.txt', 'r')
data = raw.read()

# Total Ups
totalUps = data.count('(')
print("Total Ups=%s" %totalUps)

# Total Steps
totalSteps = len(data)
print("Total Steps=%s" %totalSteps)

# Answer lmao
answer = (totalUps * 2) - totalSteps
print("Answer=%s" %answer)

# More proper way of iterating I guess. 
pos = 0
count = 0
for x in data:
	count = count + 1
	if (x == "("): 
		pos = pos + 1
		print("Count %s, %s" %(count, pos))
	else: 
		pos = pos - 1
		print("Count %s, %s" %(count, pos))
		if (pos == -1): 
			break
print(pos)





