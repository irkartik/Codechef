t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	val = a[0] * (n-1)
	print(val)