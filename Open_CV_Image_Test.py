
import picamera
import time

camera = picamera.PiCamera()
camera.capture('example1.jpg')
'''
camera.start_recording('exmpvid.h264')
time.sleep(5)
camera.stop_recording
'''

