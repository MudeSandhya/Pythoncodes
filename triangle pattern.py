n=int(input())

for i in range(1,n):
    num=1
    for j in range(n,0,-1):
        if(j>i):
            print(" ",end="")
        else:
            print(num,end="")
            num=num+1
    print("\r")
