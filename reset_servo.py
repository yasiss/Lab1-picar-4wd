from picar_4wd.servo import Servo
from picar_4wd.pwm import PWM 
import sys



try:
    ser = Servo(PWM("P0")) 
   # print("offset angle:",Servo(PWM("P0")) ) 
  #  print(ser.set_angle(0) )
                   
    ser.set_angle(-65)                 
  #  print(ser.offset)
except KeyboardInterrupt:
        print("stopped by User")
        ser = Servo(PWM("P0"))                     
        ser.set_angle(-35) 