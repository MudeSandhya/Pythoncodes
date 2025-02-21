num=11
cfact=0
for i in range(1,num+1):
    if num%i==0:
        cfact=cfact+1
    if cfact==2:
        print(f'{i} is an prime number')
else:
    print(f'{i} is not an prime number')
    
