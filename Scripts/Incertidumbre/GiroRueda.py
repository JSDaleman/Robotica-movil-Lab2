#!/usr/bin/env python3

import ev3dev2.motor as motor
from ev3dev2.motor import SpeedPercent
import time
import sys

print("Inicializando ...")


# Definir los motores conectados a los puertos B y C
motor_b = motor.LargeMotor('outB')
motor_c = motor.LargeMotor('outC')


# Restablecer la posición inicial de los encoders a cero
motor_b.position = 0
motor_c.position = 0
motor_b.speed_sp = 0
motor_c.speed_sp = 0

# Definir la velocidad máxima del motor (en grados por segundo)
MAX_SPEED = motor_b.max_speed

def rotate_wheels(interval, motor_activ, direccion):
    # Calcular la cantidad de grados necesarios para completar una vuelta
    degrees_per_rotation = 360

    # Calcular la cantidad de intervalos necesarios para completar una vuelta
    intervals_per_rotation = int(degrees_per_rotation / interval)

    # Establecer la velocidad de los motores
    speed = 5
    motor_activ.position = 0
    ultimo_angulo = motor_activ.position

    # Girar las ruedas en intervalos hasta completar una vuelta
    for _ in range(intervals_per_rotation):
        motor_activ.on_for_degrees(speed = speed*direccion, degrees=interval, brake=False)
        
        # Pequeña pausa para permitir que el valor del encoder se actualice
        time.sleep(0.1)
        
        # Leer la última posición registrada del encoder
        ultimo_angulo = motor_activ.position * direccion
        print("La posicion del encoder es:", ultimo_angulo)
        input("Precione enter para la siguente medida")
    
    # Llevar el encoder a la posición 0
    motor_activ.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="hold")
    
    # Restablece la polaridad del codificador a 'normal'
    print("El encoder ha sido llevado a la posicion 0.")

def main():

    print("Inicio de programa para medicion de giro en las ruedas del robot ev3")
    # Solicitar al usuario el intervalo deseado
    interval_option = input("Ingrese '30' para intervalos de 30 grados, o '45' para intervalos de 45 grados: ")
    motor_option = input("Ingrese el motor a trabajar (B/C): ")

    if interval_option == '30':
        interval = 30
    elif interval_option == '45':
        interval = 45
    else:
        print("Opcion invalida. Saliendo del programa.")
        sys.exit(1)

    if motor_option == 'B':
        motor_activ = motor_b
        direccion = 1
    elif motor_option == 'C':
        motor_activ = motor_c
        direccion = -1
    else:
        print("Opcion invalida. Saliendo del programa.")
        sys.exit(1)
    # Girar las ruedas hasta completar una vuelta
    rotate_wheels(interval, motor_activ, direccion)
    print("Fin de la rutina")

if __name__ == "__main__":
    main()
