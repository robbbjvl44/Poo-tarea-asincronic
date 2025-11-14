class Vehi:

    def __init__(self, marca: str, modelo: str, anio: int):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    # Propiedad para marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca

    # Propiedad para modelo
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    # Propiedad para año
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        self._anio = nuevo_anio

    # Métodos de comportamiento
    def encender(self):
        return f"El vehículo {self._marca} {self._modelo} está encendido."

    def apagar(self):
        return f"El vehículo {self._marca} {self._modelo} está apagado."

    # Representación
    def __str__(self):
        return f"marca={self._marca}, modelo={self._modelo}, anio={self._anio}"


# ----------- PRUEBA INDIVIDUAL -----------
if __name__ == '__main__':

        # VEHÍCULO 1
        v1 = Vehi("Nissan", "Sentra", 2020)
        print(v1)
        print('*'.center(25, '*'))
        print(v1.encender())
        print(v1.apagar())

        print("\n")

        # VEHÍCULO 2
        v2 = Vehi("Chevrolet", "Sail", 2018)
        print(v2)
        print('*'.center(25, '*'))
        print(v2.encender())
        print(v2.apagar())