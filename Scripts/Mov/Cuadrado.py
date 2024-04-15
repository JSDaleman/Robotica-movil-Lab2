from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor
import time

# Constantes
LADO = 30  # Longitud del lado del cuadrado en centímetros
SPEED = SpeedPercent(30)

# Función para girar 90 grados
def girar_90_grados(tank):
    tank.turn_degrees(90, speed=SPEED)

# Función para moverse hacia adelante
def moverse_adelante(tank):
    tank.on_for_seconds(SPEED, SPEED, 3)  # Moverse hacia adelante durante 3 segundos

# Inicializar objetos del motor y el giroscopio
tank = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()

# Calibrar el giroscopio
gyro.calibrate()

# Esperar a que el giroscopio se calibre completamente
while gyro.calibrating:
    time.sleep(0.1)

# Recorrer el cuadrado
for _ in range(4):
    moverse_adelante(tank)  # Moverse hacia adelante (lado del cuadrado)
    girar_90_grados(tank)   # Girar 90 grados

# Detener los motores al final
tank.stop()
