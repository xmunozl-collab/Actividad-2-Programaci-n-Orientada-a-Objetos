from enum import Enum


class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        # el saldo siempre empieza en cero
        self.saldo = 0

    def imprimir(self):
        print("Nombres del titular =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.name)
        print("Saldo =", self.saldo)

    def consultar_saldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        # no se puede retirar mas de lo que hay en la cuenta
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Se ha retirado ${valor} de la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser mayor que cero y no puede superar el saldo actual.")
            return False


def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()

    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.retirar(900000)
    cuenta.consultar_saldo()


if __name__ == "__main__":
    main()
