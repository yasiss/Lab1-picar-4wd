
from picamera import PiCamera
from time import sleep

#camera = picamera.PiCamera()
#camera.capture('example.jpg')

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Desktop/video2.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()