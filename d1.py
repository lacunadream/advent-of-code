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




