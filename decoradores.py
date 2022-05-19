# DECORADORES FUNCIÓN
def decorador(func):
    def nueva_funcion():
        print("funcionalidad nueva antes")
        func()
        print("funcionalidad nueva despues")
    return nueva_funcion

@decorador
def funcion():
    print("LA FUNCION")

funcion()




def decorador2(func):
    def nueva_funcion(instancia): # deben ir los argumentos que se van a usar
        print("funcionalidad nueva antes")
        func(instancia)
        print("funcionalidad nueva despues")
    return nueva_funcion

# Se puede decorar una función de una clase
class A:
    @decorador2
    def funcion_clase(self):
        print("FUNCIONALIDAD DE CLASE 2")

a = A()
a.funcion_clase()




def decorador3(func):
    def nueva_funcion(*args): # deben ir los argumentos que se van a usar
        print("funcionalidad nueva antes")
        func(*args)
        print("funcionalidad nueva despues")
    return nueva_funcion

# Se puede decorar una función de una clase
class B:
    @decorador3
    def funcion_clase(self):
        print("FUNCIONALIDAD DE CLASE 3")

b = B()
b.funcion_clase()