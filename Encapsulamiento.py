class CuentaBancaria:
    
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("No hay suficiente saldo en la cuenta.")
        else:
            self.saldo -= monto

    def consultar_saldo(self):
        print("El saldo de la cuenta es:", self.saldo)

# Creamos una instancia de la clase CuentaBancaria y la almacenamos en la variable cuenta1
cuenta1 = CuentaBancaria("Juan Perez", 12345, 5000)

# Intentamos acceder directamente al atributo privado saldo de la instancia cuenta1
print(cuenta1.saldo)

# Sin embargo, podemos acceder al atributo privado saldo mediante un método público
cuenta1.consultar_saldo()

# Modificamos el atributo privado saldo mediante un método público
cuenta1.retirar(1000)

# Verificamos que se haya modificado el atributo privado saldo correctamente
cuenta1.consultar_saldo()
