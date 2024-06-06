# Robotica-movil-Lab2-Kobuki-ROS
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya Castaño

Tabla de Contenidos
---
- [Conexion Kobuki con ROS](#conexion-kobuki-con-ros).
  - [Creacion del workspace](#creacion-del-workspace-1).
  - [Clonacion de repositorios para la conexion y compilacion](#clonacion-de-repositorios-para-la-conexion-y-compilacion).
  - [Preparacion robot Kobuki](#preparacion-robot-kobuki).
  - [Configuracion final del espacio](#configuracion-final-del-espacio).
  - [Sensor cliff](#sensor-cliff).
 
  ## Conexion Kobuki con ROS

### Creacion del workspace

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

Utilizando el paquete kobuki_keyop para aplicar teleoperación básica en el kobuki:

![Terminal de conexión](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/b52a08f8-759d-4cc0-b55f-c66ee7381388)


https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/bb2c6317-a187-4361-9e7f-d92b1f3fe066

### Sensor cliff

Codigo en Python:

```
import rospy
from kobuki_msgs.msg import CliffEvent, Sound
import subprocess

def accion (data):
    rospy.loginfo("Evento de caida detectado: %s", data)
    sonido(5) 

def sensor():
    rospy.init_node('cliff_listener', anonymous=True)
    rospy.Subscriber("/mobile_base/events/cliff", CliffEvent, accion)
    rospy.spin()

def sonido(sound_value):
    pub_sound = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
    sound_msg = Sound()
    sound_msg.value = sound_value
    pub_sound.publish(sound_msg)

def launch_roslaunch_file(package_name, launch_file):
    command = ['roslaunch', package_name, launch_file, '--screen']
    subprocess.Popen(command)

if __name__ == '__main__':
    try:
        launch_roslaunch_file('kobuki_keyop', 'safe_keyop.launch')
        sensor()
    except rospy.ROSInterruptException:
        pass
```

Prueba de funcionamiento:

https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/dcee9057-10f2-4529-aca3-cc5b3aa43d3c

