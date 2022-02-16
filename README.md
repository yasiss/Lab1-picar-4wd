# Lab1-picar-4wd

This project is implemented on PiCar-4WD
picar-4wd is the 4WD car that is built based on the Raspberry Pi.

I setup the car was and a camera was attached to it as well.


Quick Links:

 * [About PiCar-4WD](#about_this_module)
 * [Update](#update)
 * [About SunFounder](#about_sunfounder)
 * [License](#license)
 * [Contact us](#contact_us)

<a id="about_this_module"></a>
### About PiCar-4WD:

**** need to run following not to have a pink screen

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
