num=13
while num>=10:
    res=0
    while num!=0:
        ld=num%10
        res+=ld**2
        num=num//10
    num=res
    print(res)
