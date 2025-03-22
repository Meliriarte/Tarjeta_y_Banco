class TarjetaCredito:
    def __init__(self, numero_tarjeta, saldo_pendiente=0):
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente

    @staticmethod
    def validar_tarjeta(numero):
        numero = list(numero)
        numero.reverse()
        digitos = [int(d) for d in numero]

        for i in range(len(digitos)):
            if i % 2 == 1:
                digitos[i] = digitos[i] * 2
                if digitos[i] > 9:
                    digitos[i] = digitos[i] - 9

        suma_total = sum(digitos)

        if suma_total % 10 == 0:
            return True
        else:
            return False

    def consultar_saldo_pendiente(self):
        return self.saldo_pendiente

    def pagar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo_pendiente:
            self.saldo_pendiente -= cantidad
            print(f"Pago realizado. Nuevo saldo pendiente: {self.saldo_pendiente}")
        else:
            print("Cantidad de pago inválida o insuficiente saldo pendiente.")


class CuentaBancaria:
    def __init__(self, titular, numero_tarjeta, saldo_inicial=0):
        self.__saldo = saldo_inicial
        self.__titular = titular
        self.tarjeta = TarjetaCredito(numero_tarjeta)

    def depositar(self, cantidad):
        if self.tarjeta.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito realizado. Nuevo saldo: {self.__saldo}")
            else:
                print("La cantidad a depositar debe ser positiva.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")

    def retirar(self, cantidad):
        if self.tarjeta.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0 and cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro realizado. Nuevo saldo: {self.__saldo}")
            else:
                print("Cantidad inválida o saldo insuficiente.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular

    def realizar_pago_tarjeta(self, cantidad):
        if self.tarjeta.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0 and cantidad <= self.__saldo:
                self.__saldo -= cantidad
                self.tarjeta.pagar(cantidad)
                print(f"Pago realizado. Nuevo saldo en cuenta: {self.__saldo}")
            else:
                print("Cantidad inválida o saldo insuficiente.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")


# Ejemplo
if __name__ == "__main__":
    # Tarjeta valida
    cuenta = CuentaBancaria("Juan Pérez", "4532015112830366", 1000)
    cuenta.tarjeta.saldo_pendiente = 500 

    # Saldos
    print(f"Saldo en cuenta: {cuenta.consultar_saldo()}")
    print(f"Saldo pendiente en tarjeta: {cuenta.tarjeta.consultar_saldo_pendiente()}")

    # Operaciones
    cuenta.depositar(200)
    cuenta.retirar(100)
    cuenta.realizar_pago_tarjeta(300)

    # Tarjeta inválida
    cuenta_invalida = CuentaBancaria("Ana Gómez", "1234567890123456", 500)
    cuenta_invalida.depositar(100) 