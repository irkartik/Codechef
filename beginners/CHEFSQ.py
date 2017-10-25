for _ in range(int(input())):
    nl=int(input())
    n=list(map(int,input().split()))
    fl=int(input())
    f=list(map(int,input().split()))
    flag=0
    for i in f:
        if i not in n:
            flag=1 
            print("No")
            break
    if flag==0:
        print("Yes") 