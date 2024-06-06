# Robotica-movil-Lab2-Sensores-e-incertidumbre
Juan Sebastian Daleman

Juan David Chica Garcia

Luis Alejandro Duran Espitia

Santiago Olaya Castaño

Tabla de Contenidos
---
- [Incertidumbre en sensores](#incertidumbre-en-sensores).
  - [Consulta bibliografica](#consulta-bibliográfica).
    - [¿ Qué es el Vocabulario Internacional de Metrología (VIM)?](#-qué-es-el-vocabulario-internacional-de-metrología-vim)
    - [Vocabulario según el VIM](#vocabulario-según-el-vim)
    - [Tipos de errores](#tipos-de-errores)
    - [Teoria estadistica](#tipos-de-errores)
  - [Lidar](#lidar)
  - [Ultrasonido HC-SR04](#ultrasonido-hc-sr04)
    - [Preparacion](#preparacion)
    - [Toma de datos](#toma-de-datos)
    - [Procesamiento de datos y presentación de resultados](#procesamiento-de-datos-y-presentación-de-resultados)
  - [Sensores Lego](#sensores-lego).
    - [Desplazamineto](#desplazamineto).
    - [Giro de la rueda](#giro-de-la-rueda).

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
#### Sensor HOKUYO

Se construye un mapa y se coloca el sensor HOKUYO en tres poses distintas:

Pose 1:

![Pose1O](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/73b200a0-0ac7-4455-8d1b-96109321c96d)

Pose 2:

![Pose2O](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/27e7fa87-0ed0-4515-8cb3-a861a6103ad4)

Pose 3:

![Pose3O](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/433e9847-7503-4f2c-bfca-384beafa2fe4)


Usando el programa URG Benri data viewing tool, se realizo la configuracion del sensor y la medición del pasa construido en las tres distintas poses.

Pose 1:

![Captura1](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/8efe52e4-1f2f-46ad-bf56-751600627726)

Pose 2:

![Captura2](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/89be178f-a164-4e30-be7f-b3404ade67fa)

Pose 3:

![Captura3](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/a22f1c3d-bc19-42b3-980c-9911e8b1ca24)

#### RPLIDAR A1M8

![IMG_20240429_104106578](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/1c0eb40f-80e7-4f98-90ba-1ec0b1537172)


Datos capturados con el programa scanRPLIDAR.py

![MeRLIDAR](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/b0e68ac0-0cae-499a-8b3f-c8e508e349dc)

![POSE2](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/5b992f91-5f3e-421b-9ef6-f7074854dc81)

![POSE3](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/68557324/c1250e55-e53b-49c3-a250-56c1babea7e0)


### Ultrasonido HC-SR04
#### Preparacion
Primeramente se subio el codigo al arduino usando el IDE de arduino para el [ultrasonido](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Ultrasonido/usound3.ino) funcione con el arduino.

Se realizaron las conexiones de los pines del sensor a los pines del arduino uno, teniendo en cuenta que en este caso el pin echo es el 11 y el pin trigger es el 12 del arduino y que tienen que conectarse en el los pines echo y trigger del sensor, respectivamente.
Luego se abrio la interfaz de matlab y se creo un script para optener y almacenar los [datos](https://github.com/JSDaleman/Robotica-movil-Lab2/blob/Cambios-lab2/Scripts/Ultrasonido/ultrasound3.m) de las para suy procesamiento.

#### Toma de datos

El anterior codigo nos permite leer los primeros 100 datos seriales que nos suministre el sensor y guardarlos en un vector.

Ahora y antes de correr el script de matlab, ubicamos un obtaculo a 1m.
![Imagen de WhatsApp 2024-04-29 a las 11 25 26_238e8ffa](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/40bb4ccf-4f7f-4d57-9118-7c7ab31e1cff)
y posteriormete se corre el script, lo cual nos dio los siguientes datos.
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/f5f5f133-7e06-4666-ab42-fd5b05efb1e1)
Luego con estos datos realizamos un histograma.
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/38c3b58f-6cd1-436a-bfdd-4ebcab71375e)

Ahora ubicamos un obtaculo a 1.5m.
![Imagen de WhatsApp 2024-04-29 a las 11 28 26_50e38d44](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/5bd8bd31-aac9-472a-a9ba-09a60c232a35)
y posteriormete se corre el script, lo cual nos dio los siguientes datos.
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/d8c235aa-13f5-4b4e-be69-1e1793aa7e6f)
Luego con estos datos realizamos un histograma.
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/e5a484c6-da62-4cf5-ae2a-c0cdb8eda4bf).

Y finalmente ubicamos un obtaculo a 2m.
![Imagen de WhatsApp 2024-04-29 a las 11 33 22_0a52fda4](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/4c2b1433-ee8a-4d8e-8d4c-c51159ab3d45).
y posteriormete se corre el script, lo cual nos dio los siguientes datos.
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/27411a1b-e445-400b-a055-94563453efd5).
Luego con estos datos realizamos un histograma.

#### Procesamiento de datos y presentación de resultados
Para cada grupo de datos se calculo la distancia media, la desviación estándar, el error absoluto y el error relativo respecto a la medida de distancia con flexómetro.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/5058fe79-6714-4bb9-bae2-064d2bce663a).

Luego se realizo la gráfica de distancia contra índice de muestra.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/d97c6726-fde6-4fc9-9ffd-72f470225bc1).

Por utimo se realizan algunas gráficas de comportamiento de desviación estándar y errores absoluto y relativo en función de la distancia media.

![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/2ea7ddfe-2818-4d50-825f-52aa8a2ddcf1).
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/c7f9b3af-7d3f-4f51-8e4d-f469155aaed6).
![image](https://github.com/JSDaleman/Robotica-movil-Lab2/assets/125931563/587bf13a-c00d-4c3f-94ae-7ff79d2ea04a).

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
