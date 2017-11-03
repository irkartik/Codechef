t = int(input())
for _ in range(t):
	n = list(map(int, input().split()))
	n.sort()
	if n[-1] == len(n)-1:
		print(n[-2])
	else:
		print(n[-1])
	