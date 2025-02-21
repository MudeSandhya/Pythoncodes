num=121
dub=num
res=0
power=10**(len(str(num))-1)
while num!=0:
    rem=num%10
    res+=power*rem
    num=num//10
    power=power//10
print(res)
if res==dub:
    print("its an palindrome")
else:
    print("its not an palindrone")
