Descripción

Este programa define una clase llamada Planet que representa un planeta con tres datos: su nombre, su tipo y la estrella alrededor de la que gira. Al final del archivo se crean tres planetas de ejemplo y se muestran por pantalla.


Cómo se ejecuta

Solo hace falta tener Python 3 instalado. Desde la terminal, en la carpeta donde esté el archivo:

    python planet.py

(o python3 planet.py, según el sistema)


Qué hace la clase Planet

1. Método __init__

Es el constructor. Recibe name, planet_type y star, y antes de guardarlos hace dos comprobaciones:

- Si alguno de los tres no es una cadena de texto, lanza un TypeError con el mensaje "name, planet type, and star must be strings".
- Si alguno de los tres es una cadena vacía, lanza un ValueError con el mensaje "name, planet_type, and star must be non-empty strings".

El orden importa: primero se mira el tipo y después si está vacío. Si se hiciera al revés, un valor que no sea cadena (por ejemplo un número) daría un error raro al compararlo con la cadena vacía en vez del error que toca.

Si todo es correcto, los valores se guardan en self.name, self.planet_type y self.star.

Un detalle: el mensaje del TypeError escribe "planet type" con espacio y el del ValueError escribe "planet_type" con guion bajo. Es así a propósito porque el enunciado lo pide de esa forma y hay que copiarlo tal cual.

2. Método orbit

Devuelve un texto con el formato:

    {name} is orbiting around {star}...

Por ejemplo: "Earth is orbiting around Sun...". Ojo, no imprime nada, solo devuelve la cadena. Por eso luego hay que meterlo dentro de un print() para verlo.

3. Método __str__

Define cómo se ve el objeto cuando se imprime. Devuelve:

    Planet: {name} | Type: {planet_type} | Star: {star}

Gracias a este método, al hacer print(planet_1) se ve ese texto en lugar de algo tipo <__main__.Planet object at 0x...>.


Instancias de ejemplo

Se crean tres planetas:

    planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
    planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
    planet_3 = Planet('Neptune', 'Ice Giant', 'Sun')

Después se imprime cada objeto (lo que activa __str__) y luego se llama a orbit() en cada uno y se imprime lo que devuelve.


Salida esperada

    Planet: Earth | Type: Terrestrial | Star: Sun
    Planet: Jupiter | Type: Gas Giant | Star: Sun
    Planet: Neptune | Type: Ice Giant | Star: Sun
    Earth is orbiting around Sun...
    Jupiter is orbiting around Sun...
    Neptune is orbiting around Sun...


Errores que puede dar

Ejemplos de llamadas que fallan a propósito:

    Planet(123, 'Terrestrial', 'Sun')   -> TypeError
    Planet('Earth', '', 'Sun')          -> ValueError
