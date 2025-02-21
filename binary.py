num=int(input())
def binaryint(num):
    res=0
    power=0
    while num!=0:
        ld=num%10
        res=res+ld*(2**power)
        num=num//10
        power+=1
       
    return res
print(binaryint(num))
        
   
