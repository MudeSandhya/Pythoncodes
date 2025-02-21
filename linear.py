#recursion foe linear search
def linear(L,target,ind):
    if ind==len(L):
        return -1
    if L[ind]==target:
        return ind
    return linear(L,target,ind+1)
L=[1,33,55,77,99]
target=420
print(linear(L,target,0))
#function
def linear(L,target):
    for val in range(len(L)):
        if L[val]==target:
            return val
    return -1
L=[22,33,55,77]
print(linear(L,77))

