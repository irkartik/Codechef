t = int(input())
d = {1: 'LB', 2: 'MB', 3: 'UB', 4: 'LB', 5: 'MB', 6: 'UB', 7: 'SL', 8: 'SU'}
for i in range(t):
    s = int(input())
    n = s % 8
    if n == 0:
        print(s - 1, d[7], sep = '')
    elif n <= 3:
        print(s + 3, d[n + 3], sep = '')
    elif n <= 6:
        print (s - 3, d[n - 3], sep = '')
    elif n == 7:
        print(s + 1, d[8], sep = '')