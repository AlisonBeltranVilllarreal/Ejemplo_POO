from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        print(f"Conduciendo el coche {self.marca} {self.modelo} de color {self.color}")

class Moto(Vehiculo):
    def conducir(self):
        print(f"Conduciendo la moto {self.marca} {self.modelo} de color {self.color}")

# No se puede crear una instancia de la clase Vehiculo, ya que es una clase abstracta
# vehiculo = Vehiculo("Ford", "Mustang", "Rojo")

# Podemos crear instancias de las clases Coche y Moto, que heredan de Vehiculo
coche = Coche("Ford", "Mustang", "Rojo")
moto = Moto("Harley Davidson", "Sportster", "Negro")

# Podemos llamar al método conducir de cada instancia de Vehiculo, que se ha implementado de forma diferente en cada subclase
coche.conducir()
moto.conducir()
