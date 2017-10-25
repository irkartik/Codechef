t = int(input())
for _ in range(t):
	code = input().upper()
	codelist = list(code)
	flag = True
	for i in range(len(codelist)):
		if code[i] == code[i-2]:
			flag = True
		elif code[i] == code[i-2] and code[i] == code[i-1]: 
			flag = False
	if flag == True:
		print('YES')
	else: 
		print('NO')