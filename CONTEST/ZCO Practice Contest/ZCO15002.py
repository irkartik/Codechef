n, k = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(n):
	for j in range(i, n):
		ab = abs(lst[i] - lst[j])
		if ab>=k:
			count+=1

print(count)
