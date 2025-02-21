def quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1:] if val<pivot]
    right=[val for val in L[1:] if val>=pivot]
    return quick(left) + [pivot] + quick(right)
L=[3,5,4,6,2,1,6,9,77,33.44,79]
print(quick(L))
