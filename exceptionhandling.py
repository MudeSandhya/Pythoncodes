"""l=[1,2,3,45]
try:
    res=0
    for ele in l:
        res+=[ele]
    print(res)
except Exception:
    print("error occurred")
l=[1,2,3,45]
try:
    res=0
    for ele in l:
        res+=[ele]
    print(res)
except IndexError as msg:
    print(f'error:{msg}')
except NameError as msg:
    print(f'error:{msg}')
except TypeError as msg:
    print(f'error:{msg}')
l=[2,3,4,5,6]
try:
    res=0
    for ele in l:
        res+=l[ele]
    print(result)
except Exception as msg:
    print(f'error:{msg}')
except (IndexError,NameError,TypeError) as msg:
    print(f'error:{msg}')
num=int(input())
try:
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                raise Exception
    else:
        raise Exception
except:
    print('prime number')
else:
    print('nonprimenumber')"""
#armstrong number by Exception handling in user defined Exception
class armstrong(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    num=int(input("enter the nuber:"))
    res=0
    power=len(str(num))
    while num!=0:
        ld=num%10
        res+=ld**power
        num//=10
    if res!=num:
        raise armstrong("NotArmstrong")
except Exception as msg:
    print(f'error:{msg}' )
else:
    print("no ARMSTRONG NUMBER")
finally:
    print("excetion done")
    
    
        

    
    
