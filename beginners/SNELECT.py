t = int(input())
for _ in range(t):
	s = list(input())

	snakes = 0
	mongooses = 0
	snakes = s.count('s')
	mongooses = s.count('m')
	
	c=len(s)
	for j in range(c-1):
		if((s[j]=='s' and s[j+1]=='m') or (s[j]=='m' and s[j+1]=='s')):
			s[j]='0'
			s[j+1]='0'
			snakes-=1
	
	print(mongooses)
	print(snakes)
	if snakes > mongooses:
		print('snakes')
	elif mongooses>snakes:
		print('mongooses')
	else:
		print('tie')