def sum1(arr):
	tot = 0
	for i in arr:
		tot = tot + i
	return tot

def prod(arr):
	pro = 1
	for i in arr:
		pro = pro*i
	return pro

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	count = len(a)
	for i in range(len(a)):
		for j in range(len(a)):
			if sum(a[i:j+1]) == prod(a[i:j+1]):
				count = count + 1
	print(count)