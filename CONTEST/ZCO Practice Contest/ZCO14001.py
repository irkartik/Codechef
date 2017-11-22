# cook your dish here
n, h = map(int,input().split())
no_of_boxes = list(map(int, input().split()))
operation = list(map(int, input().split()))
has_box = False

st = 0
for i in operation:
	if i == 1 and st != 0:
		st = st - 1;
	elif i == 2 and st != n-1:
		st = st + 1;
	elif i == 3 and no_of_boxes[st] != 0 and has_box == False:
		no_of_boxes[st] -= 1
		if has_box:
			has_box = False
		else:
			has_box = True
	elif i == 4 and no_of_boxes[st] != h and has_box == True:
		no_of_boxes[st] += 1
		if has_box:
			has_box = False
		else:
			has_box = True
	elif i == 0:
		break

print(*no_of_boxes)