#!/usr/bin/env python
import sys
import tty
import termios


import rospy
from serial_port.msg import header
from serial_port.msg import con
import time 


    
def talker():
    pub = rospy.Publisher('contral_data', con, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        msg = con()
        data1 = int(input("enter your input: "))
        #data1 = 
        msg.con = data1
        pub.publish(msg)
        print(msg.con)
       # rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


