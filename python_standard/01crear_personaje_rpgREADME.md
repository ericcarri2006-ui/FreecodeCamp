Build an RPG Character
Función en Python que valida y crea un personaje RPG con nombre y tres estadísticas (fuerza, inteligencia y carisma), representadas visualmente con barras de puntos.

¿Cómo funciona?
La función create_character(name, strength, intelligence, charisma) recibe el nombre del personaje y sus tres estadísticas, valida que todo sea correcto y devuelve una ficha visual del personaje.

Reglas de validación

El nombre debe ser una cadena de texto
El nombre no puede estar vacío
El nombre no puede tener más de 10 caracteres
El nombre no puede contener espacios
Las estadísticas deben ser números enteros
Cada estadística debe estar entre 1 y 4
La suma de las tres estadísticas debe ser exactamente 7


Ejemplo de uso
pythoncreate_character('ren', 4, 2, 1)
Resultado:
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○

Tecnologías

Python 3


Curso
Ejercicio realizado como parte del curso Scientific Computing with Python de freeCodeCamp.
