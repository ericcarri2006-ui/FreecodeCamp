# Importa el módulo de expresiones regulares para la validación de patrones de cadenas de texto.
import re

# Estructura de datos simulada: una lista que contiene múltiples diccionarios, 
# donde cada diccionario representa un registro médico estructurado.
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    # Función auxiliar para validar los campos individuales de un registro.
    # Recibe los valores del diccionario desempaquetados como argumentos.
    
    # El diccionario 'constraints' almacena el resultado booleano (True/False) 
    # de evaluar condiciones lógicas estrictas sobre cada campo.
    constraints = {
        # Valida que sea de tipo string y cumpla el patrón regex: 
        # letra 'p' (ignorando mayúsculas) seguida de uno o más dígitos numéricos (\d+).
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        
        # Valida tipo entero y rango lógico.
        'age': isinstance(age, int) and age >= 18,
        
        # Valida tipo string y restringe el valor exacto a dos opciones mediante lower().
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        
        # Permite tipo string o tipo NoneType (ausencia de diagnóstico).
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        
        # Valida tipo lista y, mediante una comprensión evaluada por all(), 
        # garantiza que todos los elementos internos sean de tipo string.
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        
        # Valida patrón regex análogo a patient_id, pero comenzando con la letra 'v'.
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    
    # Retorna una lista generada por comprensión que filtra y contiene únicamente 
    # las claves de 'constraints' cuyo valor booleano fue False (es decir, fallaron la validación).
    return [key for key, value in constraints.items() if not value]

def validate(data):
    # Función principal que coordina el proceso de validación del conjunto de datos completo.
    
    # Validación de tipo inicial: comprueba que la estructura principal sea iterable (lista o tupla).
    is_sequence = isinstance(data, (list, tuple))

    # Ejecuta un retorno temprano (early return) si la estructura base no es válida,
    # evitando excepciones de iteración más adelante.
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    # Bandera global para rastrear si se encuentra al menos un error en toda la secuencia.
    is_invalid = False
    
    # Define un objeto set (conjunto) inmutable que contiene el esquema exacto de claves requeridas.
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Itera sobre la secuencia obteniendo el índice posicional y el sub-elemento (diccionario).
    for index, dictionary in enumerate(data):
        
        # Comprobación de tipo estructural: el elemento debe ser obligatoriamente un diccionario.
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue # Interrumpe el ciclo actual y salta al siguiente elemento de 'data'.

        # Comprobación de integridad estructural: convierte las claves del diccionario en un set
        # y las compara con el key_set maestro. Detecta claves faltantes o sobrantes.
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue # Salta al siguiente registro, ya que este no tiene la estructura necesaria para ser evaluado.

        # Desempaquetado de diccionario (**dictionary): pasa los pares clave-valor 
        # directamente como argumentos a la función find_invalid_records.
        invalid_records = find_invalid_records(**dictionary)
        
        # Itera sobre la lista de campos que no pasaron las reglas de validación en constraints.
        for key in invalid_records:
            # Extrae el valor anómalo utilizando la clave identificada.
            val = dictionary[key]
            # Genera un log en consola con el formato de interpolación f-string indicando clave, valor e índice.
            print(f"Unexpected format '{key}: {val}' at position {index}.")
        
            # Activa la bandera global indicando que la estructura general de datos contiene registros sucios.
            is_invalid = True        

    # Evaluación final de estado.
    if is_invalid:
        return False
        
    print('Valid format.')
    return True

# Llamada a la función principal para ejecutar el script sobre los datos simulados.
validate(medical_records)
