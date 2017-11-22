t = int(input())
for _ in range(t):
	n, r = map(int, input().split())
	a = list(map(int, input().split()))
	left = min(a)
	right = max(a)
	count = 0
	for i in a:
		if i>=r and i<=right:
			# go left
			right = i
			count +=1
		elif i<=r and i>=left:
			#go right
			left = i
			count +=1
	if count == len(a):
		print('YES')
	else:
		print('NO')

