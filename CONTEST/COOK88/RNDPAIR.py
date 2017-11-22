t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))

	count = 0
	max_count = 0
	maxi = 0
	for i in range(n):
		for j in range(i):
			if (a[i]+a[j])> maxi:
				maxi = a[i]+a[j]

	for i in range(n):
		for j in range(i):
			max_count +=1
			if (a[i]+a[j])==maxi:
				count+=1


	probability = count/max_count
	print("%.8f" % probability)