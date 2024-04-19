#!/usr/bin/env python3

from ev3dev2.sensor.lego import GyroSensor
from time import sleep

# Definir el objeto GyroSensor para el sensor conectado al puerto sensor1
gyro = GyroSensor()

# Mostrar el ángulo inicial del sensor
print("Angulo inicial:", gyro.angle)

# Leer el ángulo del sensor continuamente
while True:
    # Leer el ángulo actual del sensor
    angle = gyro.angle
    print("Angulo actual:", angle)
    
    # Esperar un breve periodo de tiempo antes de leer nuevamente
    sleep(0.5)
