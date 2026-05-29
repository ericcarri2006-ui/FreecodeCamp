def pin_extractor(poems):
    # Lista donde guardaremos el código final de cada poema
    secret_codes = []
    
    # Bucle principal para iterar sobre la lista de poemas recibida
    for poem in poems:
        # Inicializamos el código de este poema como una cadena vacía
        secret_code = ''
        # Dividimos el poema en una lista de líneas usando el salto de línea como separador
        lines = poem.split('\n')
        
        # Recorremos cada línea obteniendo también su índice (0, 1, 2...)
        for line_index, line in enumerate(lines):
            # Dividimos la línea actual en una lista de palabras
            words = line.split()
            
            # Comprobamos si la lista de palabras tiene suficientes elementos para el índice actual
            if len(words) > line_index:
                # Si existe, medimos la longitud de la palabra que ocupa la posición del índice
                # y la añadimos al código secreto como texto
                secret_code += str(len(words[line_index]))
            else:
                # Si la línea no tiene suficientes palabras para ese índice, añadimos un '0'
                secret_code += '0'
        
        # Al terminar de procesar todas las líneas del poema, guardamos su código en la lista general
        secret_codes.append(secret_code)
    
    # Una vez procesados todos los poemas, devolvemos la lista con todos los resultados
    return secret_codes        

# Definición de los poemas de prueba
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Llamada a la función pasando una lista con los tres poemas e imprimiendo el resultado
print(pin_extractor([poem, poem2, poem3]))
