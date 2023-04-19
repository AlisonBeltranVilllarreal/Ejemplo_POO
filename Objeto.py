# Definimos una clase llamada Persona
class Persona:
    
    # Definimos el constructor de la clase con tres parámetros: nombre, edad y altura
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    # Definimos un método llamado presentarse, que imprime una cadena con información de la persona
    def presentarse(self):
        print("Hola, mi nombre es", self.nombre, "tengo", self.edad, "años y mido", self.altura, "metros.")

# Creamos un objeto de la clase Persona y lo almacenamos en la variable persona1
persona1 = Persona("Juan", 30, 1.75)

# Llamamos al método presentarse del objeto persona1
persona1.presentarse()