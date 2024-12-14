class CuentaBancaria:

    def __init__(self, titular, saldo):
        #Inicializa la cuenta bancaria con el titular y el saldo inicial.

        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        #Agrega dinero al saldo de la cuenta, siempre que el monto sea positivo.

        if monto > 0:
            self.__saldo += monto
            print(f"Se han depositado {monto}. Saldo actual: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        #Resta dinero del saldo de la cuenta, siempre que haya suficientes fondos.

        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se han retirado {monto}. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        #Devuelve el saldo actual de la cuenta.

        return self.__saldo

# Uso de encapsulación
cuenta = CuentaBancaria("Carlos", 1000)  # Crear una cuenta bancaria con un saldo inicial de 1000
cuenta.depositar(500)  # Depositar 500
cuenta.retirar(300)  # Retirar 300
print("Saldo disponible:", cuenta.consultar_saldo())  # Consultar el saldo
