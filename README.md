# Close Pass Pi
Use pi camera and LiDAR / ultrasound to detect and record drivers passing bikes badly.  

Project started at #picademy.

## Goals

* Active research into using Raspberry Pi on a bike
* Gather data about how drivers pass cyclists
* Gather evidence of bad passing

Please note at the moment I'm just hacking away on the platform, I'm not sure if anyone could or should use this evidence but its worth a go.

## Idea
* Put a distance sensor, pi camera, pi and battery into a saddle bag which fits under the bike seat. 
 * Distance sensor pointing to the right
 * Camera pointing backwards
* Have code looping around measuring distance
 * if car is too close start bleeping & record for another 10 seconds and save that to disk. Using a circular video buffer to be able to decide whether to record a cars overtake to disk after they have got too close.

## Hardware 

* A Pi
  * 3b
  * Zero W maybe
* A battery system (I'm using a PiJuice)
* A PiCamera https://shop.pimoroni.com/products/raspberry-pi-camera-module-v2-1-with-mount
* A Ultrasound Distance Sensor HC-SR04 
* A LiDAR Time of Flight Sensor 
  * First go was with this VL53L0X based one https://www.amazon.co.uk/SODIAL-VL53L0X-Flight-Distance-GY-VL53L0XV2/dp/B075LHC51D
  * This alternative may work https://shop.pimoroni.com/products/vl53l1x-breakout 
  
![Ultrasound Build 1](/docs/imgs/Ultrasound_Build_1.jpg)

![LiDAR Build 1](/docs/imgs/LiDAR_Build_1.jpg)
  

## Software

* https://gpiozero.readthedocs.io/en/stable/api_input.html#distance-sensor-hc-sr04
* This one is hard to use https://github.com/johnbryanmoore/VL53L0X_rasp_python so I'll be looking for something easier
* https://picamera.readthedocs.io/en/release-1.13/

