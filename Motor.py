class Motor:

    def __init__(self, tipo: str, potencia: int):
        self._tipo= tipo
        self._potencia= potencia

    # Propiedad para tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    # Propiedad potencia
    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, nueva_potencia):
        self._potencia = nueva_potencia

    def encender_motor(self):
        return f"El motor {self._tipo} está encendido."

    def detener_motor(self):
        return f"El motor {self._tipo} está apagado."

    # Representación
    def __str__(self):
        return f"Motor(tipo={self._tipo}, potencia={self._potencia}HP)"

if __name__ == '__main__':
        objMotor = Motor(tipo= 'Diesel' , potencia= 180 )

        print(objMotor)
        print('*'.center(20, '*'))
        print(f'tipo: {objMotor.tipo}')
        print(f'potencia: {objMotor.potencia}')
