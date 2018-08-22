import picamera
from time import sleep
import VL53L0X
from gpiozero import LED

buzzer = LED(21)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))


i = 1
minDistance = 0.5

#camera.start_preview(alpha=192)

from gpiozero import DistanceSensor
from time import sleep

# TODO : get ring buffer recording
camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=20)
camera.start_recording(stream, format='h264')
print("Camera started");

sensor = DistanceSensor(echo=17, trigger=4)

try:
    while True:
        camera.wait_recording(0.1)
        distance = tof.get_distance()
        if (distance > 0):
            print ("%d mm, %d cm, %d" % (distance, (distance/10), i))
        
        if(distance > 0 and  distance/ 1000 < minDistance):
            buzzer.blink()
        # TODO : on trigger write buffer to disk.
        #if(sensor.distance > 0 and  sensor.distance < minDistance):
            print("Too Close... Recording");
            camera.wait_recording(2)
            stream.copy_to("/home/pi/Desktop/motion{}.h264".format(i));
            print("Recording Ended");
            buzzer.off()
            i += 1
            #if i> 10:
            #    break
                # Keep recording for 10 seconds and only then write the
                # stream to disk
            
finally:
    camera.stop_recording()
    


