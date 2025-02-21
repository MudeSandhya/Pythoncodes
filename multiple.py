class father  :
    def properties(self):
        print("earning")
        print("eating")
class mother:
    def properties(self):
        print("helping")
        print("crime support")
class child(father,mother):
    def properities(self):
        super().properties()
        mother.properties(self) 
        print("no money")
        print("wasting time")
obj=child()
obj.properties()
