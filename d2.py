import re
with open('data/d2.txt', 'r') as raw:

	pattern = re.compile(r'\d*')
	# spec = pattern.findall("2x3x4")
	# # a = (test[2])
	# # b = (test[0])
	# # k = int(a) * int(b)
	# # print(k)

	# # Part I
	# totalArea = 0

	# for line in raw: 
	# 	spec = pattern.findall(line)
	# 	# print(line)
	# 	# print(spec)
	# 	a = int(spec[0])
	# 	b = int(spec[2])
	# 	c = int(spec[4])
	# 	first = a*b
	# 	second = b*c
	# 	third = c*a
	# 	add = min(first, second, third)
	# 	# print(add)
	# 	totalArea = totalArea + 2*first + 2*second + 2*third + add
	# 	print("Total area is %s" % totalArea)
	# 	# print(a)
	# 	# print(b)
	# 	# print(c)

	# 	# nice = map(float, spec)  --> doesnt work because 
	# 	# print(nice)
	# 	# print(min(nice))

	# 	# print('lol')
		
	# Part II
	totalRibbon = 0

	for line in raw: 
		spec = pattern.findall(line)
		a = int(spec[0])
		b = int(spec[2])
		c = int(spec[4])
		volume = a*b*c

		first = 2*(a+b)
		second = 2*(b+c)
		third = 2*(a+c)
		perimeter = min(first, second, third)
		totalRibbon = totalRibbon + volume + perimeter
		print(totalRibbon)