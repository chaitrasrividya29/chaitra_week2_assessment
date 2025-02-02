class vehicle:
    def __init__(self):
        print("vechile base")
class car(vehicle):
    def __init__(self):
        print("car child of  vechile")
class electriccar(car):
    def __init__(self):
        super().__init__()
        print(" electriccar child of  car")
class bike(vehicle):
    def __init__(self):
        print("bike child of  vechile")
c=electriccar()
b=bike()
