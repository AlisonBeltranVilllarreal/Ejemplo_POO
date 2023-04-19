# Definimos una clase llamada Animal
class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print("El animal hace un sonido.")

# Definimos una clase llamada Perro que hereda de la clase Animal
class Perro(Animal):
    
    # Definimos el constructor de la clase con dos parámetros: nombre y raza
    def __init__(self, nombre, raza):
        # Llamamos al constructor de la clase Animal para asignar el nombre del perro
        super().__init__(nombre)
        self.raza = raza

    # Definimos un método llamado hablar, que imprime una cadena con el ladrido del perro
    def hablar(self):
        print("El perro", self.nombre, "de raza", self.raza, "ladra.")

# Creamos un objeto de la clase Animal y lo almacenamos en la variable animal1
animal1 = Animal("Gato")

animal1.hablar()

perro1 = Perro("Fido", "Labrador")

perro1.hablar()
