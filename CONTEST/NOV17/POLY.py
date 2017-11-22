def calculate(a, t):
	b = a[::-1]
	result = b[0]
	for i in range(1, 4):
		result = result*t + b[i]
	return result
 
t = int(input())
for _ in range(t):
	n = int(input())
	a = [[0 for x in range(4)] for y in range(n)]
	for i in range(n):
		a[i][0], a[i][1], a[i][2], a[i][3]  = map(int, input().split())
	q = int(input())
	t = [0 for x in range(q)]
	for j in range(q):
		t[j] = int(input())
	mini = list()
	for i in range(q):
		val = list()
		for j in range(n):
			ans = calculate(a[j], t[i])
			val.append(ans)
		val.sort()
		mini.append(int(val[0]))
	for k in mini:
		print(k)