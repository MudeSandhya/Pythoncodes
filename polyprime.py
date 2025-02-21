def prime(num,val=2):
    if num<=1:
        return 0
    if num==val:
        return 1
    if num%val==0:
        return 0
    return prime(num,val+1)
def reverse(num,result=0):
    if num==0:
        return result
    return reverse(num//10,result*10 + num%10)
def polyprime(num):
    rev=reverse(num)
    if prime(num)==prime(rev):
        return "polyprime"
    return "no polyprime"
num=int(input())
print(polyprime(num))

