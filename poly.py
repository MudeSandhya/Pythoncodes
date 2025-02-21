class employee(): 
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
management=manager("sindhiya","10000","cse")
management.display()
        
