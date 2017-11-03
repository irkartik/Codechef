t = int(input())
for _ in range(t):
	a, b, n = map(int, input().split())
	if n%2==0:
		print(int(max(a,b)/min(a,b)))
	else:
		x = a*2
		print(int(max(x,b)/min(x,b)))
