#!/usr/bin/env python

# -*- coding: utf-8 -*-

import time 
import serial
time.sleep(1)
serialPort = "/dev/ttyUSB0"  
baudRate = 9600  
ser = serial.Serial(serialPort, baudRate, timeout=1)
contral = 1
while 1:
        contral=not(contral)
        if contral:
            ser.write("1\n") 
        else:
            ser.write("0\n")
        print(contral)    
        time.sleep(1)
        
ser.close()