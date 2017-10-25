t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	limak, bob=0,0
	i = 1
	while(limak<=a and bob<=b):
		limak = limak + i
		bob = bob + i + 1
		i = i + 2
	if limak>a:
		print("Bob")
	else:
		print('Limak')
