Descripcion
Este proyecto implementa un sistema de gestion de configuraciones de usuario mediante diccionarios de Python. Permite realizar las operaciones basicas sobre pares clave-valor: añadir, actualizar, eliminar y visualizar configuraciones.

Estructura del proyecto
El codigo se organiza en cuatro funciones principales y un diccionario de prueba inicial:
pythontest_settings = {
    "theme": "dark",
    "language": "es"
}
Este diccionario actua como estado inicial del sistema y se usa para probar las funciones.

Funciones
add_setting(config_dict, setting_tuple)
Añade una nueva configuracion al diccionario.
Recibe el diccionario de configuraciones y una tupla con la clave y el valor. Antes de insertar, normaliza ambos a minusculas para evitar duplicados por diferencias de capitalizacion. Si la clave ya existe, devuelve un mensaje de error sin modificar el diccionario.
pythonadd_setting({'theme': 'light'}, ('THEME', 'dark'))
# "Setting 'theme' already exists! Cannot add a new setting with this name."

add_setting({'theme': 'light'}, ('volume', 'high'))
# "Setting 'volume' added with value 'high' successfully!"

update_setting(config_dict, update_tuple)
Actualiza el valor de una configuracion existente.
Recibe el diccionario y una tupla con la clave a modificar y el nuevo valor. Si la clave no existe en el diccionario, devuelve un error en lugar de crear una entrada nueva.
pythonupdate_setting({'theme': 'light'}, ('theme', 'dark'))
# "Setting 'theme' updated to 'dark' successfully!"

update_setting({'theme': 'light'}, ('volume', 'high'))
# "Setting 'volume' does not exist! Cannot update a non-existing setting."

delete_setting(config_dict, key)
Elimina una configuracion del diccionario por su clave.
A diferencia de las funciones anteriores, recibe la clave directamente como cadena de texto, no como tupla. Normaliza la clave a minusculas antes de buscarla. Si no existe, devuelve un mensaje de error.
pythondelete_setting({'theme': 'light'}, 'theme')
# "Setting 'theme' deleted successfully!"

delete_setting({'theme': 'light'}, 'volume')
# "Setting not found!"

view_settings(config_dict)
Muestra todas las configuraciones actuales del diccionario.
Si el diccionario esta vacio, devuelve un mensaje indicandolo. Si tiene entradas, construye un texto con cada par clave-valor, capitalizando la primera letra de cada clave. El resultado incluye una cabecera y termina con un salto de linea.
pythonview_settings({})
# "No settings available."

view_settings({'theme': 'dark', 'language': 'es'})
# Current User Settings:
# Theme: dark
# Language: es

Normas de funcionamiento
Todas las funciones siguen estas convenciones:

Las claves y valores se normalizan siempre a minusculas antes de operar.
Ninguna funcion modifica el diccionario si la operacion no es valida.
Todas devuelven un mensaje de texto indicando el resultado de la operacion.


Requisitos

Python 3.x
No requiere librerias externas
Compartir
