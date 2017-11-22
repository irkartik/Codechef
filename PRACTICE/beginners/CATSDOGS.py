t = int(input())
for _ in range(t):
	c, d, l = map(int, input().split())
	maxi = (c+d)*4
	mini = max(4*d, 4*(c-d))
	if l<=maxi and l>=mini and l%4 == 0:
		print('yes')
	else:
		print('no')