# Lab1-picar-4wd

* This project is implemented on PiCar-4WD
* picar-4wd is the 4WD car that is built based on the Raspberry Pi.

## What has been done.
* Setting up raspberry pi operating system on Micro SD 64 
* Assembled the PiCar-4WD 
* Connect the raspberry pi to the car and communicated with it 
* One of the files is an obstacle avoidance code, quite simple, for the obstacle detection task by the servo and the camera. 
* I defined a function to reset my servo each time an obstacle avoided.
In the code, obst_avoid.py, the car sees the obstacle and then will stop, go backward, and turn right 
* I have implemented line detection. I have used OpenCV functions and capability to achieve line detection. if the lines are in blue the car can detect and map them. 
the code is in: cam_car.py 
* For giving the computer vision to my car I used the Pi Camera. I used Raspberry Pi NoIR Camera instead of the regular camera. 
Raspberry Pi Camera has a sharper better-quality image, in daylight or well-lit room than NoIR camera 
Raspberry Pi NoIR Camera has better vision at night so can be used for setting up surveillance camera at night. 

Pi NoIR camera had a shade of pink, so I fixed that by running the following code. 

sudo vcdbg set awb_mode 0   

I have tested the Pi camera by setting up a surveillance camera/video streaming. By accessing the IP address of Raspberry Pi as follow and using the address to access my feed like surveillance camera by web. 

pi@raspberry:~ $ ifconfig 
 
camera_surveillance.py

### Object Detection  

I used 
* Tensorflow
* OpenCV
* Anaconda - Notebook
* CUDA
* cuNN 
to create custom Tensorflow lite model trained the model. I used 6 objects for my object detection. 
For training my model, I created a virtual tensorflow environment on Anaconda on Laptop. 
I took pictures of my objects in different orientations and on different backgrounds to train my model. 

I used **Labelimage** to label the images.

I used Tensorflow model “ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03” as the base of my code from  https://github.com/tensorflow/models . 
 
Training the model took about 7 hours


**** need to run the following on Raspberry Pi not to have a pink screen from camera

>sudo vcdbg set awb_mode 0 

### Files
-------------------------------------------
cam_car.py --> shows lane_detection when lanes are blue without driving

car_drive.py --> main file --> following 2 files called there
lane_follower.py --> shows lane_detection when lanes are blue for the main file drive
object_on_road.py --> detect 6 objects and the model was trained for 7h with 40 images
(needed more images for accurate result)

reset_servo--> bring the servo to the middle looking forward as it is broken

obst_avoid.py--> obstacle avoidence with broken servo

camera_surveillance.py --> Camera Surveillance

### Quick Links:

 * [About PiCar-4WD](#about_this_module)
 * [Update](#update)
 * [About SunFounder](#about_sunfounder)

<a id="about_this_module"></a>


