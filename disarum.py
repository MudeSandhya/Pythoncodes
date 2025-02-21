num=135
rev=0
dup=num
while num!=0:
    power=len(str(num))
    ld=num%10
    rev+=ld**power
    num=num//10
if dup==rev:
    print("disarum number")
else:
    print("its not an disarum number")
