import math
t = int(input())
for _ in range(t):
	n, v1, v2 = map(int, input().split())
	# v1 chef velocity
	# v2 elevator velocity
	t1 = (math.sqrt(2)*n)/v1
	t2 = (2*n)/v2
	if t1>=t2:
		print('Elevator')
	else:
		print('Stairs')