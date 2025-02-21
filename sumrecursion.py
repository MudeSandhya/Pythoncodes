def sum(num):
    if num==0:
        return 0
    return int(num%10)+int(sum(num//10))
num=1234
print(sum(num))
