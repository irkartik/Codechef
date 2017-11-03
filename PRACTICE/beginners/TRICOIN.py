t = int(input())
for _ in range(t):
	n = int(input())
	sum = 0
	h = 1
	while(sum <= n):
		sum = sum + h
		h = h + 1
	print(h-2)
