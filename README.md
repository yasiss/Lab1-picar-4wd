# Lab1-picar-4wd
**** need to run following not to have a pink screen

>sudo vcdbg set awb_mode 0 

Files
-------------------------------------------
cam_car.py --> shows lane_detection when lanes are blue without driving

car_drive.py --> main file --> following 2 files called there
lane_follower.py --> shows lane_detection when lanes are blue for the main file drive
object_on_road.py --> detect 6 objects and the model was trained for 7h with 40 images
(needed more images for accurate result)


reset_servo--> bring the servo to the middle looking forward as it is broken

obst_avoid.py--> obstacle avoidence with broken servo

camera_surveillance.py --> Camera Surveillance
