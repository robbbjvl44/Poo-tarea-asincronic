# Proyecto: Programación Orientada a Objetos en Python

Este proyecto implementa un sistema de vehículos utilizando Programación Orientada a Objetos (POO) con:
- Encapsulamiento mediante `@property` y `@setter`
- Herencia
- Composición
- Métodos de comportamiento
- Sobrescritura del método `__str__()`

El sistema simula Automóviles y Motocicletas, cada uno asociado a un Motor.

---

## Estructura del Proyecto

- Motor.py  
- Vehi.py  
- Automovil.py  
- Motocicleta.py  
- main.py  
- uml_diagrama.png  
- README.md  

---

## Descripción de las Clases

### 1. Motor
Clase usada por Automóvil y Motocicleta (composición).
- Atributos privados: tipo, potencia
- Métodos:
  - encender_motor()
  - detener_motor()
- Implementa `__str__()`  
- Usa @property y @setter

---

### 2. Vehi (Clase Padre)
Representa un vehículo general.
- Atributos privados: marca, modelo, anio
- Métodos:
  - encender()
  - apagar()
- Implementa `__str__()`

---

### 3. Automovil (Hereda de Vehi)
- Atributo adicional: número de puertas
- Contiene un Motor
- Métodos:
  - abrir_maletero()
  - tocar_claxon()
- Sobrescribe `__str__()`

---

### 4. Motocicleta (Hereda de Vehi)
- Atributo adicional: cilindraje
- Contiene un Motor
- Métodos:
  - caballito()
  - usar_arranque()
- Sobrescribe `__str__()`

---

## Ejecución del Programa

El archivo principal:
- Crea 2 automóviles
- Crea 2 motocicletas
- Les asigna motores
- Ejecuta métodos de comportamiento
- Imprime sus datos usando `__str__()`

---

