# cook your dish here
t = int(input())
for _ in range(t):
	n, p = map(int, input().split())
	a = [None]*p
	for i in range(p):
		if i%2==0:
			a[i] = 'a'
			a[p-i-1] = 'a'
		else:
			a[i] = 'b'
			a[p-i-1] = 'b'
	x = n//p
	ans = a*x
	s = ''.join(ans)
	countA = s.count('a')
	countB = s.count('b')
	if s != s[::-1] or countA ==0 or countB==0:
		print('impossible')
	else:
		print(s) 