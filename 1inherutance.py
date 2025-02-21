class A:
    var=100
    var2=200
class B(A):
    var2=300
    var4=800
obj=B()
"""print(obj.var2)
#multi inheritance
class A:
    var1=100
    var2=9
class B(A):
    var1=0
    var4=420
class C(B):
    var5=11
    var2=15
obj=C()
print(obj.var2)
#chaining
  #super chaining
class A:
    def __init__(self,name,mob):
        self.name=name
        self.mob=mob
class B(A):
    def __init__(self,name,mob,aadhar,pan):
        super().__init__(name,mob)
        self.aadhar=aadhar
        self.pan=pan
obj=B("sindhiya",7548819758,"ASDT45667345",6789567)
print(obj.mob)
print(obj.name)
      #class chaining
class c:
    def __init__(self,name,mob):
        self.name=name
        self.mob=mob
class D(C):
    def __init__(self,name,mob,adhar,pan):
        C.__init__(self)
        self.adhar=adhar
        self.pan=pan
obj=D("sindhiya",7548819758,"ADUCGD456","PAND34568D")
print(obj.adhar)
class student:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
class scoredetail(student):
    def __init__(self,name,phno,score):
        super().__init__(name,phno)
        self.score=score
obj=scoredetail('sindhiya',7548819758,99)
print(obj.phno)"""
class student():
    def __init__(self,name,phno,course):
        self.name=name
        self.phno=phno
        self.course=course
    def detail(self):
        print(f'name:{self.name}')
        print(f'phno:{self.phno}')
        print(f'course:{self.course}')
        
class update(student):
    def __init__(self,name,phno,course,score):
        student.__init__(self,name,phno,course)
        self.score=score
    def detail(self):
        student.detail(self)
        print(f'score:{self.score}')
class studentdetails(update):
    def __init__(self,name,phno,course,score,time):
        update.__init__(self,name,phno,course,score)
        self.time=time
    def detail(self):
        super().detail()
        print(f'time {self.time}')
obj=studentdetails("sindhiya",7548869758,"pfs","p1","11.00")
obj.detail()
            


        
    
