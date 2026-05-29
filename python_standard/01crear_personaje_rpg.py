full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    # Valida que el nombre sea una cadena de texto
    if not isinstance(name, str):
        return "The character name should be a string"
    
    # Valida que el nombre no esté vacío
    if len(name) == 0:
        return 'The character should have a name'
    
    # Valida que el nombre no tenga más de 10 caracteres
    if len(name) > 10:
        return "The character name is too long"
    
    # Valida que el nombre no contenga espacios
    if ' ' in name:
        return "The character name should not contain spaces"
    
    # Valida que todas las estadísticas sean números enteros
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    
    # Valida que todas las estadísticas sean al menos 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    # Valida que ninguna estadística supere el valor 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    # Valida que la suma de las estadísticas sea exactamente 7
    if not strength + intelligence + charisma == 7:
        return 'The character should start with 7 points'

    # Construye las barras de estadísticas con puntos llenos y vacíos hasta llegar a 10
    str_bar = f"STR {'●' * strength}{'○' * (10 - strength)}"
    int_bar = f"INT {'●' * intelligence}{'○' * (10 - intelligence)}"
    cha_bar = f"CHA {'●' * charisma}{'○' * (10 - charisma)}"

    # Devuelve la ficha del personaje con el nombre y las estadísticas
    return f"{name}\n{str_bar}\n{int_bar}\n{cha_bar}"

# Ejemplo de uso
create_character('ren', 4, 2, 1)
