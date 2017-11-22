n = int(input())
strength = list(map(int, input().split()))

revenue = 0

for i in range(n):
	for j in range(i, n):
		revenue += abs(strength[i] - strength[j])

print(revenue)