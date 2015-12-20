data = 3400000
bar = 1
multiAdd = 0
flag = 0

for i in range (1, data):
	bar += 1
	print ("initial %s" %i)
	for k in range (1, bar):
		if (i % k == 0):
			multiAdd = multiAdd + k
			print(multiAdd)
			if multiAdd == data:
				print ("***")
				flag = 1
				break 
	if (flag == 1):
		print ("Answer is %s" %i)
		break  
	multiAdd = 0