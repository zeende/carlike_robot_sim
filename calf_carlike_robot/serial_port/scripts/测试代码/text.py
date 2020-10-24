import serial
import time 

serialPort = "/dev/ttyUSB0"  
baudRate = 9600  
ser = serial.Serial(serialPort, baudRate, timeout=1)
print("port=%s ,b=%d" % (serialPort, baudRate))

while 1:
    str = ser.readline()
    str = str.strip()
    str = str.decode('utf-8','ignore') 
    print(str)
    list_str = str.split(',')
    numbers = int(list_str[0])

   # list_int[0] = int(list_str[0])
    print(numbers)
    time.sleep(1)
ser.close()
