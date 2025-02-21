"""s_username="EMC"
s_password="123"

user=input("user ")
passno=input("passno ")

def validation():
    if(user==s_username and passno==s_passwword):
        print("valid")
    else:
        print("invalid")
validation()"""
#validate true or false using return function
"""s_username="EMC"
s_password="123"

user=input("user ")
passno=input("passno ")

def validation():
    if(user==s_username and passno==s_password):
        return True
    else:
        return False
a=validation()
print(a)"""

#example 3 (a+b)*c
a=int(input("A:"))
b=int(input("b:"))
c=int(input("c:"))
def add():
    sum=a+b
    return sum*c
a=add()
print(a)



    
