l=[5,7,3,5,8,9,4]
for val in range(len(l)-1,0,-1):
    for ind in range(val):
        if l[ind]>l[ind+1]:
            l[ind],l[ind+1]=l[ind+1],l[ind]
print(l[-1])
