t = int(input())
for _ in range(t):
	n = int(input())
	prod = 1
	for i in range(1,n+1):
		prod = prod * i
	print(prod)