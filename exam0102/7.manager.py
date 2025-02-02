

class Person:
    def info(self):
        self.company_name=input("enter the company name")
        print(f"{self.company_name}  has 2  employees say manager and employee")  
class Employee(Person):
    def emp_details(self):
        super().info()
        self.emp_name=input("enter the name of employee")
        print(f"{self.emp_name} is the employee")
class Manager(Employee):
    def __init__(self):
        super().emp_details()
    def approve_leave(self):
        print(f"leave has been approved for {self.emp_name}")
mann=Manager()
mann.approve_leave()