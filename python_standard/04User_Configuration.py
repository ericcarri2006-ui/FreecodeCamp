test_settings = {
    "theme": "dark",
    "language": "es"
}

# Añade una nueva configuración al diccionario si la clave no existe
def add_setting(config_dict, setting_tuple):
    # Desempaquetamos la tupla en clave y valor
    key, value = setting_tuple
    # Normalizamos a minúsculas para evitar duplicados por capitalización
    key = key.lower()
    value = value.lower()

    # Si la clave ya existe, no permitimos sobreescribirla
    if key in config_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        # Si no existe, la insertamos y confirmamos
        config_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

# Actualiza el valor de una configuración existente
def update_setting(config_dict, update_tuple):
    key, value = update_tuple
    key = key.lower()
    value = value.lower()

    # Solo actualizamos si la clave ya existe en el diccionario
    if key in config_dict:
        config_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        # No se puede actualizar algo que no existe
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Elimina una configuración del diccionario por su clave
def delete_setting(config_dict, key):
    # Normalizamos la clave antes de buscarla
    key = key.lower()

    if key in config_dict:
        # Borramos la entrada y confirmamos
        del config_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

# Muestra todas las configuraciones actuales del diccionario
def view_settings(config_dict):
    # Caso especial: diccionario vacío
    if not config_dict:
        return f"No settings available."
    
    # Cabecera del listado
    result = f"Current User Settings:\n"
    # Recorremos cada par clave-valor y lo añadimos al resultado
    for key, value in config_dict.items():
        # Capitalizamos la clave para mejor legibilidad
        result += f"{key.capitalize()}: {value}\n"
    
    return result


print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(delete_setting({'theme': 'light'}, 'theme'))
print(view_settings(test_settings))
print(view_settings(test_settings))
