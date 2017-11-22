t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a.sort()
	b.sort()
	count = 0
	i, j = 0, 0
	while i<len(a) and j < len(b):
		if a[i] ==  b[j]:
			count = count + 1
			i += 1
			j += 1
		elif a[i] < b[j]:
			i +=1
		else:
			j+=1
	print(count)