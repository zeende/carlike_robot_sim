#!/usr/bin/env python
import rospy
from serial_port.msg import header
import serial
import time 

serialPort = "/dev/ttyUSB0"  
baudRate = 9600  
ser = serial.Serial(serialPort, baudRate, timeout=1)
print("port=%s ,b=%d" % (serialPort, baudRate))
time.sleep(1)

def talker():
    pub = rospy.Publisher('chatter', header, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        get_str = ser.readline()
        get_str = get_str.strip()
        get_str = get_str.decode('utf-8','ignore') 
        print(get_str)
        list_str = get_str.split(',')
        msg = header()
        data1 = int(list_str[0])
        data2 = int(list_str[1])
        data3 = int(list_str[2])
        msg.num1 = data1
        msg.num2 = data2
        msg.num3 = data3
        pub.publish(msg)
        print(msg.con)
        if msg.con:
            ser.write("1\n") 
        else:
            ser.write("0\n") 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


