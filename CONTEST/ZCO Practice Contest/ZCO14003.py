n = int(input())
customers = []
revenue = 0
for i in range(n):
	customers.append(int(input()))
customers.sort()
for i in range(n):
	temp = customers[i]*(n-i)
	if temp > revenue:
		revenue = temp

print(revenue)