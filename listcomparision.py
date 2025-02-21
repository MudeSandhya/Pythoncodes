l="hello "
print([l[si:ei] for si in range(len(l)) for ei in range(si+1,len(l)+1) if len(l[si:ei])%2==0])
print("-"*79)
print([val**2 for val in range(20,31) if val%2==0])
print("-"*79)
#if even no print square else odd print sqaure root
print([val**2 if val%2==0 else val**0.5 for val in range(30,40)])
print("-"*79)
#pattern
num=5
print('\n'.join(["*"*5 if val%2==0 else "*"*3 for val in range(num)]))
print("-"*79)
#adding of two list
L1=[1,2,3,4]
L2=[1,2,4,5]
print([ L1[ele]+L2[ele] for ele in range(len(L1))])
print("-"*79)
L1=[2,4,5,6]
L2=[3,4,5,67,55,77,88]
if len(L1)>len(L2):
    for ele in range(len(L2)):
        L2[ele]=L1[ele]+L2[ele]
    print(L2)
else:
    for ele in range(len(L1)):
        L1[ele]=L1[ele]+L2[ele]
    print(L1)
