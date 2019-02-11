#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Vector3

def node1():
    pub = rospy.Publisher('/p1pos', Vector3, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    startup_time = rospy.get_time()
    x0y0pos = np.array([2,2,0])
    while not rospy.is_shutdown():
        x1y1pos = rotate(startup_time-rospy.get_time(), x0y0pos)
        x1y1posV = Vector3(x1y1pos[0], x1y1pos[1], x1y1pos[2])
        rospy.loginfo(x1y1posV)
        pub.publish(x1y1posV)
        rate.sleep()

def rotate(delta_time, pos):
    rotation_rate = 0.1 #rads/sec
    theta = rotation_rate * delta_time
    rot_transform = np.array([[np.cos(theta), -np.sin(theta), 0],
                             [np.sin(theta),   np.cos(theta), 0],
                             [0            , 0            ,   1]])
    return np.dot(pos, rot_transform)

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
