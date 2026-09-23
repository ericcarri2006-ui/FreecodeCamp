class Planet:
    def __init__(self, name, planet_type, star):
        # Validación de tipos: los tres argumentos deben ser cadenas
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        # Validación de contenido: ninguna cadena puede estar vacía
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')

        # Asignación de los atributos de instancia
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        # Devuelve el texto de la órbita con el formato exacto pedido
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        # Representación en texto del objeto
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


# Creación de las tres instancias
planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_3 = Planet('Neptune', 'Ice Giant', 'Sun')

# Imprimir cada objeto (usa el método __str__)
print(planet_1)
print(planet_2)
print(planet_3)

# Llamar a orbit() en cada planeta e imprimir el resultado
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
