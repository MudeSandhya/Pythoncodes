"""a=int(input())
b=int(input())
maxi=max(a,b)
print(maxi)"""
#factorial of a number
"""a=int(input())
fact=1
if a<0:
    print("not possible")
else:
    for i in range(1,a+1):
        fact=fact*i
    print(fact)"""
#simple interest

"""def simple_interest(p,t,r):
    simple = (p * t * r)/100
    print('The Simple Interest is', simple)
    return simple
simple_interest(8, 6, 8)"""
#palindrome
"""def ispalindrome(string):
    if(string==string[::-1]):
       return"palindrome"
    else:
        return"not palindrome"
string=input()
print(ispalindrome(string))"""
#reverse
"""string="enjoi everytime"
s=string.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(" ".join(l))"""
#missing
"""
def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))
"""
#
    
    



    

    
    
