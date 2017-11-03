def prefixSum(a, i):
	sum = 0
	for j in range(i):
		sum += a[j]
	return sum

def suffixSum(a, n, i):
	sum = 0
	start = n - i + 1
	while(start<n):
		sum = sum + a[start]
		start = start + 1
	return sum

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))

	total = 0
	for i in range(n):
		total = total + a[i]

	temp = total
	for i in range(n):
		pre = prefixSum(a, i)
		suff = suffixSum(a, n, i)
		if (pre+suff<temp):
			index = i

	print(index)

