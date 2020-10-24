#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

import time 



def callback(data):

    print("I have read :" 
        "contral_data = "+str(data.linear.x)+"\n")

    #rate.sleep()
   # time.sleep(1)

def SubscribeAndPublish():
    
    rospy.init_node('serial_data_contral', anonymous=True)
    rospy.Subscriber('~/car/cmd_vel', Twist, callback)
    rospy.spin()
   # rate = rospy.Rate(1) # 1hz


if __name__ == '__main__':
    try:
        SubscribeAndPublish()
    except rospy.ROSInterruptException:
        pass


