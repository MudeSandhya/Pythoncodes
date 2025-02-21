"""num=3
for row in range(1,num+1):
    for space in range(num-row):
        print(" ",end="")
    for value in range(row*2-1):
        print("*",end="")
    print()

num=4
for row in range(num):
    for col in range(num):
        print("*",end="")
    print()
num=4
for row in range(1,num+1):
    for space in range(row):
        print(" ",end="")
    for col in range(2*row-1,0,-1):
        print("*",end="")
    print()"""
num=4
for row in range(num+1):
    for col in range(row):
        print("*",end="")
    print()
