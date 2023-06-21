# Patrones de diseño #

Un patrón de diseño es una solución general reusable para un problema común en diseño de software. 

Provee un enfoque probado o un template para resolver un problema, haciendo más fácil el desarrollo de software bien estructurado, mantenible y escalable. 

Existen varios tipos de patrones de diseño: 

1. Creational

Son aquellos especializados en mecanismos para la creación de objetos. 

Proveen maneras de crear objetos ocultando la lógica de creación. 

2. Structural

Se enfocan en la composición de clases y objetos para formar grandes estructuras y relaciones entre ellos.

Asegura que las clases y objetos se combinen de manera flexible y eficiente. 

3. Behavioral

Estos especifican la manera en la que interactuan y se comunican multiples objetos entre si. 

Especifican como los objetos interactuan y distribuyen responsabilidad entre si. 

__**EJEMPLOS:**__ Singleton (creational), factory(creational), observer (behavioral), strategy (structural) y command (structural). 

# Singleton #

Es un patrón de diseño creacional que garantiza que una clase solo tiene una instancia y solo existe un punto de acceso a ella. 

Cuando un usuario requiere una instancia de la clase, el patrón singleton chequea si la instancia existe, en caso afirmativo la retorna, en caso contrario la crea y la retorna. 

