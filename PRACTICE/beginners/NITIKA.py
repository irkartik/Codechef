t = int(input())
for _ in range(t):
	name = input().lower().title().split()
	j = list()
	for i in name:
		j.append(i[0])
	fname = str()
	for i in range(len(j)-1):
		fname = fname + j[i] +'. '
	fname = fname + name[-1]
	print(fname)