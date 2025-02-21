'''l=[44,55,66,88]
dup=l.copy()
print(dup is l)
print(id(dup[0]))'''
#greast value
'''a,b,c,d=2,3,10,5
if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
else:
    if b>c:
        if b>d:
            print(b)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)

if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)
num=20
count=0
for val in range(1,num+1):
    if num%val==0:
        print(val)
        count+=1
        print(bin(val))
        print(int(bin(val),2))

#prinme or not
num=7
fact=0
for val in range(1,num+1):
    if num%val==0:
        fact+=1
if fact==2:
    print("prime")
else:
    print("not an prime")
row,col=4,4
for row1 in range(1,row+1):
    for star in range(4):
        print("*",end="")
    print(" ")
row=4
for row in range(1,row+1):
    for space in range(row):
        print("*",end="")
    print("")'''

num=7
for row in range(0,num):
    for col in range(num):
        if  row+col==num//2 or row-col==num//2 or col-row==num//2 or row+col==num+2:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

