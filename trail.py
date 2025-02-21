def function(num,power,res=0):
        ld=num%10
        res+=ld*power
        power//=10
        num//=10
num=121
power=10**(len(str(num))-1)
print(function(num,power))
