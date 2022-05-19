from abc import ABCMeta, abstractmethod

class Calculation(metaclass=ABCMeta):
    
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def substract(self):
        pass
    
    def multiply(self):
        print(self)
    
    def division(self):
        pass


# @abstractmethod es un metodo que debe ser abstraido en las clases hijas
# si un metodo tiene @abstractmethod, tiene que ser heredado.


class Calculator1(Calculation):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a + self.b)
    
    def substract(self):
        print(self.a - self.b)


one = Calculator1(10,4)
one.add()
one.multiply() # se puede usar porque lo hereda.
one.substract()



# @Calculation.register virtualiza la sub clase,
# No tenemos ayuda del Helper de python,
# pero podemos saltarnos los metodos abstractos 
@Calculation.register
class Calculator2:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a + self.b)


two = Calculator2(10,4)
two.add()
print(issubclass(Calculator2,Calculation)) # True
# .register si la hace subclase.