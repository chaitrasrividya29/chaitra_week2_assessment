class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber

    def display(self):
        return f"name of the student: {self.name} roll number : {self.rollnumber}"
    
std=student("chaitra",6761)
print(std.display())