#!/usr/bin/env python

import rospy
from serial_port.msg import header
 
def callback(data):

    # rospy.loginfo(data.num1)
    # rospy.loginfo(data.num2)
    # rospy.loginfo(data.num3)
    print("num1 = "+str(data.num1)+", "
          "num2 = "+str(data.num2)+", "
          "num3 = "+str(data.num3)+"\n")


def listener():
 
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('serial_data_odom', header, callback,queue_size=1)
    rospy.spin()
 
if __name__ == '__main__':
    listener()

