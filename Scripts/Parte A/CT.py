#!/usr/bin/env python

import rospy
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty

if __name__ == '__main__':
     rospy.init_node('turtlesimservice', anonymous=False)

  #Define la primera tortuga
     rospy.wait_for_service('turtle1/teleport_absolute')
     turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute',
 	   TeleportAbsolute)

  #Define la segunda tortuga
     rospy.wait_for_service('turtle2/teleport_absolute')
     turtle2_teleport = rospy.ServiceProxy('turtle2/teleport_absolute',
 	   TeleportAbsolute)
 
     rospy.wait_for_service('clear')
     clear1 = rospy.ServiceProxy('clear', Empty)


     rate = rospy.Rate(0.3)

  #Posicion de las tortugas
     pos1=1
     pos2=1
     # Similar to while(ros::ok())
  #Bucle
     while not rospy.is_shutdown():
  #Cuadrado
 	      if (pos1==1):
 		       resp1 = turtle1_teleport(4, 5, 0)
 		       clear1()
 	      if (pos1==2):
 		       resp1 = turtle1_teleport(4, 10, 0)
 	      if (pos1==3):
 		       resp1 = turtle1_teleport(8, 10, 0)
 	      if (pos1==4):
 		       resp1 = turtle1_teleport(8, 5, 0)
 	      if (pos1==5):
 		       resp1 = turtle1_teleport(4, 5, 0)
 	      if (pos1>5):
 		       pos1=1
 	      pos1+=1

   #Triangulo
 	      if (pos2==1):
 		       resp2 = turtle2_teleport(3, 5, 0)
 		       clear1()
 	      if (pos2==2):
 		       resp2 = turtle2_teleport(3, 11, 0)
 	      if (pos2==3):
 		       resp2 = turtle2_teleport(0, 7, 0)
 	      if (pos2==4):
 		       resp2 = turtle2_teleport(3, 5, 0)
 	      if (pos2>4):
 		       pos2=1
 	      pos2+=1
 
rate.sleep()
