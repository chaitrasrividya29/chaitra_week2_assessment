class product:
    def __init__ (self):
        self.name=input("enter name")
        self.price=int(input("enter price"))
        self.stock=int(input("enter stock"))
        self.req_quantity=int(input("enter req_quantity"))
    def check_availability(self):
        if self.req_quantity<=self.stock:
            return "required quantity available"
        else:
            return "not available"
        
p=product()
print(p.check_availability())
        