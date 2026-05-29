Descripcion General
Este script contiene una funcion denominada pin_extractor diseñada para generar codigos numericos (PINs) a partir de una lista de textos o poemas. El sistema utiliza una logica de posicionamiento dinamico donde el numero de la linea determina que palabra debe analizarse para extraer su longitud y construir el codigo final.

Requisitos
Python 3.x

No requiere librerias externas.

Estructura del Codigo
El programa se divide en tres secciones principales:

Definicion de la funcion procesadora.

Declaracion de variables de entrada (strings con formato multilineal).

Ejecucion y salida de resultados.

Funcionamiento Paso a Paso
1. Inicializacion
La funcion recibe una lista de poemas. Se crea una lista vacia llamada secret_codes que servira como contenedor para los resultados finales. Por cada poema en la lista, se reinicia una cadena de texto vacia (secret_code) que almacenara los digitos del PIN actual.

2. Segmentacion de Texto
El codigo realiza dos niveles de division (parsing):

Division por lineas: Utiliza poem.split('\n') para convertir el bloque de texto en una lista donde cada elemento es una linea individual.

Division por palabras: Dentro de cada linea, utiliza line.split() para separar las palabras eliminando los espacios en blanco sobrantes.

3. Logica de Extraccion (Indice n en Linea n)
Para cada linea del poema, la funcion realiza las siguientes operaciones:

Identifica el numero de linea actual mediante la funcion enumerate (empezando desde 0).

Verifica la existencia de la palabra: Comprueba si la cantidad de palabras en esa linea es mayor al indice de la linea actual (len(words) > line_index).

Caso positivo: Si la palabra existe en esa posicion, calcula su longitud con len() y añade dicho numero al codigo secreto.

Caso negativo: Si la linea es demasiado corta y no contiene una palabra en esa posicion, añade un caracter '0' por defecto.

4. Compilacion y Retorno
Una vez procesadas todas las lineas de un poema, el codigo resultante se añade a la lista general. Tras procesar todos los poemas de la entrada, la funcion retorna la lista completa de codigos generados.

Ejemplo de Ejecucion
Si la primera linea (indice 0) de un poema es "Stars and the moon", el codigo tomara la palabra en la posicion 0 ("Stars"), contara sus 5 letras y el primer digito del PIN sera "5". En la segunda linea (indice 1), buscara la palabra en la posicion 1, y asi sucesivamente.

Uso
Para ejecutar el script, se deben agrupar los strings de los poemas en una lista y pasarla como argumento a la funcion:
print(pin_extractor([poema1, poema2, poema3]))
