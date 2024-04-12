#!/usr/bin/env python 1
2
import rospy 3
from geometry_msgs.msg import Twist 4
from random import random 5
6
if __name__ == ’__main__’: 7
# Create a publisher on topic turtle1/cmd_vel, type geometry_msgs/Twist 8
pub = rospy.Publisher(’turtle1/cmd_vel’, Twist, queue_size=1000) 9
rospy.init_node(’pypubvel’, anonymous=False) 10
11
rate = rospy.Rate(2) 12
13
# Similar to while(ros::ok()) 14
while not rospy.is_shutdown(): 15
# Create and populate new Twist message 16
msg = Twist() 17
msg.linear.x = random() 18
msg.angular.z = 2*random() - 1 19
20
# Similar to ROS_INFO_STREAM macro, log information. 21
rospy.loginfo(’Sending random velocity command:’ + 22
’ linear=’ + str(msg.linear.x) + ’ angular=’ + str(msg.angular.z)) 23
24
# Publish the message and wait on rate. 25
pub.publish(msg) 26
rate.sleep() 
