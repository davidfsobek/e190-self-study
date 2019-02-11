#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Vector3

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

def node2():
    rospy.init_node('node2', anonymous=True)

    rospy.Subscriber('/p1pos', Vector3, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    node2()
