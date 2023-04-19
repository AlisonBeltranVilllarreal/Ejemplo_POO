class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

class Vaca(Animal):
    def hablar(self):
        return "Muu!"

# Creamos instancias de las clases Perro, Gato y Vaca
perro = Perro("Toby")
gato = Gato("Garfield")
vaca = Vaca("Margarita")

# Creamos una lista de animales
animales = [perro, gato, vaca]

# Iteramos sobre la lista de animales e invocamos el método hablar de cada uno, que se ha implementado de forma diferente en cada subclase
for animal in animales:
    print(animal.nombre + ": " + animal.hablar())
