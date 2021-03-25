import picar_4wd as fc
import time, math
import threading
from speed import Speed
from picar_4wd.servo import Servo
from picar_4wd.pwm import PWM

import cv2

speed = 20
def reset_servo(angle1):
    ser = Servo(PWM("P0"))                     
    ser.set_angle(angle1) 

def main():

    reset_servo(-65)
    while True:
       #reset_servo(-65)
        scan_list = fc.scan_step(25)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp == [2,2,2,2]:        
            fc.forward(speed)
          #  reset_servo(-65)

        else:
            fc.stop()
            time.sleep(0.5)
            fc.backward(100)
            time.sleep(0.5)
            fc.stop()
            time.sleep(0.5)
            fc.turn_right(50)   

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("stopped by User")
       # ctrl+c
    finally: 
        fc.stop()

