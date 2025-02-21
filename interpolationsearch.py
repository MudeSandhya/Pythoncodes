l=[3,4,5,6,7]
target=6
low=0
high=len(l)-1
while low<=high and l[low]<=target<=l[high]:
    ind=int(low+((high-low)/(l[high]-l[low]))*(target-l[low]))
    if l[ind]<target:
        low=ind+1
    elif l[ind]>target:
        high=ind-1
    elif l[ind]==target:
        print(ind)
        break
else:
    print(-1)
#function
def inter(l,low,high,target):
    while low<=high and l[low]<=target<=l[high]:
        ind=int(low+((high-low)/(l[high]-l[low]))*(target-l[low]))
        if l[ind]<target:
            low=ind+1
        elif l[ind]>target:
            high=ind-1
        elif l[ind]==target:
            return ind
    return -1
l=[4,5,6,7,8]
target=8
print(inter(l,0,len(l)-1,target))
#recursion
def interp(l,low,high,target):
    while low<=high and l[low]<=target<=l[high]:
        ind=int(low+((high-low)/(l[high]-l[low]))*(target-l[low]))
        if l[ind]<target:
            return interp(l,ind+1,high,target)
        elif l[ind]>target:
            return interp(l,low,ind-1,target)
        elif l[ind]==target:
            return ind
    else:
        return -1
l=[1,2,3,4,5,67,8,99]
target=9
print(interp(l,0,len(l)-1,target))
#highest val finding by bubble sort
l=[4,5,6,7,8]
for val in range(len(l)-1,len(l)-2):
    for val2 in range(val):
        if l[val2]>l[val2+1]:
            l[val2],l[val2+1]=l[val2+1],l[val2]
print(l[-1])
#getting highest value in an list
l=[2,5,66,4,7,9]
high=l[0]
for val in range(1,len(l)):
    if high<l[val]:
        high=l[val]
print(high)
#getting least value
l=[9,8,5,7,9,2,3,1]
least=l[0]
for val in range(1,len(l)):
    if least>l[val]:
        least=l[val]
print(least)
    
            
