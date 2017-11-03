t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	minus, one, misc, zero= 0,0,0,0
	for i in a:
		if i==0:
			zero+=1
		elif i==-1:
			minus +=1
		elif i==1:
			one+=1
		else:
			misc+=1
	if (minus>0 and misc>0) or (minus>1 and one<1) or misc>1:
		print('no')
	else:
		print('yes')