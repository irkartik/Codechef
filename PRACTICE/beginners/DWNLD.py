t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	c = 0
	for i in range(n):
		t, d = map(int, input().split())
		if k>0:
			k = k - t
			if k<0:
				c = c + abs(k)*d
				k = 0
		else:
			c = c+t*d

	print(c)
