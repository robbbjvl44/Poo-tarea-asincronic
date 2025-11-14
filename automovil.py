from Vehi import Vehi
from Motor import Motor

class Automovil(Vehi):

    def __init__(self, marca, modelo, anio, numero_puertas: int, motor: Motor):
        super().__init__(marca, modelo, anio)
        self._numero_puertas = numero_puertas
        self.motor = motor

    @property
    def numero_puertas(self):
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, nuevas_puertas):
        self._numero_puertas = nuevas_puertas

    def abrir_maletero(self):
        return "El maletero está abierto."

    def tocar_claxon(self):
        return "El claxon ha sonado."

    # Representación
    def __str__(self):
        return f"Automovil({super().__str__()}, puertas={self._numero_puertas}, motor={self.motor})"


if __name__ == '__main__':
        # AUTO 1
        motor1 = Motor(tipo='Diesel', potencia=180)
        auto1 = Automovil('Toyota', 'Hilux', 2025, 4, motor1)

        print(auto1)
        print('*'.center(25, '*'))
        print(auto1.encender())
        print(auto1.tocar_claxon())
        print(auto1.abrir_maletero())

        print('\n')

        # AUTO 2
        motor2 = Motor(tipo='Gasolina', potencia=150)
        auto2 = Automovil('Ford', 'Focus', 2024, 4, motor2)

        print(auto2)
        print('*'.center(25, '*'))
        print(auto2.encender())
        print(auto2.tocar_claxon())
        print(auto2.abrir_maletero())