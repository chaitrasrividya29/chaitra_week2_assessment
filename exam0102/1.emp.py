class  emp:
    def __init__(self):
        self.name= input("enter name")
        self.id=int(input("enter id"))
        self.department=input("enter department")
    
    def display(self):
        print("name",self.name)
        print("id",self.id)
        print("department",self.department)

e=emp()
e.display()