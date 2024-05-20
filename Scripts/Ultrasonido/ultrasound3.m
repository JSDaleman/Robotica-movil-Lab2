% ULTRASOUND3 programa para capturar datos por el puerto serial. Previo a
% ejecutar el programa verifique mediante el Administrador de dispositivos
% el puerto alque esta conectado el ARDUINO y modifique el numero de puerto 
% en la instruccion PORT. Ricardo % Ramarez Heredia, Universidad Nacional 
% de Colombia, 2023. 

clear all;
port=serialport('COM4',9600,'DataBits',8);
flush(port)
nm=100; %Numero de muestras.
figure(1)
clf
xlabel('Muestra')
ylabel('Distancia (cm)')
title('U_{sound} Data')
grid on;
hold on;
t=1:nm;
dist=zeros(1,nm);
for i=1:nm
      dist(i)=readline(port); 
      pause(.25)
end
plot(t,dist)
delete(port);
clear port
