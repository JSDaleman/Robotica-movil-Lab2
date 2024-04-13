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

# Definir el sensor de ultrasonido conectado al puerto 3
ultrasonic_sensor = lego_sensor.UltrasonicSensor('in3')

# Definir el tipo de llanta usado
llanta = EV3EducationSetTire()

# Establecer la velocidad de los motores
motor_b.speed_sp = 0
motor_c.speed_sp = 0



def move_distance(speed_percentage):
    # Definir la velocidad máxima del motor (en grados por segundo)
    MAX_SPEED = motor_b.max_speed

    # Calcular la velocidad a la que se moverán los motores
    speed = MAX_SPEED * speed_percentage / 100

    
    # Inicializar la distancia inicial
    initial_distance = ultrasonic_sensor.distance_centimeters

    print("Distancia inicial:", initial_distance, "cm")
    #print("Posicion encoders",  motor_b.position, motor_c.position )
    
    # Calcular la distancia recorrida en centímetros
    distancia_recorrida_cm1 = (llanta.circumference_mm * (motor_b.position / 360)) / 10
    distancia_recorrida_cm2 = (llanta.circumference_mm * (motor_c.position / 360)) / 10

    print("Distancia inicial encoder1:", distancia_recorrida_cm1, "cm")
    print("Distancia inicial encoder2:", distancia_recorrida_cm2, "cm")

    # Mover los motores hasta que la distancia medida sea mayor o igual a la distancia inicial más 100 cm
    while True:
        motor_b.run_forever(speed_sp=speed)
        motor_c.run_forever(speed_sp=speed)

        current_distance = ultrasonic_sensor.distance_centimeters

        # Si la distancia medida es menor o igual a la distancia inicial - 100 cm, detener los motores
        if current_distance <= initial_distance - 100:
            break

    # Detener los motores
    motor_b.stop()
    motor_c.stop()

    # Leer la distancia final desde el sensor de ultrasonido
    final_distance = ultrasonic_sensor.distance_centimeters

    print("Distancia final:", final_distance, "cm")
    #print("Posicion encoders",  motor_b.position, motor_c.position)

    # Calcular la distancia recorrida en centímetros
    distancia_recorrida_cm1 = (llanta.circumference_mm * (motor_b.position / 360)) / 10
    distancia_recorrida_cm2 = (llanta.circumference_mm * (motor_c.position / 360)) / 10

    print("Distancia final encoder1:", distancia_recorrida_cm1, "cm")
    print("Distancia final encoder2:", distancia_recorrida_cm2, "cm")



def main():

    print("Iniciando prueba de sensor de ultra sonido")
    # Solicitar al usuario la velocidad deseada
    speed_option = input("Ingrese '30' para el 30%% de la velocidad maxima, o '100' para el 100%: ")

    if speed_option == '30':
        speed_percentage = 30
    elif speed_option == '100':
        speed_percentage = 100
    else:
        print("Opcion invalida. Saliendo del programa.")
        sys.exit(1)

    # Mover el robot con la velocidad especificada
    move_distance(speed_percentage)

if __name__ == "__main__":
    main()
