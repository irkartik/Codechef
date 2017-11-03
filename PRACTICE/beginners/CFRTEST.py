t = int(input())
for _ in range(t):
	n = int(input())
	nlist = list(map(int, input().split()))
	total = len(nlist)
	saved = len(set(nlist))
	print(saved)