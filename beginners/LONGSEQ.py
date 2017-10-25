t = int(input())
for _ in range(t):
	n = list(input())
	onecount = 0
	zerocount = 0
	for i in n:
		if i == '1':
			onecount = onecount + 1
		elif i == '0':
			zerocount = zerocount + 1
	if onecount == 1 or zerocount == 1:
		print('Yes')
	else:
		print('No')
