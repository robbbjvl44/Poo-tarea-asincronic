from Vehi import Vehi
from Motor import Motor

class Motocicleta(Vehi):

    def __init__(self, marca, modelo, anio, cilindraje: int, motor: Motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self.motor = motor

    # Propiedad para cilindraje
    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        self._cilindraje = nuevo_cilindraje

    # Métodos de comportamiento
    def caballito(self):
        return "La motocicleta está realizando una maniobra."

    def usar_arranque(self):
        return "La motocicleta está arrancando."

    # Representación
    def __str__(self):
        return f"Motocicleta({super().__str__()}, cilindraje={self._cilindraje}cc, motor={self.motor})"


if __name__ == '__main__':
        # MOTO 1
        motor1 = Motor(tipo='Gasolina', potencia=80)
        moto1 = Motocicleta('Yamaha', 'FZ', 2022, 150, motor1)

        print(moto1)
        print('*'.center(25, '*'))
        print(moto1.encender())
        print(moto1.caballito())
        print(moto1.usar_arranque())

        print('\n')

        # MOTO2
        motor2 = Motor(tipo='Gasolina', potencia=100)
        moto2 = Motocicleta('Honda', 'CBR', 2023, 250, motor2)

        print(moto2)
        print('*'.center(25, '*'))
        print(moto2.encender())
        print(moto2.caballito())
        print(moto2.usar_arranque())
