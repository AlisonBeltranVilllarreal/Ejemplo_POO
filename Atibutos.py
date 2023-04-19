class Persona:
    # Atributos
    nombre = ""
    edad = 0
    
    # Métodos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")
        
    # Eventos
    def cumple_anos(self):
        self.edad += 1
        print(f"Feliz cumpleaños, {self.nombre}!")
    
    # Mensajes
    def presentarse(self):
        self.hablar(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
    
    # Relaciones
    def conocer(self, otra_persona):
        self.hablar(f"Mucho gusto, {otra_persona.nombre}.")
        
    # Estado
    def cambiar_nombre(self, nuevo_nombre):
        self.hablar(f"Mi nombre ha sido cambiado de {self.nombre} a {nuevo_nombre}.")
        self.nombre = nuevo_nombre
