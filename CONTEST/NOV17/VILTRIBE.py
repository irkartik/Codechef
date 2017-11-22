t = int(input())
for _ in range(t):
	s = input()
	countA, countB, temp = 0,0,0
	countA = s.count('A')
	countB = s.count('B')
	for i in range(len(s)):
		temp = 0
		if s[i] == 'A':
			for j in range(i+1, len(s)):
				if s[j] == '.':
					temp +=1
				elif s[j] == 'A':
					countA = countA + temp
					break
				else:
					break
		elif s[i] == 'B':
			for j in range(i+1, len(s)):
				if s[j] == '.':
					temp +=1
				elif s[j] == 'B':
					countB = countB + temp
					break
				else:
					break
	print("%s %s"%(countA, countB))