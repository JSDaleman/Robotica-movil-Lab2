# Robotica-movil-Lab2
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya

## Conexion Lego EV3 con ROS
Para poder conectar el lego EV3 con ROS primero se necesita tener una memoria SD de minimo 2 GB de alamacenamiento y una antena USB wifi para el robot EV3. Para elegir una SD compatible y un adaptador wifi se recomienda leer las siguientes paginas:
* [Seleccion de SD](https://github.com/ev3dev/ev3dev/wiki/Selecting-a-microSD-card)
* [Antenas wifi compatibles leJos](https://lejosnews.wordpress.com/2015/02/03/comparing-wifi-adapters/).
* [Antena wifi compatibles con ev3dev](https://github.com/ev3dev/ev3dev/wiki/USB-Wi-Fi-Dongles)

  Para acceder a la programación del robot EV3 por una API diferente a la de lego usamos un booteo de una distribución de Linux Debian desarrollada para el robot conocido como [ev3dev](https://www.ev3dev.org/) este fue desarrollado para el uso de diferentes lenguajes de programación con el robot ev3 como python, micropython, java, C++, C y etc. (Para conocer todos los lenguajes disponibles ver [lenguajes de programación](https://www.ev3dev.org/docs/programming-languages/)).

  **Nota:** Acabe aclarar que este es un booteo por una unidad de almacenamiento diferente por lo cual no se afecta o modifica el firmware original que posee el bloque ev3.
  Para crear la SD booteable se siguieron los pasos de la pagina de ev3dev [SD booteable](https://www.ev3dev.org/docs/getting-started/)

## Otros links de interes
* [Conexion de Lego Ev3 por medio de una raspberry pi](https://github.com/aws-samples/aws-builders-fair-projects/blob/master/reinvent-2019/lego-ev3-raspberry-pi-robot/README.MD) 
* [ROS desde el Lego Ev3](https://github.com/moriarty/ros-ev3) 
* [Manejo de motores del Ev3 con Python](https://www.youtube.com/watch?v=j0-ATIe6pqg) 
* [Uso de sensor lidar con Ev3](https://www.youtube.com/watch?v=JX0zeYa-faM) 
* [Programacion y conexion SSH desde Visual Studio Code con Ev3](https://www.youtube.com/watch?v=uNSIOvqzAnY) 
* [Instalacion de ROS distribucion JADE en el Ev3](https://github.com/osmado/ev3dev_ros_distribution) 


