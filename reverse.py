num=345
def Reverse(num):
    res=0
    pos=10**len(str(num))-1
    while num!=0:
        ld=num%10
        res+=ld*pos
        num=num//10
        pos//=10
    return res
print(Reverse(678))
