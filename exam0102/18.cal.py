from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def Add(self):
        pass
    @abstractmethod
    def Sub(self):
        pass
    @abstractmethod
    def Divide(self):
        pass
    @abstractmethod
    def Multiply(self):
        pass

class BasicCalculator(ICalculator):
    def Add(self,a,b):
        return a+b
    def Sub(self,a,b):
        return a-b
    def Multiply(self,a,b):
        return a*b
    def Divide(self,a,b):
        return a/b
    
BasicCalc=BasicCalculator()
print("addition : ",BasicCalc.Add(2,4))
print("substraction : ",BasicCalc.Sub(8,2))
print("Multiplication : ",BasicCalc.Multiply(2,3))
print("Division : ",BasicCalc.Divide(6,3))