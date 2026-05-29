1. DESCRIPCION GENERAL
Este sistema proporciona un marco de validacion para estructuras de datos medicos en Python. El objetivo es filtrar y detectar errores en registros almacenados en diccionarios, garantizando que cumplan con tipos de datos especificos, formatos de expresiones regulares y logica de negocio antes de ser procesados por capas superiores de una aplicacion.

2. COMPONENTES DEL CODIGO
2.1 Estructura de Datos (medical_records)
Los datos de entrada consisten en una lista de diccionarios. Cada diccionario debe representar un paciente y contener las siguientes llaves:

patient_id: Identificador unico.

age: Edad cronologica.

gender: Genero declarado.

diagnosis: Condicion clinica.

medications: Lista de farmacos prescritos.

last_visit_id: Identificador de la ultima consulta.

2.2 Motor de Restricciones (find_invalid_records)
Esta funcion actua como el nucleo de validacion. Evalua los argumentos recibidos mediante el diccionario 'constraints':

Expresiones Regulares (re.fullmatch): Verifica que los IDs sigan el patron de una letra seguida de digitos, ignorando diferencias entre mayusculas y minusculas.

Verificacion de Tipos (isinstance): Asegura que los campos sean str, int o list segun corresponda.

Logica Condicional: Valida que la edad sea mayor o igual a 18 y que el genero se limite a opciones predefinidas.

Comprension de Listas (List Comprehension): Valida que cada elemento dentro de la lista de medicamentos sea de tipo string.

Retorno: Una lista con los nombres de las claves que fallaron alguna validacion.

2.3 Controlador de Flujo (validate)
La funcion principal gestiona la integridad global del conjunto de datos:

Validacion Estructural: Confirma que la entrada sea una secuencia iterable.

Validacion de Integridad: Compara el set de llaves del diccionario actual con un set de referencia (key_set) para detectar omisiones o campos extra.

Procesamiento de Errores: Itera sobre los fallos detectados por el motor de restricciones y genera logs detallados indicando la clave, el valor erroneo y la posicion del registro en la lista original.

3. ESPECIFICACIONES TECNICAS
Lenguaje: Python 3.x

Modulos Estandar: re (Regular Expressions)

Paradigma: Programacion funcional y procedimental.

Tecnicas de optimizacion: Uso de 'continue' para evitar computacion innecesaria en registros ya identificados como invalidos y 'enumerate' para rastreo de indices.

4. FORMATO DE SALIDA
Si los datos son correctos: Retorna True y emite "Valid format."

Si hay errores: Emite una descripcion por cada fallo detectado (formato, tipo o valor) y retorna False al finalizar el escaneo.
