def prefixSum(i, a):
	s = 0
	for c in range(i+1):
		s += a[c]
	return s

def suffixSum(i, a):
	s = 0
	n = len(a)
	for c in range(i, n):
		s += a[c]
	return s

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	tot = prefixSum(0, a) + suffixSum(0,a)
	cou = 1
	for i in range(len(a)):
		if suffixSum(i,a)+prefixSum(i,a)<tot:
			tot = suffixSum(i,a)+ prefixSum(i,a)
			cou = i+1
	print(cou)