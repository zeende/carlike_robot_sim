#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

import time

msg = """
Control Your ROBOT!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

space key, k : force stop
w/x: shift the middle pos of throttle by +/- 5 pwm
a/d: shift the middle pos of steering by +/- 2 pwm
CTRL-C to quit
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
       # ',':(-1,0),
       # '.':(-1,1),
       # 'm':(-1,-1),
           }
moveBackBindings = {
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('car_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    status = 0
    count = 0
    reversing=0
    step=0
    wait=3
    speed_mid = 1500 #(1500:stop, 1480:0.5m/s, 1450:2.5m/s)
    speed_bias = 0
    turn_mid = 90    #(0~180)
    turn_bias = 0
    control_speed = speed_mid
    control_turn = turn_mid
    try:
        print msg
        print vels(control_speed,control_turn)
        while(1):
            
            key = getKey()
            if key in moveBindings.keys():
                control_speed = -moveBindings[key][0]*45 + speed_mid + speed_bias
                control_turn = moveBindings[key][1]*30 + turn_mid + turn_bias
                count = 0
		step=0
		reversing=0
	    elif key in moveBackBindings.keys():
		if reversing == 0 :
			if step < wait :
                		control_speed = -moveBackBindings[key][0]*120 + speed_mid + speed_bias
                		control_turn = moveBackBindings[key][1]*30 + turn_mid + turn_bias
				step=step + 1 
			elif step < wait+2 :
				control_speed = speed_mid + speed_bias
				control_turn = moveBackBindings[key][1]*30 + turn_mid + turn_bias
				step=step + 1
			else:
				step=0
				reversing=1
		else:
		    	control_speed = -moveBackBindings[key][0]*110 + speed_mid + speed_bias
                    	control_turn = moveBackBindings[key][1]*30 + turn_mid + turn_bias
                count = 0
            elif key == ' ' or key == 'k' :
                control_speed = speed_mid + speed_bias
                control_turn = turn_mid + turn_bias
            elif key == 'w' :
                speed_bias = speed_bias - 5
                control_speed = control_speed - 5
                print vels(control_speed,control_turn)
            elif key == 'x' :
                speed_bias = speed_bias + 5
                control_speed = control_speed + 5
                print vels(control_speed,control_turn)
            elif key == 'a' :
                turn_bias = turn_bias + 2
                control_turn = control_turn + 2
                print vels(control_speed,control_turn)
            elif key == 'd' :
                turn_bias = turn_bias - 2
                control_turn = control_turn - 2
                print vels(control_speed,control_turn)
            else:
                count = count + 1
                if count > 4:
                    control_speed = speed_mid + speed_bias
                    control_turn = turn_mid + turn_bias
                if (key == '\x03'):
                    break
            twist = Twist()
            twist.linear.x = (control_speed-1500)/100; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = (control_turn-90)*3.14/180
            pub.publish(twist)

            

    except:
        print "error"

    finally:
        twist = Twist()
        twist.linear.x = speed_mid; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = turn_mid
        pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

