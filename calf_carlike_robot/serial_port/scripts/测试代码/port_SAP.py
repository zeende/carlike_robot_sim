#!/usr/bin/env python
import rospy
import std_msgs.msg
from serial_port.msg import header
from geometry_msgs.msg import Twist
import serial
import time 
import threading

serialPort = "/dev/ch340"  
baudRate = 115200
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("serial port is %s ,baudRate is %d" % (serialPort, baudRate))
time.sleep(1)
pub = rospy.Publisher('serial_data_odom', header, queue_size=1)


def thread_job():
    rospy.spin()

def callback(data):
    # x=int(data.linear.x*1000)
    # th=int(data.angular.z*1000)
    # print("---Twist.linear.x = "+str(data.linear.x)+","
    #       "Twist.angular.z = "+str(data.angular.z)+"---\n")

    str1=str(int(data.linear.x*1000))
    str2=str(int(data.angular.z*1000))
    ser.write("%s,0,%s\n"%(str1,str2))
    print("---- %s ,%s ----"%(str1,str2))
    #time.sleep(0.25)
    # print("%d,%d"%(data.linear.x,data.angular.z))


def SubscribeAndPublish():
    rospy.init_node('serial_data_contral', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback,queue_size=1,buff_size=52428800)
    #rospy.Subscriber('cmd_vel', Twist, callback,queue_size=1,buff_size=52428800)
    # rospy.spin()
    rate = rospy.Rate(20)
    add_thread = threading.Thread(target = thread_job)
    add_thread.start()

    while not rospy.is_shutdown():
        
        get_str = ser.readline()
        get_str = get_str.strip()
        #get_str = get_str.decode('utf-8','ignore') 
        print(get_str)
        list_str = get_str.split(',')
        #print(list_str)
        #print("######\n")

        msg = header()
        # data1 = int(list_str[0])
        # data2 = int(list_str[1])
        # data3 = int(list_str[2])
        # msg.num1 = data1
        # msg.num2 = data2
        # msg.num3 = data3
        # # msg.num1 = x 
        # # msg.num2 = 0 
        # # msg.num3 = th 
        # pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        SubscribeAndPublish()
    except rospy.ROSInterruptException:
        pass


########################
