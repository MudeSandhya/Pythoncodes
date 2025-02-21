num=145
dub=num
while num!=num:
    id=num%10
    fact=1
    for val in range(1,id+1):
        fact=fact*val
    print(fact)
    res=res+fact
    num=num//10
if dub==num:
    print("strong number")
else:
    print("not a strong nmber")
    
    
