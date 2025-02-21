#6.44 video 
"""class student:
    def __init__(self):
        self.name="sindhiya"
        self.regno="122"
    def display(self):
        print("name:", self.name)
        print("student:", self.regno)
detail=student()
print(detail.name)
print(detail.regno)
detail.display()
#exampe 2 6.56
class fruit:
    def __init__(self,color):
        self.color="red"
apple=fruit()
print(apple.color)"""
#example 3 video 7.03
"""class teacher:
    def __init__(self,id,reg):
        self.name=id
        self.regno=reg
    def display(self):
        print("name:",self.name)
        print("id:",self.regno)
t1=teacher("sindhiya","sister for shalini")
t2=teacher("shalini","sister for sindhiya")
t1.display()
t2.display()"""
#example 4 video 7.09
"""class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        add=int(self.a)+int(self.b)
        print("addtion:",add)
    def sub(self):
        sub=int(self.a)-int(self.b)
        print("sub:" ,sub)
    def mul(self):
        mul=int(self.a)*int(self.b)
        print("mul:" ,mul)
    def div(self):
        div=int(self.a)/int(self.b)
        print("div:",div ) 
A=calculator(10,20)
A.add()
A.sub()
A.mul()
A.div()"""
  #alter method
class calculator:
    def add(self,a,b):
        print("add:",a+b)
    def sub(self,a,b):
        print("sub:",a-b)
o1=calculator()
o1.add(10,30)
o1.sub(30,55)


