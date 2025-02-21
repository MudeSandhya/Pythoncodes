"""def bin(num,res=0):
    pos=1
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos*=10
        num=num//2
    return res
print(list(map(bin,range(10,21))))
print(list(map(lambda val:bin(val),range(10,21))))
def even(num):
    if num%2==0:
        return True
    return False
print(list(filter(even,range(1,41))))"""
#maximum no of number
"""
def max(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print("maximum:",num1)
    elif num2>num3:
        if num2>num1:
            print("maximum:",num2)
    else:
        print("maximum:",num3)

"""
#max(55,6,44)sum of the 3 number
"""def sum(val=0):
    list1=(8,2,3,0,7)
    for val in list1:
        val+=val
    return val
print(sum())"""
#reverse the string
def rev(val):
    

    
    

