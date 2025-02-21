#armstrong number
def armstrong(num,power,res=0):
    while num!=0:
        ld=num%10
        res+=ld**power
        num//=10
    return res
num=153
print("armstromg" if armstrong(num,power=len(str(num)))==num else "not armstrong")
#disarum number
def disarum(num,power,res=0):
    while num!=0:
        ld=num%10
        res+=ld**power
        num//=10
        power-=1
    return res
num=135
print('disarum' if disarum(num,power=len(str(num)))== num else 'not an disarum' )
#int to number
def binary(num,res=0,pos=1):
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos*=10
        num=num//2
    return res
print(binary(12))
#binary to int
def int(num,res=0,power=0):
    while num>0:
        ld=num%10
        res+=ld*2**power
        power+=1
        num//=10
    return res
print(int(binary(12)))
#reverse an number
def reverse(num,res=0):
    while num>0:
        ld=num%10
        res+=ld*10**(len(str(num))-1)
        num//=10
    return res
print(reverse(345))
#strong num
def strong(num,fact=1):
    while num!=0:
        fact*=num
        num-=1
    return fact
print(strong(5))
#alter string by for loob
def strong1(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
print(strong(6))
print(strong1(6))
#happy number
'''def happy(num):
    num=square(num)
    if num==1 or num == 7:
        return "happy number"
    else:
        return "no happy number"
def square(num):
    while num>=10:
        res=0
        while num!=0:
            ld=num%10
            res+=ld**2
            num//=10
    return res
print(happy(19))'''
#happy number
def square(num):
    res=0
    while num!=0:
        ld=num%10
        res+=ld**2
        num//=10
    return res
def check(num):
    while num>=10:
        num=square(num)
    if num==1 or num==7:
        print("happynumber")
    else:
        print("No HappyNumber")
check(89)



