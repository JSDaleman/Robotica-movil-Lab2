# Robotica-movil-Lab2
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya

Tabla de Contenidos
---
- [¿Qué es ROS?](#qué-es-ros)
- [ Comandos para rosnode, rostopic, rosservice,rosmsg, rospack](#comandos-para-rosnode-rostopic-rosservice-rosmsg-rospack)
- [¿Qué hacen los programas de python?](#qué-hacen-los-programas-de-python)
- [Plano donde el Turtlesim puede moverse](#plano-donde-el-turtlesim-puede-moverse)
- [Como usar algún servicio en Python](#como-usar-algún-servicio-en-python).
- [Servicio spawn](#servicio-spawn).
- [Incertidumbre en sensores](#incertidumbre-en-sensores)
- [Otros links de interes](#Otros-links-de-interes).
- [Referencias](#Referencias) 

## ¿Qué es ROS? 

ROS es un meta sistema operativo de código abierto para tu robot. Provee de servicios que se esperarían de un sistema operativo, incluyendo abstracción de hardware, control de dispositivos de bajo nivel, implementación de funcionalidades comunes, pasaje de mensaje entre procesos y manejo de paquetes. También brinda herramientas y librerías para obtener, construir, escribir y correr código a través y mediante varias computadoras. ROS es similar a otras estructuras o armazones para robot como Player, YARP, Orocos, CARMEN, Orca, MOOS, y Microsoft Robotics Studio. [1]

Al ser un sistema muy versartil al tener una contruccion modular permite una alta adaptabilidad a los diferentes proyectos que se desarrollen, por su ampllio uso ROS cuenta con una comunidad muy amplia dando un alto acceso a diferentes bibliotecas, paketes, documentacion y soporte para diferentes problemas. Por la alta disponibilidad de librerias y paquetes se puede hacer un facil reuso de codigo lo que permite hacer dasarrollos más rapidamente además de poseer diversas herramientas para visualizar y depurar el comportamiento de los robots en tiempo real, lo que facilita el desarrollo y la depuración de aplicaciones robóticas complejas. Poir ultimo su comtabilidad con diferentes sistemas operativos permite su manejo en sistemas linux, masOS y windows.

## Comandos para rosnode, rostopic, rosservice, rosmsg, rospack

### rosnode
  * rosnode ping Permite probar la conectividad al nodo.
  * rosnode list Muesta la lista de nodos activos.
  * rosnode info Imprime la información del nodo.
  * rosnode machine Muesta la lista de nodos activos en la maquina.
  * rosnode kill Termina el proceso de un nodo activo.

### rostopic
  * rostopic bw Muestra el ancho de banda usado por el topico.
  * rostopic echo Imprime mensaje en la pantalla.
  * rostopic find Busca un topico por su tema.
  * rostopic hz Muestra la tasa de publicación del tema.
  * rostopic info Imprime información sobre un tema activo.
  * rostopic list Muesta la lista de todos los temas publicados.
  * rostopic pub Publica la información al tema.
  * rostopic type Imprime el tipo del tema.

### rosservice
  * rosservice list Imprime informacion sobre el servicio activo.
  * rosservice node Imprime el nombre del nodo proveniente de un servicio.
  * rosservice call Llama el servicio con los argumentos dados.
  * rosservice args Muesta la lista de argumentos de un servicio.
  * rosservice type Imprime el tipo del servicio.
  * rosservice uri Imprime el servico ROSRPC uri.
  * rosservice find Busca el servicio por el tipo de servicio.

### rossmsg
  * rosmsg show Muestra los campos en el msg/srv.
  * rosmsg list Muestra los nombres de todos los msg/srv. 
  * rosmsg md5 Muestra el msg/srv md5 sum. 
  * rosmsg package Muestra la lista de todos los msg/srv en un paquete.
  * rosmsg packages Muestra la lista de todos los paquetes que contienen el msg/srv.


### rospack
  * rospack Busca y recupera la informacion sobre los paquetes.
  * catkin_create_pkg Crea un nuevo paquete.
  * catkin_make Construyeun espacio de trabajo de paquetes.
  * rosdep Instala dependencias del sistema de un paquete.
  * rqt En un rqt existe una extencion llamada "Introspection/Package Graph", la cual visualiza las dependencias de paquetes como un grafico.

## ¿Qué hacen los programas de python?

### Programa #1: Publicador de velocidades para turtlesim (pypubvel.py)
Este programa Python esta pensado para ir publicando comandos de velocidad angular y lineal aleatorios en un robot simulado del turtlesim. Utiliza ROS para interactuar con el sistema de control del robot.

[pypubvel.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20A/pypubvel.py)

Funciones de ROS utilizadas:
rospy.init_node(): Inicializa un nodo ROS.
rospy.Publisher(): Crea un publicador en un determinado tema con un tipo de mensaje específico.
rospy.Rate(): Crea un objeto que permite dormir el tiempo necesario para alcanzar una cierta frecuencia.
Creación del publicador y configuración del nodo: Se crea un publicador en el tema "turtle1/cmd_vel" con el tipo de mensaje Twist. También se inicializa el nodo ROS.

Bucle principal: Se establece un bucle principal que se ejecuta mientras el nodo no se haya apagado.

Funciones de ROS utilizadas:
rospy.is_shutdown(): Verifica si el nodo ROS ha sido apagado.
Generación de un mensaje Twist aleatorio: En cada iteración del bucle, se crea un nuevo mensaje Twist con valores aleatorios para la velocidad lineal y angular.

Registro de información y publicación del mensaje: Se registra la información del mensaje generado y se publica en el tema especificado.

Funciones de ROS utilizadas:
rospy.loginfo(): Registra un mensaje informativo en el registro de ROS.
pub.publish(): Publica un mensaje en el tema especificado.
Espera para cumplir con la frecuencia deseada: Después de publicar el mensaje, el programa espera el tiempo necesario para cumplir con la frecuencia especificada.


### Programa #2: Subcripción a tema turtle1/pose (pysubpose.py)

Con este programa de Python se genera la subspricion a los mensajes de posición del robot simulado con turtlesim, y al mismo tiempo buscamos registrar esta información.

[pysubpose.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20A/pysubpose.py)

Funciones de ROS utilizadas:
rospy.init_node(): Inicializa un nodo ROS.
rospy.Subscriber(): Crea un suscriptor que escucha un determinado tema y llama a una función de devolución de llamada cuando se recibe un mensaje.
rospy.spin(): Mantiene el nodo en funcionamiento hasta que se apague explícitamente.
Definición de la función de devolución de llamada: Se define una función poseMessageReceived() que se ejecutará cada vez que se reciba un mensaje en el tema "turtle1/pose". Esta función simplemente registra la posición y dirección del mensaje recibido.
rospy.loginfo(): Registra un mensaje informativo en el registro de ROS.
Configuración del nodo y suscripción al tema: Se inicializa el nodo ROS y se configura un suscriptor en el tema "turtle1/pose" para que llame a la función de devolución de llamada poseMessageReceived() cada vez que recibe un mensaje en ese tema.
rospy.init_node(): Inicializa un nodo ROS.
rospy.Subscriber(): Crea un suscriptor que escucha un determinado tema y llama a una función de devolución de llamada cuando se recibe un mensaje.
Mantenimiento del nodo en funcionamiento: Se llama a rospy.spin() para mantener el nodo en funcionamiento y esperar la llegada de mensajes.
rospy.spin(): Mantiene el nodo en funcionamiento hasta que se apague explícitamente.

Para resunmir, el programa #1 controla la generación y publicación de comandos de velocidad aleatorios para el robot simulado, mientras que el programa #2 genera la subscripcion a los mensajes de posición del mismo robot y registra esta información. Ambos programas utilizan ROS para interactuar con el sistema de control del robot y facilitar la comunicación entre los diferentes componentes del sistema.


## Plano donde el Turtlesim puede moverse
Corriendo el pysubpose.py y con el turtle_teleop_key se encontraron los datos mostrados a continuación 
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/d386a914-7b25-47e9-9fd8-7e220912cbe8)
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/a5f749b7-8082-4ff5-bb86-64f4a6968c34)
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/c7cd4cc5-0ab2-46c9-8bb0-3b38c2ed4eec)
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/4f352c8a-a07c-4ddd-945e-edcd4f0fe362)
el plano de movimiento de la tortuga según los datos recogidos es de dimenciones 11.088889122009277 x 11.088889122009277 en donde puede moverse desde la coordenada (0, 0) hasta la coordenada (11.088889122009277, 11.088889122009277)


## Como usar algún servicio en Python

Los servicios ROS están definidos por archivos srv, que contienen un mensaje de solicitud y un mensaje de respuesta, rospy convierte estos archivos srv en código fuente Python y crea tres clases: definiciones de servicios, mensajes de solicitud y mensajes de respuesta.

Supongamos que se tiene un servicio llamado add_two_ints que toma dos números enteros como entrada y devuelve su suma como salida. Aquí hay un ejemplo paso a paso de cómo usar este servicio en Python:

1. Importar los módulos necesarios:
```
import rospy
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import String
```
2. Iniciar el nodo ROS:
```
rospy.init_node('service_client_node')
```
3. Esperar a que el servicio esté disponible:
```
rospy.wait_for_service('add_two_ints')
```
4. Crear un objeto de servicio que llame al servicio deseado:
```
add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
```
5.Llamar al servicio con los argumentos necesarios:
```
# Forma explicita
req = rospy_tutorials.srv.AddTwoIntsRequest(1, 2)
resp = add_two_ints(req)
# Forma implicita con argumentos en orden
resp = add_two_ints(1, 2)
# Forma implicita con argumentos de palabras clave
resp = add_two_ints(a=1)
```
6. Procesar la respuesta:
```
print("La suma de dos enteros es:", response.sum)

```
7. Cerrar el servicio:
```
# Detener explícitamente un servicio:
s.shutdown('shutdown reason')
# Esperar a que se apague:
s.spin()
```
## Servicio spawn

Se usara el servicio Spawm para hacer para aparecer otra tortuga y realice un programa en Python que haga que las tortugas dibujen un triángulo y un cuadrado.

1. Iniciar el nucleo principal de ROS:
```
roscore
```
2. Crear los archivos:

   El primer archivo, CT.py es el archivo de Python encargado de dibujar el cuadrado y triángulo con cada una de las tortugas.
   [ CT.py][(https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20A/CT.py)
  

   Segundo archivo, es el launch para ejecutar todas las tareas.
   [CT.launch](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20A/CT.launch)
  
3. Ejecución
   
   En la consola se ejecuntan los siguientes comandos:
   ```
   roslaunch pruebas CT.launch
   ```
   Para aparecer otra tortuga
   ```
   rosservice call /spawn 4 5 0 turtle2
   ```

   Resultados:

   
 ![Resultado](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/83f2dcec-3f68-4caa-973c-f2fb6356e63e)



## Conexión Lego EV3 con ROS

### Preparación de entorno e intalacion de librerias y paquetes

#### Creacion del workspace

Para esto crearemos un directrotio que sera nuestro workspace y tendra nuestros archivos de intalación

```
cd ~
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin build
cd src
catkin_create_pkg ev3dev_ros
```

#### Intalacion de libreria de python

Para la instalacion de la libreria en python descargaremos los archivos necesarios y haremos la instalcion con los siguientes comandos

```
cd ~/catkin_ws/src/ev3dev_ros/
git clone https://github.com/ev3dev/ev3dev-lang-python.git
cd ~/catkin_ws/src/ev3dev_ros/ev3dev-lang-python
sudo python3 setup.py install
```

#### Intalacion de libreria C++

Para la instalacion de la libreria en C++ descargaremos los archivos necesarios y haremos la instalcion con los siguientes comandos

```
cd ~/catkin_ws/src/ev3dev_ros/
git clone https://github.com/ddemidov/ev3dev-lang-cpp.git
cd ~/catkin_ws/src/ev3dev_ros/ev3dev-lang-cpp
mkdir build
cd build
cmake ..
sudo make install
```

### Creación de SD booteable con ev3dev
Para poder conectar el lego EV3 con ROS primero se necesita tener una memoria SD de minimo 2 GB de alamacenamiento y una antena USB wifi para el robot EV3. Para elegir una SD compatible y un adaptador wifi se recomienda leer las siguientes paginas:
* [Seleccion de SD](https://github.com/ev3dev/ev3dev/wiki/Selecting-a-microSD-card)
* [Antenas wifi compatibles leJos](https://lejosnews.wordpress.com/2015/02/03/comparing-wifi-adapters/).
* [Antena wifi compatibles con ev3dev](https://github.com/ev3dev/ev3dev/wiki/USB-Wi-Fi-Dongles)

  Para acceder a la programación del robot EV3 por una API diferente a la de lego usamos un booteo de una distribución de Linux Debian desarrollada para el robot conocido como [ev3dev](https://www.ev3dev.org/) este fue desarrollado para el uso de diferentes lenguajes de programación con el robot ev3 como python, micropython, java, C++, C y etc. (Para conocer todos los lenguajes disponibles ver [lenguajes de programación](https://www.ev3dev.org/docs/programming-languages/)).

  **Nota:** Acabe aclarar que este es un booteo por una unidad de almacenamiento diferente por lo cual no se afecta o modifica el firmware original que posee el bloque ev3.
  
  Para crear la SD booteable se siguieron los pasos de la pagina de ev3dev [SD booteable](https://www.ev3dev.org/docs/getting-started/). Una vez con la antena colocada en el robot y la SD se prende este y se espera que se inicialice el sistema.

### Conexión al PC via wifi
Para esta conexión se puede hacer por dos vias la primera es configurar manualmente la red wifi a la cual se conectara o configurandola por medio del pc por conexión [bluethoot](https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/) o [USB](https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/). Una vez configurada nos podremos conectar al robot atravez de esta en el PC usando una conexión [SSH](https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/).Para esto lanzaremos una terminal y mandaremos el siguente comando

```
ssh robot@<Dirección IP del robot>
```
**Nota:** La dirrección IP asignada al robot se puede ver en la parte superior a la izquierda del robot y el password es "maker" se puede usar tambien el comado ```ssh robot@ev3dev.local ``` pero al habero otros robots conectados o por configuración DNS de la red wifi puede generar algún error.

#### Pruebas de motores
Si desea probar el funcionamiento de motores por el terminal puede conectar los motores en los puestos B y C del robot y corra el siguente comando el cual movera las dos ruedas con una velocidad de 50 grados/s sin frenado premero la del motor conectado al puerto C y luego la del motor conectado al puerto C.

* Prueba movimiento de cada motor
```
python3 -c "from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C; LargeMotor(OUTPUT_B).on_for_seconds(speed=50, seconds=2); LargeMotor(OUTPUT_C).on_for_seconds(speed=50, seconds=2)"
```
* Prueba con frenadao
```
python3 -c "from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank; tank_drive = MoveTank(OUTPUT_B, OUTPUT_C); tank_drive.on_for_seconds(left_speed=50, right_speed=50, seconds=5, brake=True)"
```

* Giro del robot
```
python3 -c "from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank; tank_drive = MoveTank(OUTPUT_B, OUTPUT_C); tank_drive.on_for_seconds(left_speed=50, right_speed=45, seconds=5, brake=True)"
```
* Frenado suave
```
python3 -c "from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank; tank_drive = MoveTank(OUTPUT_B, OUTPUT_C); tank_drive.on_for_seconds(left_speed=50, right_speed=45, seconds=5); tank_drive.off(brake=True)"

```


#### Scripts de prueba con python
En la terminal del robot vamos a crear los directorios de trabajo para nuestros scripts de python con los siguentes comandos

```
cd ~
mkdir pruebas
cd pruebas/
mkdir python
cd python/
mkdir Mov
cd Mov
```

ahora en crearemos el scritp inicial el cual lo que hara es que cambiara los leds de color y movera en los dos motores con velocidad del 75% por 5 rotaciones

[pythonHello.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Mov/pythonHello.py)

copiaremos el archivo en el directorio del robot 

```
scp pythonHello.py robot@<Dirección IP del robot>:/home/robot/pruebas/python/Mov/
```

Para correr el script en la terminar del robot le daremos los permisos necesarios al archivo y lo correremos
```
cd ~/pruebas/python/Mov/
chmod +x pythonHello.py
python3 pythonHello.py
```
Otro script que se puede usar para hacer pruebas es el siguiente para una trayectoria de un cuadrado
[Cuadrado.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Mov/Cuadrado.py)

o se puede tambien probar el del poryecto de ev3dev PS4Explor3r para control remoto con un control de PS4

[PS4Explor3r](https://www.ev3dev.org/projects/2018/09/02/PS4Explor3r/)


### Pruebas de funcionamiento

## Incertidumbre en sensores

### Lidar

### Ultrasonido HC-SR04

###  Sensores Lego

#### Desplazamineto
* Encoder sensor de rueda.
* Sensor de Ultrasonido del EV3.

** Nota ** Si en la red wifi se detecta correctamente el robot puede usara ev3dev.local en vez de la dirección IP

#### Giro de la rueda
Para hacer la medición con un medio externo se uso un transportador de 360° con una estructura en lego mostrada a continuación.

![Imagen de WhatsApp 2024-04-12 a las 13 55 23_59aae77c](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/0eea2e30-2691-4768-bbc7-1d8075c36262)
![Imagen de WhatsApp 2024-04-12 a las 13 55 22_03e7eb2c](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/c5a7549c-ccb0-4f42-8105-ea8fb35fb596)
![Imagen de WhatsApp 2024-04-12 a las 13 55 22_a3575e64](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/d108d465-82e3-438b-bb3c-9135ff404477)
![Imagen de WhatsApp 2024-04-12 a las 13 55 23_fa8bc017](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/c13b7282-47cf-4817-b429-d3ab1457ed04)

Asimismo se creo el siguente script el cual solicita al usuario cuanto sera el valor de intervalo de cada movimiento de la ruda para dar la vuelta y el puerto del motor que se hara girar haciendo una pausa en cada intervalo para que el usuario pueda hacer la medicón externa y luego indique que se realice el siguente movimiento.

[GiroRueda.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Incertidumbre/GiroRueda.py)

luego este script se copio al robot con el comando mostrado a continuación

```
scp GirtoRueda.py robot@<Dirección IP del robot>:/home/robot/pruebas/python/Incertidumbre/
```

luego en la terminal donde esta corriendo la conexión ssh se corrio el script

```
cd ~/pruebas/python/Incertidumbre/
chmod +x GirtoRueda.py
python3 GirtoRueda.py
```


Las mediciónes se registrarón en el siguiente excel para procesar la información

[Excel de mediciones](https://unaledu-my.sharepoint.com/:x:/g/personal/jdaleman_unal_edu_co/Ed-b2T2l6-hNlDRAIFZ_NJcBvsgojICqpPVucmziBNNi9A)




## Otros links de interes
* [Conexion de Lego Ev3 por medio de una raspberry pi](https://github.com/aws-samples/aws-builders-fair-projects/blob/master/reinvent-2019/lego-ev3-raspberry-pi-robot/README.MD) 
* [ROS desde el Lego Ev3](https://github.com/moriarty/ros-ev3)
* [Manaje con python ev3dev](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/latest/)
* [Manejo de motores del Ev3 con Python](https://www.youtube.com/watch?v=j0-ATIe6pqg) 
* [Uso de sensor lidar con Ev3](https://www.youtube.com/watch?v=JX0zeYa-faM) 
* [Programacion y conexion SSH desde Visual Studio Code con Ev3](https://www.youtube.com/watch?v=uNSIOvqzAnY) 
* [Instalacion de ROS distribucion JADE en el Ev3](https://github.com/osmado/ev3dev_ros_distribution) 
* [ROS blog sobre lego Ev3](http://wiki.ros.org/Robots/EV3)
* [Conexión Ev3 y arduino](https://www.dexterindustries.com/howto/connecting-ev3-arduino/)
* [Manejo con ROS de Ev3 con C++](https://www.youtube.com/watch?v=iRQqEKYDRI4)
* [Github manejo con ROS de Ev3 con C++](https://github.com/srmanikandasriram/ev3-ros?tab=readme-ov-file)
* [Libreria de Python de ev3dev](https://github.com/ev3dev/ev3dev-lang-python)
* [Libreria de C++ de ev3dev](https://github.com/ddemidov/ev3dev-lang-cpp)

## Referencias 

[1] ROS Wiki, "ROS/Introducción," [En línea]. Disponible en: http://wiki.ros.org/es/ROS/Introduccion. [Accedido el: 31 03 2024].
