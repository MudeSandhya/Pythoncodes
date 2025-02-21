class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self,l,b):
        l=30
        b=40
        rect=l*b
        return rect
rec=rectangle( )
print(rec.area(3,4))

