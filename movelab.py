import picar_4wd as fc
import RPi.GPIO as GPIO
import time, math
import threading
from speed import Speed

speed = 5

def move_scan():
    
 #   speed = 10   # 30
#    speed1= Speed(10)
#    speed1.start()
    while True:
        scan_list = fc.scan_step(50)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2,2,2,2]:
           # fc.backward(30)
            fc.turn_right(speed)
           # fc.stop()
        else:
            fc.forward(speed)
if __name__ == "__main__":
     try:
        print(fc.us.get_distance())
        move_scan()        
     finally: 
        fc.stop()

