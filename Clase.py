# Se define la clase CuentaBancaria
class CuentaBancaria:
    
    # Se define el constructor de la clase
    def __init__(self, titular, numero, saldo):
        # Se asignan los valores de los parámetros titular
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    # Se define un método llamado depositar que recibe un parámetro monto
    def depositar(self, monto):
        self.saldo += monto

    # Se define un método llamado retirar que recibe un parámetro monto
    def retirar(self, monto):
       
        if monto > self.saldo:
            print("No hay suficiente saldo en la cuenta.")
        else:
            self.saldo -= monto

    # Se define un método llamado consultar_saldo
    def consultar_saldo(self):

        print("El saldo de la cuenta es:", self.saldo)
