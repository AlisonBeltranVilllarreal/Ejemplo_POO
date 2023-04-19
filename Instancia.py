# Definimos una clase llamada Persona
class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")

# Creamos una instancia de la clase Persona y la almacenamos en la variable persona1
persona1 = Persona("Juan", 30)
persona1.presentarse()

# Creamos otra instancia de la clase Persona y la almacenamos en la variable persona2
persona2 = Persona("Ana", 25)
persona2.presentarse()
