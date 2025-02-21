#add of a even posi tion in list
l=[44,5,66,77,88,99,11,22,33]
res=0
for ind in range(len(l)):
    if ind%2==0:
        res+=l[ind]
print(res)
#while loop
l=[44,5,66,77,88,99,11,22,33]
final=0
index=0
while index<len(l):
    if index%2==0:
        final+=l[index]
    index=index+1
print(final)
#even number from list
result=0
for val in range(len(l)):
    if l[val]%2==0:
        result+=l[val]
print(result)
#while loop to get addtion of even no from list
ino=0
Res=0
while ino<len(l):
    if l[ino]%2==0:
        Res+=l[ino]
    ino+=1
print(Res)
#reverse of list using negative index
list1=[4,3,2]
list2=[]
for val in range(-1,-len(list1)-1,-1):
    list2.append(list1[val])
print(list2)
#while loop
pos=-1
ans=[]
while pos>=-len(list1):
    ans.append(list1[pos])
    pos-=1
print(ans)
    
#positive index
list1=[7,8,9]
for val in range(len(list1)-1,-1,-1):
    list2.append(list1[val])
print(list2)
#print the sum of target no is 7 from 2 list
list22=[1,3,4,5,2,3]
for start in range(len(list22)):
    for ending in range(start+1,len(list22)):
        if list22[start]+list22[ending]==7:
            print(list22[start],list22[start])
#prime num from list
L=[33,44,55,66,77]
res=[]
for num in L:
    if num>1:
        for val in range( 2,num//2+1):
            if num%val==0:
                break
        else:
            res.append(num)
print(res)
        
