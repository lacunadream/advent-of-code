data = 18
raw = 20
bar = 1
multiAdd = 0

for i in range (1, raw):
	bar += 1
	print ("initial %s" %i)
	for k in range (1, bar):
		if (i % k == 0):
			multiAdd = multiAdd + k
			print(multiAdd)
			if multiAdd == data:
				print ("***")
				break 
	multiAdd = 0