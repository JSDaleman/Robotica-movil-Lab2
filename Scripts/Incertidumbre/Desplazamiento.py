#!/usr/bin/env python3

import ev3dev2.motor as motor
import ev3dev2.sensor as sensor
import ev3dev2.sensor.lego as lego_sensor
from ev3dev2.wheel import EV3EducationSetTire
import sys


# Definir los motores conectados a los puertos B y C
motor_b = motor.LargeMotor('outB')
motor_c = motor.LargeMotor('outC')

#Posicion cero de los encoders
motor_b.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="hold")
motor_c.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="hold")

# Definir el tipo de llanta usado
llanta = EV3EducationSetTire()

# Definir el sensor de ultrasonido conectado al puerto 3
ultrasonic_sensor = lego_sensor.UltrasonicSensor('in3')

# Establecer la velocidad de los motores
motor_b.speed_sp = 0
motor_c.speed_sp = 0

def move_distance(distance, speed_percentage):
    # Definir la velocidad máxima del motor (en grados por segundo)
    MAX_SPEED = motor_b.max_speed

    # Calcular la velocidad a la que se moverán los motores
    speed = MAX_SPEED * speed_percentage / 100

    # Establecer la velocidad de los motores
    motor_b.speed_sp = 0
    motor_c.speed_sp = 0

    # Leer la distancia inicial desde el sensor de ultrasonido
    initial_distance = ultrasonic_sensor.distance_centimeters
    print("Distancia inicial:", initial_distance, "cm")

    # Calcular la distancia recorrida en centímetros
    distancia_recorrida_cm1 = (llanta.circumference_mm * (motor_b.position / 360)) / 10
    distancia_recorrida_cm2 = (llanta.circumference_mm * (motor_c.position / 360)) / 10

    print("Distancia inicial encoder1:", distancia_recorrida_cm1, "cm")
    print("Distancia inicial encoder2:", distancia_recorrida_cm2, "cm")

    # Calcular la cantidad de grados necesarios para recorrer la distancia
    degrees = (distance / llanta.circumference_mm) * 360  

    # Mover los motores la cantidad de grados calculada
    motor_b.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action="hold")
    motor_c.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action="hold")

    # Esperar a que los motores terminen de moverse
    motor_b.wait_while('running')
    motor_c.wait_while('running')

        # Leer la distancia final desde el sensor de ultrasonido
    final_distance = ultrasonic_sensor.distance_centimeters
    
    print("Distancia final:", final_distance, "cm")
    
    # Calcular la distancia recorrida en centímetros
    #print("Posicion encoders",  motor_b.position, motor_c.position )

    distancia_recorrida_cm1 = (llanta.circumference_mm * (motor_b.position / 360)) / 10
    distancia_recorrida_cm2 = (llanta.circumference_mm * (motor_c.position / 360)) / 10

    print("Distancia final encoder1:", distancia_recorrida_cm1, "cm")
    print("Distancia final encoder2:", distancia_recorrida_cm2, "cm")

def main():
    

    # Solicitar al usuario la velocidad deseada
    speed_option = input("Ingrese '30' para el 30% de la velocidad maxima, o '100' para el 100%: ")

    if speed_option == '30':
        speed_percentage = 30
    elif speed_option == '100':
        speed_percentage = 100
    else:
        print("Opcian invalida. Saliendo del programa.")
        sys.exit(1)

    # Mover el robot 1000 mm con la velocidad especificada
    move_distance(1000, speed_percentage)
    

if __name__ == "__main__":
    main()
