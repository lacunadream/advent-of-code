import re
raw = open('data/d2.txt', 'r')

pattern = re.compile(r'\d*')
# spec = pattern.findall("2x3x4")
# # a = (test[2])
# # b = (test[0])
# # k = int(a) * int(b)
# # print(k)

totalArea = 0

for line in raw: 
	spec = pattern.findall(line)
	# print(line)
	# print(spec)
	a = int(spec[0])
	b = int(spec[2])
	c = int(spec[4])
	first = a*b
	second = b*c
	third = c*a
	add = min(first, second, third)
	# print(add)
	totalArea = totalArea + 2*first + 2*second + 2*third + add
	print("Total area is %s" % totalArea)
	# print(a)
	# print(b)
	# print(c)

	# nice = map(float, spec)
	# print(nice)
	# print(min(nice))

	# print('lol')
	
