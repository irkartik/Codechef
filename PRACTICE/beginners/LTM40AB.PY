t = int(input())
for _ in range(t):
	a, b, c, d = map(int, input().split())
	count = 0
	for i in range(a, b+1):
		for j in range(c, d+1):
			if i<j:
				count = count +1
	print(count)
