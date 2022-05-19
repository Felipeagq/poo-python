class Perro:
    def __init__(self):
        pass
    
    @property # obtener el nombre
    def name(self):
        return self._name
    
    @name.setter # asignar el nombre
    def name(self,name):
        self._name = name

perro = Perro()
perro.name = "Kaizer"
print(perro.name)


class A:
    # name = None
    def __init__(self):
        pass

a = A()
a.name = "a"
a.name_two = "A"
print(a.name)
print(a.name_two)