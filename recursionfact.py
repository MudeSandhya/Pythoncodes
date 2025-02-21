def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
num=5
print(fact(num))
def fact(val,num):
    if val==num or val==num+1:
        return val
    return val*fact(val+1,num)
print(fact(1,7))
#armstrong using recursion
def armstrong(num,power):
    if num==0:
        return 0
    return (num%10)**power+armstrong(num//10,power)
num=153
power=len(str(num))
print(armstrong(num,power))
print("armstrong" if num==armstrong(num,power) else "not an amstrong")
#diarum using disarum
def disarum(num,power):
    if num==0:
        return 0
    print(power)
    return (num%10)**power+disarum(num//10,power-1)
num=135
power=len(str(num))
print("disarum" if num==disarum(num,power) else "not an disarum")
#strong no
def facter(num):
    if num==0 or num==1:
        return 1
    return num*facter(num-1)
def strong(num):
    if num==0:
        return 0
    return facter(num%10) + strong(num//10)
num=145
print("strong no" if num==strong(num) else "no strong numbber")
#happy no
def happy(num):
    if num<10:
        return num==0 or num==7
    return happy(check(num))
def check(num):
    if num==0:
        return 0
    return (num%10)**2+check(num//10)
num=19
print("happy no" if happy(num) else "no happy number")
        
        


