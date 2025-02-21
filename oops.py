"""class Cls1:
    def __init__(self):
        print("its an constructor")
obj1=Cls1()
print("*"*10)
obj2=Cls1()
print("-"*10)
"""
#objject reference
'''class c203:
    course="PFS"
    time="4:30"
    batch="M17"
    def __init__(self,name,mblno,adhar):
        self.name=name
        self.mblno=mblno
        self.adhar=adhar
obj1=c203('sindhiya',7548819758,123456789)
obj2=c203('shalini',87654354,345678321)
obj3=c203('na chelle',789657844,567890321)
print(obj3.name)
print(obj2.name)'''
class c203:
    course="PFS"
    batch="m17"
    timing="4.30"
    def __init__(self,name,phno,adhar):
        self.name=name
        self.phno=phno
        self.adhar=adhar
    def detail(self):
        print(f'name={self.name}')
        print(f'phno={self.phno}')
        print(f'adhar={self.adhar}')
obj1=c203("shalini",456373891,1233131344252)
obj2=c203("sindhiya",784563242,456789398734)
obj2.detail()
        
        
