t = int(input())
for _ in range(t):
	i1 = list(map(str, input().split()))
	i2 = list(map(str, input().split()))
	count = 0
	for i in i1:
		for j in i2:
			if i == j:
				count = count +1
	if count>=2:
		print('similar')
	else:
		print("dissimilar")