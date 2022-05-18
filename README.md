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

## Proceso de creación de un objeto
![](/images/construccionDeObjeto.PNG)