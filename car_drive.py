import picar_4wd as fc
import cv2
import datetime
import time, math
import threading
import logging
from speed import Speed
from picar_4wd.servo import Servo
from picar_4wd.pwm import PWM
from lane_follower import LaneFollower
#from objects_on_road_processor import ObjectsOnRoadProcessor

_SHOW_IMAGE = True


class PiCar(object):

    __INITIAL_SPEED = 0
    __SCREEN_WIDTH = 320
    __SCREEN_HEIGHT = 240

    def __init__(self):
        """ Init camera and wheels"""
        logging.info('Creating a PiCar-4WD...')

        fc.stop()

        logging.debug('Set up camera')
        self.camera = cv2.VideoCapture(-1)
        self.camera.set(3, self.__SCREEN_WIDTH)
        self.camera.set(4, self.__SCREEN_HEIGHT)
        
        ser = Servo(PWM("P0"))                     
        ser.set_angle(-65) 

        self.lane_follower = LaneFollower(self)
        #self.traffic_sign_processor = ObjectsOnRoadProcessor(self)
        # lane_follower = DeepLearningLaneFollower()

        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        datestr = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        self.video_orig = self.create_video_recorder('../data/temp/car_video%s.avi' % datestr)
        self.video_lane = self.create_video_recorder('../data/temp/car_video_lane%s.avi' % datestr)
   #     self.video_objs = self.create_video_recorder('../data/temp/car_video_objs%s.avi' % datestr)

        logging.info('Created a PiCar-4wd')

    def create_video_recorder(self, path):
        return cv2.VideoWriter(path, self.fourcc, 20.0, (self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))

    def __enter__(self):
        """ Entering a with statement """
        return self

    def __exit__(self, _type, value, traceback):
        """ Exit a with statement"""
        if traceback is not None:
            # Exception occurred:
            logging.error('Exiting with statement with exception %s' % traceback)

        self.cleanup()

    def cleanup(self):
        """ Reset the hardware"""
        logging.info('Stopping the car, resetting hardware.')
        fc.stop()
        self.camera.release()
        self.video_orig.release()
        self.video_lane.release()
       # self.video_objs.release()
        cv2.destroyAllWindows()


    def drive(self, speed=__INITIAL_SPEED):
        """ Main entry point of the car, and put it in drive mode
        Keyword arguments:
        speed -- speed of back wheel, range is 0 (stop) - 100 (fastest)
        """
        logging.info('Starting to drive at speed %s...' % speed)
        i = 0
        while self.camera.isOpened() and i<30:
            _, image_lane = self.camera.read()
            image_objs = image_lane.copy()
            i += 1
            self.video_orig.write(image_lane)

      #      image_objs = self.process_objects_on_road(image_objs)
      #      self.video_objs.write(image_objs)
       #     show_image('Detected Objects', image_objs)

            image_lane = self.follow_lane(image_lane)
            self.video_lane.write(image_lane)
           # show_image('Lane Lines', image_lane)
            cv2.imshow('Lane Lines', image_lane)
   
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cleanup()
                break
        speed4 = Speed(25)
        speed4.start()
        # time.sleep(2)
        fc.forward(20)
        x = 0
        for i in range(25):
            time.sleep(0.1)
            speed = speed4()
            x += speed * 0.1
        #    time.sleep(0.5)    
            #print("%smm/s"%speed)
        print("%smm"%x)
        speed4.deinit()
        fc.stop()

      
    #    speed4 = Speed(10)
     #   speed4.start()
      
      #  fc.turn_left(20)
      #  x = 0
      #  for i in range(15):
       #     time.sleep(0.1)
        #    speed = speed4()
         #   x += speed * 0.1
           # print("%smm/s"%speed)
       # print("%smm"%x)
       # speed4.deinit()
      #  fc.stop()  

        # time.sleep(2)
#        fc.forward(20)
   #     fc.stop()
 #       time.sleep(0.5)
#        fc.turn_right(50)  
#fc.stop()        

     #   self.back_wheels.speed = speed


  #  def process_objects_on_road(self, image):
  #      image = self.traffic_sign_processor.process_objects_on_road(image)
  #      return image

    def follow_lane(self, image):
        image = self.lane_follower.follow_lane(image)
        return image


############################
# Utility Functions
############################
def show_image(title, frame, show=_SHOW_IMAGE):
    if show:
        cv2.imshow(title, frame)


def main():
   with PiCar() as car:
        car.drive(10)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)-5s:%(asctime)s: %(message)s')
    
        main()
    except KeyboardInterrupt:
        print("stopped by User")
       # ctrl+c
    finally: 
        fc.stop()