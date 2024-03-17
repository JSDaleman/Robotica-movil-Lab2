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
