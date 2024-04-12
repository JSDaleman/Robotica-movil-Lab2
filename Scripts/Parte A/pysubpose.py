#!/usr/bin/env python 1
2
import rospy
from turtlesim.msg import Pose 4
5
def poseMessageReceived(message): 6
rospy.loginfo(’position=(’ + str(message.x) + ’,’ + str(message.y) + 7
’)’ + ’ direction=’ + str(message.theta)) 8
9
if __name__ == ’__main__’: 10
rospy.init_node(’pysubpose’, anonymous=False) 11
sub = rospy.Subscriber(’turtle1/pose’, Pose, poseMessageReceived) 12
13
rospy.spin()
