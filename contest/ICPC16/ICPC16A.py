t = int(input())
for _ in range(t):
	x1,y1,x2,y2 = map(int, input().split())
	if x1==x2:
		if y1>y2:
			print('down')
		else:
			print('up')
	elif y1==y2:
		if x1>x2:
			print('left')
		else:
			print('right')
	else:
		print('sad')