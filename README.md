# POO Python

## 4 Pilares de la POO:
- Abstracción: Expresar caracteristicas de un objeto real o imaginario que los distinguen de los demas. 
    - Caracteristicas.
    - Comportamiento/Acciones.
- Encapsulamiento: Proceso que se ocultan las caracteristicas o los datos internos del objeto al mundo exterior y se oculta la complejidad o detalles de como se implementan.
- Herencia: La capacidad de heredar las caracteristicas y comportamientos de clases superiores.
- Polimorfismo: En tiempo de ejecución nuestro programa puede ejecutar acciones diferentes. 

## Que es una clase
Nos permite abstraer los datos del mundo real y encapsular la complejidad  para darle forma a la aplicación
## estructura y representación UML 
![](/images/representacionUML.PNG)
## En Memoria
Las clases se guardan en la memoria, la cual puede separase en dos, tabla de simbolos y Monticulo.
- La tabla de simbolos guarda los objetos creados.
- Los monticulos guarda la estrcutura y la abstracción de la clase.
![](/images/EnEspacioMemoria.PNG)

## Constructores
Es un metodo especial por el cual accedemos para inicializar un objeto:
- No retorna, solo inicializa nuestro objeto.
- Se puede tener varios constructores.
- En la representación UML deberá tener el mismo nombre de la clase.
- Es llamado indirectamente cuando creamos un objeto.
- Si no se crea el constructor, este se creará vacio en tiempo de ejecución.
![](/images/constructorUML.PNG)

### Proceso de creación de un objeto
![](/images/construccionDeObjeto.PNG)

## Destructor
Metodo especial el cual se accede cuando un objeto ya no esta en uso y se destruye en memoria:
- No retorna datos.
- No pide valores.
- Su representación UML tiene el mismo nombre de la clase solo que se antepone de un (~).
- Solo puede ser llamado indirectamente cuando dejamos de usar un objeto o perdemos la referencia al monticulo.
- Si una clase hace referencia a otra, primero se destruye la más alejada y sin relación y por ultimo destruye la más alta. 

### Destructor representación UML
![](/images/representacionUMLDestructor.PNG)

### Proceso destructor en memoria
![](/images/destructorDeObjeto.PNG)




# ABC (Abstract Base Class)
An Abstract class is one of important concept in object oriented p
rogramming(oops). It is like blueprint for other classes.

Abstract class nos provee de los detalles de una clase, por defecto, python no nos provee Abstract class, pero el modulo ABC nos provee de esta infraestructura.

### @abstractmethod
Es un  decorador para un metodo que debe ser abstraido en las clases hijas, si un metodo tiene @abstractmethod, tiene que ser heredado, sino, este nos arrojará error.

### @class.register
@Calculation.register virtualiza la sub clase, No tenemos ayuda del Helper de python, pero podemos saltarnos los metodos abstractos.