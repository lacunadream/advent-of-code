import collections

raw = open('data/d3.txt', 'r')
data = raw.read()

position = [0,0]  #x, y 
# position[0] = position[0] + 2
# print(position[0])
gah = ([])

for move in ("^>v<"): 
	print(position)
	gah.append(position)
	print(gah)
	if (move==">"):
		position[0] = position[0] + 1
	elif (move =="<"):
		position[0] = position[0] - 1
	elif (move =="^"): 
		position[1] = position[1] + 1
	elif (move =="v"): 
		position[1] = position[1] - 1
	
set([x for x in gah if gah.count(x) > 1])