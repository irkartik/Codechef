t = int(input())
for _ in range(t):
	n, p = map(int, input().split())
	a = list(map(int, input().split()))
	cakewalk, hard = 0, 0
	cakep = p//2
	hardp = p//10
	for i in a:
		if i >= cakep:
			cakewalk +=1
		elif i <= hardp:
			hard +=1
	if cakewalk == 1 and hard ==2:
		print('yes')
	else:
		print('no')