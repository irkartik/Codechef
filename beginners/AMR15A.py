n = int(input())
even = 0
odd = 0
weapon = list(map(int, input().split()))
for i in weapon:
	if i%2 == 0:
		even = even +1 
	else: 
		odd = odd +1
if even>odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")