# Robotica-movil-Lab2
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya Castaño

Tabla de Contenidos
---
- [¿Qué es ROS?](#qué-es-ros)
- [ Comandos para rosnode, rostopic, rosservice,rosmsg, rospack](#comandos-para-rosnode-rostopic-rosservice-rosmsg-rospack).
- [¿Qué hacen los programas de python?](#qué-hacen-los-programas-de-python).
- [Plano donde el Turtlesim puede moverse](#plano-donde-el-turtlesim-puede-moverse).
- [Como usar algún servicio en Python](#como-usar-algún-servicio-en-python).
- [Servicio spawn](#servicio-spawn).
- [Conexión Lego EV3 con ROS](#conexi%C3%B3n-lego-ev3-con-ros).
  - [Preparación de entorno e intalacion de librerias y paquetes](#preparación-de-entorno-e-intalacion-de-librerias-y-paquetes).
    - [Creacion del workspace](#creacion-del-workspace).
    - [Instalacion de libreria de python](#instalacion-de-libreria-de-python).
  - [Creación de SD booteable con ev3dev](#creación-de-sd-booteable-con-ev3dev).
  - [Conexión al PC via wifi](#conexión-al-pc-via-wifi).
    - [Pruebas de motores](#pruebas-de-motores).
    - [Scripts de prueba con python](#scripts-de-prueba-con-python).
  - [Comunicación mqtt](#comunicación-mqtt).
  - [Implementación de la comunicación](#implementación-de-la-comunicación).
    - [Creación de broker y modificación de archivos](#creación-de-broker-y-modificación-de-archivos).
    - [Carga de archivos al robot](#carga-de-archivos-al-robot).
    - [Compilación del paquete](#compilación-del-paquete).
  - [Ejecución](#ejecucion).
  - [Conclusiones de la implementación](e#conclusiones-de-la-implementación).
- [Incertidumbre en sensores](#incertidumbre-en-sensores).
  - [Consulta bibliografica](#consulta-bibliográfica).
    - [¿ Qué es el Vocabulario Internacional de Metrología (VIM)?](#-qué-es-el-vocabulario-internacional-de-metrología-vim)
    - [Vocabulario según el VIM](#vocabulario-según-el-vim)
    - [Tipos de errores](#tipos-de-errores)
    - [Teoria estadistica](#tipos-de-errores)
  - [Sensores Lego](#sensores-lego).
    - [Desplazamineto](#desplazamineto).
    - [Giro de la rueda](#giro-de-la-rueda).
- [Otros links de interes](#Otros-links-de-interes).
- [Referencias](#Referencias).

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
mkdir ev3dev_ros
cd ev3dev_ros
mkdir src
cd src
catkin_create_pkg ev3dev_ros
```

#### Instalacion de libreria de python

Para la instalacion de la libreria en python descargaremos los archivos necesarios y haremos la instalcion con los siguientes comandos

```
cd ~
mkdir librerias
cd ~/librerias/
git clone https://github.com/ev3dev/ev3dev-lang-python.git
cd ~/librerias/ev3dev-lang-python
sudo python3 setup.py install
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

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/4514641b-869f-43b0-8adf-74ec17cf0142

* Prueba con frenado
```
python3 -c "from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank; tank_drive = MoveTank(OUTPUT_B, OUTPUT_C); tank_drive.on_for_seconds(left_speed=50, right_speed=50, seconds=5, brake=True)"
```

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/5100ec6d-13a1-4fb5-8574-61f7fa2af7d3

* Giro del robot
```
python3 -c "from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank; tank_drive = MoveTank(OUTPUT_B, OUTPUT_C); tank_drive.on_for_seconds(left_speed=50, right_speed=45, seconds=5, brake=True)"
```


https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/6e06f705-b825-4c8d-ac69-6b6de09b7f5b


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

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/9ceeae43-7512-4ca5-8dd9-0cdb3c182c99


Otro script que se puede usar para hacer pruebas es el siguiente para una trayectoria de un cuadrado [Cuadrado.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Mov/Cuadrado.py) o se puede tambien probar el del poryecto de ev3dev PS4Explor3r para control remoto con un control de PS4 [PS4Explor3r](https://www.ev3dev.org/projects/2018/09/02/PS4Explor3r/)

* Cuadrado.py


https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/584d0fcd-5021-4c59-8e6e-98d7026d1675


En esta prueba cabe resaltar varias cosas en esta prueba la primera es que como se ve en el video al momento de girar sucede una guiñada ya que el movimiento tiene un control PID interno el cual corrige el movimiento cuando se pasa de la rotación objetivo. Asimismo podemos ver que el movimiento de girar posee un grado de error que si se revisa la documentación de la libreria se puede encontara que es de 2 si no se declara los errores de giros se van acumulando a un grado tal que no se hace un cuadrado en algunas ocaciones sino una especie de rombo o en otros una figura abierta.

* PS4Explor3r


https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/f3be589d-fb43-42f0-85e0-a6480df9a6db


### Comunicación mqtt

Para poder integrar el robot lego ev3 con ros se buscaron varias formas para comunicarse con ros entre las cualses se encontro la comunicación mqtt la cual sigue una estructura similar a ros donde los elementos que se comunican se conectan a un broker mqtt el cual maneja los mensajes recibios, se manejas topicos en los cuales se pueden publicar mensajes y se puden suscribir para hacer la recepción de mensajes en donde se tiene tiene una escucha permanente para recibir los mensajes dependiendo del QoS del mesnaje se puede tener QoS 0 en donde el mensaje se entrega una unica vez sin mensaje de respuesta de entraga ni almacenamiento sino es entregado se pierde, QoS 1 se asegura la recepción del mensaje se envia el mensaje tantas veces como sea necesario hasta que el receptor confirme la recepción y el QoS 2 se asegura que el mensje siempres sea recibido esperando el emisor un mensaje de confirmación de procesamiento del mensaje para eliminarlo. Las ventajas de esta comunicación es que es de mesajes pequeños con los cuales no se requiere mucho recurso de computo para procesarse, versatilidad en los mensajes y comunicación permitiendo estar conectado a diferentes topicos al tiempo y manejando canales para cada mensaje y que los mensajes controlados tengan varios datos para controlar equipos.

En esta comunicación los equipos que se conectan son conocidos como clientes del broker MQTT para crear este cliente en el PC se uso [modulo MQTT PC](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/ev3dev_ros/scripts/mqtt_remote_method_calls.py) y para el ev3 se creo el de [modulo MQTT EV3](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/Robot/mqtt_remote_method_calls.py) en donde se crean todos los elementos para la creación del cliente y las sucripción y publicación a los topicos necesarios para que se intercomunique por medio del broker, para la recepción de los mesajes en cada caso se crean delegados que según el mesaje jason recibido lo procesaran para generar acciónes en la interfaz o en el robot. Para el control del robot se creo un modulo en python [robot_control.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/Robot/robot_control.py) en el cual se tiene la clase del robot y los metodos que este puede realizar y [ev3_MQTT.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/Robot/ev3_MQTT.py) crea el cliente que estara en ejecución en el robot y el delegado correspondiente. Para el caso del PC se creo el paquete en ROS [ev3dev_ros]([ev3dev_ros](https://github.com/JSDaleman/Robotica-movil-Lab2/tree/Cambios-lab2/Scripts/Parte%20B%20Ev3/ev3dev_ros)) el cual crea el nodo que puede comunicarse con otros nodos en ROS y funciona de puente entre ROS y el broker MQTT. Es de esta forma que la estructura de la comunicación para integrar ros es la siguiente.

![Comunicaciónes](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/ac8bc943-ea79-49ea-a248-852512709800)

### Implementación de la comunicación

#### Creación de broker y modificación de archivos
Lo primero sera crear el broker MQTT para esto usaremos [hivemq](https://www.hivemq.com/) que nos permite crear un broker gratuito con un trafico maximo de 10 GB que al ser nuestros mensajes tan puqeños y bajo trafico sera más que suficiente y se pueden conectar hasta 100 sesiones al tiempo. Una vez creado iremos a la siguiente pestaña de resumen.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/62362c28-b876-47cb-a5df-69f8fc6677b4)

De esta sacaremos los datos de Cluster URL y Port los cuales replazaremos de los archivos de  [modulo MQTT EV3](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/Robot/mqtt_remote_method_calls.py) y [GIU_Control](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Parte%20B%20Ev3/ev3dev_ros/scripts/GIU_Control.py) para poder conectarnos a nuestro propio broker. Luego iremos a la pestaña Access Management para crear el usurio con contraseña para la seguridad en este caso el usurio y contraseña seran ```LegoEV301``` el cual es el nombre del robot. El nombre dado al robot consiste de dos parte "LegoEV3" + Lego_ID que es un número de identificación que se da en los archivos anteriormente modificados para tener una identificación del robot por si deseamos conectar más robots en la red y manejarlos.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/eb66381b-6ed9-45df-b269-845c788bce5c)

Leugo iremos a la pestaña web client en donde ingrsaremos las anteriores credenciales y conectaremos el cliente. Despues nos suscribiremos a todos los topicos para ver todo el trafico esta pestaña es util para verificar el trafico que se esta teniendo y hacer pruebas de mensajes.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/a390c292-2093-438e-a0b7-0527c92722cd)


#### Carga de archivos al robot
En la terminal de la conexión con el robot crearemos un directorio para los archivos de la conexión y que ejecutaremos mas adelante para controlarlo

```
cd ~/pruebas/python/
mkdir MQTT
cd ~/pruebas/python/MQTT
```

luego copiaremos como se ha mostrado anteriormente todos los archivos del robot

#### Compilación del paquete
los archivos en la carpeta de [scripts](https://github.com/JSDaleman/Robotica-movil-Lab2/tree/Cambios-lab2/Scripts/Parte%20B%20Ev3/ev3dev_ros/scripts) los copiaremos en el paquete creado de ev3dev_ros de tal forma que quede la siguiente organización de los archivos.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/04f98a99-03f9-4e8b-bfbe-f51418f00c04)

Ahora modiifcaremos el archivo CMakeLists.txt agregando al final de este el siguiente codigo y guardamos los coambios

```
catkin_install_python(PROGRAMS
    scripts/GIU_Control.py
    scripts/mqtt_remote_method_calls.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
    )
```

ya con todos los archivos necesarios y la modificacion compilaremos el paquete

```
cd ~/ev3dev_ros/
catkin_make
source devel/setup.bash
```

### Ejecucion 
Para la ejecución abriremos kitty y lanzaremos cuatro terminales (prar abrir las cuadro abriremos el program y opriremos tres veces ctrl + shift + enter).

* Primera terminal
  En esta haremos la conexión shh con el robot para iniciar la ejecución del cliente MQTT para el control de este recordar que la contraseña es "maker"
  ```
  ssh robot@ev3dev.local
  maker
  cd ~/pruebas/python/MQTT
  python3 ev3_MQTT.py
  ```

* Segunda terminal
  En esta iniciaremos el nodo Master de ROS
  ```
  roscore
  ```

* Tercera terminal
  En esta inicaremos el nodo de turtlesim
  ```
  rosrun turtlesim turtlesim_node
  ```

* Cuarta terminal
  En esta inicaremos nuestro nodo de ros con la GUI
  ```
  rosrun ev3dev_ros GIU_Control.py
  ```

Obteniendo lo mostrado a continuación
![Terminales](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/948cb35b-e152-4094-8a82-10b70f5d180b)

Ya con esto se desplegara la interfaz donde el usuario puede hacer que el robot gire de un lado o a otro además poder ir a adelante o atras, subir o bajar el brazo o solicitar la orientación actual del robot y verla reflejada en la orientación de la tortuga.

![GIU](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/2dfd4890-bb76-4eb1-9ba9-2559c0825ade)

* Prueba de control del brazo del robot

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/93a1506f-b2b7-4799-aad5-fe47d4745182

* Prueba de controlar orientación del robot


https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/92c940af-cf99-44eb-8f9e-c92b9c9d245d


* Prueba de controlar desplazamiento

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/46a48ef9-ab9e-4792-9af0-0337abf88a13


### Conclusiones de la implementación

* El usar mensajes por MQTT permite generar un control en el robot facilmente escalable para el manejo de diferentes sensores y de diferentes formas de los motores.
* La integración con ROS por medio de la comunicación MQTT permite que el robot no sature su procesador interno pemitiendo tener una respuesta rapida a muchos de sus elementos.
* Dado que la comunicación MQTT no depende de ROS se podria llegar a implementar un nodo parecido de funcionamiento con ROS2.
* Con el manejo del robot EV3 con esta integracion con ROS se abre la posiblidad de integrarle otros sensores o procesamiento de información para realizar acciones muy grande usando el procesamiento de una computadora como nodo Master de ROS.


## Conexion Kobuki con ROS

#### Creacion del workspace

Se crea un directrotio que sera el workspace en dondde se estara trabajando y contendra nuestros archivos de intalación, adicional se genera una carpeta scr para ingresqar alli el directorio

```
mkdir Kobuki_ws

cd Kobuki_ws
mkdir src
cd src
```

### Clonacion de repositorios para la conexion y compilacion

```
git clone https://github.com/yujinrobot/kobuki
git clone https://github.com/yujinrobot/yujin_ocs

catkin_make
```
### Preparacion robot Kobuki

En este punto, procedemos preparar y realizar la conexion del robot Kobuki para su conexion con ROS, para esto, se enciende el robot utilizando el Switch ubicado en el lateral derecho, y conecta mediante el Cable USB al PC en donde tenemos el Ubuntu con el ROS.

### Configuracion final del espacio

Ubicandonos en la carpeta kobuki_ws que se genero, ejecutamos el siguiete comando para finalizar la configuracion del espacio de trabajo

```
source devel/setup.bash
```

Finalmente, se ejecuta la conexión con el comando roslaunch, ayudqandose del script "minimal.launch" que se encuentra en el paquete kobuki_node, que se utiliza para generar el enlace con el Kobuki:

```
cd
roslaunch kobuki_node minimal.launch --screen
```

En la terminal deberian verse reflejados todos los nodos de comunicacion junto con los diagnosticos del robhot.

Si se quiere corooborar que comandos están disponibles para trabajar con el robot actual en esta conexion, se puede ejecutar el comando "rostopic list", el cual nos entregara un listado completo de todos los comandos que reconoce como disponibles dentro de esta conexixon, a modo e ejemplo esta la siguiente lista:

```
rostopic list
/diagnostics
/diagnostics_agg
/diagnostics_toplevel_state
/joint_states
/mobile_base/commands/digital_output
/mobile_base/commands/external_power
/mobile_base/commands/led1
/mobile_base/commands/led2
/mobile_base/commands/motor_power
/mobile_base/commands/reset_odometry
/mobile_base/commands/sound
/mobile_base/commands/velocity
/mobile_base/debug/raw_data_command
/mobile_base/debug/raw_data_stream
/mobile_base/events/bumper
/mobile_base/events/button
/mobile_base/events/cliff
/mobile_base/events/digital_input
/mobile_base/events/power_system
/mobile_base/events/robot_state
/mobile_base/events/wheel_drop
/mobile_base/sensors/bump_pc
/mobile_base/sensors/core
/mobile_base/sensors/dock_ir
/mobile_base/sensors/imu_data
/mobile_base/sensors/imu_data_raw
/mobile_base/version_info
/odom
/rosout
/rosout_agg
/tf
```

Dentro de las funciones que tenemos con estos comandos esta el subscribirse y publicar eventos asociados a ciertos sensores del Robot y entradas digitales del mismo, asi como tambien ofrece la posibilidad de verificar el nivel de bateria.




## Incertidumbre en sensores

###  Consulta bibliográfica

#### ¿ Qué es el Vocabulario Internacional de Metrología (VIM)?

El Vocabulario Internacional de Metrología (VIM) es un estándar internacional que se desarrolló con el objetivo de establecer un conjunto común de términos y definiciones en el campo de la metrología, la ciencia de la medición y sus aplicaciones. Este estándar fue desarrollado por la Organización Internacional de Metrología Legal (OIML) y el Comité Internacional de Pesas y Medidas (CIPM). El VIM es esencialmente un “diccionario terminológico” que contiene las denominaciones y definiciones que conciernen a uno o varios campos específicos de la metrología. Este documento es de gran importancia para los laboratorios y los profesionales de la medición, ya que proporciona una base común para la comprensión y la comunicación de los conceptos de medición.

La versión más reciente del VIM es la 3ª edición, que se publicó en 2012. Esta edición incluye pequeñas correcciones y actualizaciones a las definiciones y términos anteriores. Además, está disponible en varios idiomas, incluyendo el español, lo que facilita su uso y comprensión por parte de los profesionales de la metrología de todo el mundo. El VIM es una herramienta valiosa para los profesionales de la metrología y los laboratorios de medición. Al proporcionar un conjunto común de términos y definiciones, el VIM ayuda a garantizar que todos los involucrados en el proceso de medición tengan una comprensión clara y consistente de los conceptos clave. Esto es esencial para garantizar la precisión y la coherencia de las mediciones.

#### Vocabulario según el VIM

* **Exactitud de medida:** Se define como la proximidad entre un valor medido y un valor verdadero de un mensurando. Es decir, se refiere al grado de cercanía que tiene los resultados medidos con el valor de referencia, también llamado valor verdadero o magnitud real.
* **Precisión de medida:** Se define como la proximidad existente entre las indicaciones o los valores medidos obtenidos en mediciones repetidas de un mismo objeto, o de objetos similares, bajo condiciones específicas.
* **Error de medida:** Se define como la diferencia entre un valor medido de una magnitud y un valor de referencia (valor convencional o valor verdadero).
* **Incertidumbre de medida:** Se define como un parámetro, asociado al resultado de una medición, que caracteriza la dispersión de los valores que razonablemente podrían ser atribuidos al mensurando. Es una medida de la variabilidad en los resultados de medición.

#### Tipos de errores

* **Error sistemático:** Este tipo de error es constante en todas las mediciones y se debe a problemas con el equipo o el diseño del experimento. Por ejemplo, si tu cinta de medición se ha estirado, todas tus mediciones serán más bajas que el valor real. Este tipo de error afecta la validez del estudio y se asocia con debilidades en el diseño metodológico o de la fase de ejecución del estudio.
* **Error aleatorio:** Este tipo de error varía de manera impredecible de una medición a otra. Se debe a la variabilidad inherente en el proceso de medición o en la cantidad que se está midiendo. Por ejemplo, si estás midiendo la velocidad del viento, esta puede aumentar y disminuir en diferentes momentos, por lo que si tomas una medida en un minuto, probablemente no será exactamente igual un minuto después. Los errores aleatorios afectan principalmente a la precisión de la medición.

#### Teoria estadistica

En estadística, el valor medio o esperado es un número que representa el valor promedio de una variable aleatoria. Es igual al sumatorio de todos los productos formados por los valores de los sucesos aleatorios y sus respectivas probabilidades de suceder.

Las magnitudes que se usan para medir la dispersión de datos en estadística son las siguientes:

- **Rango:** Es la diferencia entre el menor y el mayor valor de la distribución. 
- **Desviación media:** Es el promedio de las diferentes desviaciones de cada dato respecto a la media.
- **Varianza:** Es igual a la suma de los cuadrados de los residuos partido por el número total de observaciones.
- **Desviación estándar:** Es igual a la raíz cuadrada de la suma de los cuadrados de las desviaciones de la serie de datos partido por el número total de observaciones.
- **Coeficiente de variación:** Es una medida de dispersión que sirve para determinar la dispersión de un conjunto de datos respecto a su media.
- **Rango intercuartil:** Indica la diferencia entre el tercer y el primer cuartil.

### Lidar

Usando el RPLIDAR A1M8

![IMG_20240429_104106578](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/1c0eb40f-80e7-4f98-90ba-1ec0b1537172)


Datos capturados con el programa scanRPLIDAR.py

![MeRLIDAR](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/b0e68ac0-0cae-499a-8b3f-c8e508e349dc)

![POSE2](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/5b992f91-5f3e-421b-9ef6-f7074854dc81)

![POSE3](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/c1250e55-e53b-49c3-a250-56c1babea7e0)


### Ultrasonido HC-SR04

###  Sensores Lego

#### Desplazamineto
Para encontar la incertidumbre en el desplazamiento del robot con los encoder de los motores y el sensor de ultrasonido se hizo el siguiente montaje experimental donde se usa un flexometro o cinta metrica como patrón.

![Imagen de WhatsApp 2024-04-12 a las 22 03 10_ea68df87](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/dfffbc05-0613-4085-92e6-433e7413eeef)
![Imagen de WhatsApp 2024-04-12 a las 22 03 10_1a7d094a](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/70998067/6a870c9f-32e1-45fd-99d5-caaa2f58bd13)

En este medimos con el flexometro el desplazamiento que tiene el punto de contacto de la rueda con el suelo, para la obtención de datos se hicieron dos scripts uno en donde el movimiento se detiene con el valor del encoder [Desplazamiento.py](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Incertidumbre/Desplazamiento.py) y otro donde se detiene con el valor del sensor de ultra sonido [DesplazamientoSensorUltraSonido.py
](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Incertidumbre/DesplazamientoSensorUltraSonido.py). Una vez creados los scripts estos se copiaron en el robot en un directorio creado para estos.

En la terminal de la conexion ssh
```
cd ~/pruebas/python/
mkdir Incertidumbre
cd Incertidumbre
```

En la terminar en el directorio donde tengamos los scripts
```
scp Desplazamiento.py robot@<Dirección IP del robot>:/home/robot/pruebas/python/Incertidumbre/
scp DesplazamientoSensorUltraSonido.py robot@<Dirección IP del robot>:/home/robot/pruebas/python/Incertidumbre/

```
** Nota ** Si en la red wifi se detecta correctamente el robot puede usara ev3dev.local en vez de la dirección IP

En la terminal de la conexion ssh
```
cd ~/pruebas/python/Incertidumbre/
chmod +x Desplazamiento.py
chmod +x DesplazamientoSensorUltraSonido.py
```

para ejecutar cada uno se usan los comados 

```
python3 Desplazamiento.py
python3 DesplazamientoSensorUltraSonido.py
```
Cada uno se ejecuto dos veces una con velocidad de 30% y otra con la de 100% obteniendo los datos presentados en este excel [Excel de mediciones](https://unaledu-my.sharepoint.com/:x:/g/personal/jdaleman_unal_edu_co/Ed-b2T2l6-hNlDRAIFZ_NJcBvsgojICqpPVucmziBNNi9A). Con los errores encontrados se puede ver que el sensor de ultrasonido teinde a ser más excato que el encoder esto debido a los calucolos internos que se hacen con el encoder puede afectar más la lectura de la medición asi mismo que cuando se maneja mayores velocidades el error de desplazamiento tiende a ser mayor que a baja velocidad.

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


Las mediciónes se registrarón en el siguiente excel para procesar la información [Excel de mediciones](https://unaledu-my.sharepoint.com/:x:/g/personal/jdaleman_unal_edu_co/Ed-b2T2l6-hNlDRAIFZ_NJcBvsgojICqpPVucmziBNNi9A). En las mediciones podemos ver que el error relativo que se maneja es del 1%, el error esta entre 1 a 2 grados del valor del patron  en donde los movimientos cortos (30°) generan menos errores a los movimientos largos (45°). Esto se puede deber al error acumulado en el movimiento en donde al moverse un ángulo mayor se tiene errores más grandes aun asi el grado del error tiende a no superar el 3%.


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
