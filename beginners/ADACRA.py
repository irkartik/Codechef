t = int(input())
for _ in range(t):
	s = input()
	temp = s[0]
	count=0
	for i in range(len(s)):
		if temp == 'U':
			if s[i] == 'D' and s[i-1]=='U':
				count = count+1
		elif temp == 'D':
			if s[i] == 'U' and s[i-1]=='D':
				count = count+1
	print(count)