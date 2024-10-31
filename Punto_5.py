"""
5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
saldo encapsulado. 
De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue exitoso). 
Se debe crear la clase e implementarla.
"""

class Cuenta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo  
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto} exitoso.")
        else:
            print("El monto a depositar debe ser positivo.")
    
    def retirar(self, monto):
        if monto > 0:
            if monto <= self._saldo:
                self._saldo -= monto
                print(f"Retiro de ${monto} exitoso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("El monto a retirar debe ser positivo.")
    
    def obtener_saldo(self):
        return self._saldo


mi_cuenta = Cuenta_bancaria("Nicolas", 500)

print(f"Saldo actual: ${mi_cuenta.obtener_saldo()}")
mi_cuenta.depositar(200)       

print(f"Saldo después del depósito: ${mi_cuenta.obtener_saldo()}")
mi_cuenta.retirar(100)        

print(f"Saldo después del retiro: ${mi_cuenta.obtener_saldo()}")


