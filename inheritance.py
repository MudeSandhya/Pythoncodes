"""class dad():
    def phone(self):
        print("das's phone use by son")
class mom():
    def sweet(self):
        print("mom's sweet to son")
class son(dad,mom):#class son(dad)-single classs(son class) inherits another class(dad())
    #class son(dad,mom): in this single class inherits an multiple class
    def laptop(self):
        print("son's labtop")
obj=son()
obj.laptop()
obj.phone()
obj.sweet()"""

#hierarchial inheritance one base class inherit multi class
class dad():
    def phone(self):
        print("dad's phone")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s2=son2()
s2.phone()
    

    
