"""num=17
dup=num
res=0
while dup!=0:
    ld=dup%10
    res=res*10+ld
    dup=dup//10
if num!=res:
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                print("not an EMIPR")
                break
        else:
            if res>1:
                for val in range(2,res//2+1):
                    if res%val==0:
                        print("no EMIPR")
                        break
                else:
                    print("emipr")
else:
    print("no emipr")
"""
def prime(num,val=2):
    if num<=1:
        return 0
    if num==val:
        return 1
    if num%val==0:
        return 0
    return prime(num,val+1)
def reverse(num,result=0):
    if num==0:
        return result
    return reverse(num//10,result*10+num%10)
def emipr(num):
    rev=reverse(num)
    if rev==num:
        return "no emipr"
    if prime(num) and prime(rev):
        return "emipr"
    else:
        return "no emipr"
num=int(input())
print(reverse(num))
print(emipr(num))

                            
                    

