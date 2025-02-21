def func():
    global fname 
    fname = "sindhiya durai"  

fname = "sindhiya"  
func()  
print(fname)

def func(name):
    fname[0] = "sindhiya durai"  
    return name

fname = ["sindhiya"] 
fname = func(fname)
print(fname[0]) 

