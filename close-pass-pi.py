import picamera
from time import sleep

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
        # TODO : on trigger write buffer to disk.
        if(sensor.distance > 0 and  sensor.distance < minDistance):
            print("Too Close... Recording");
            camera.wait_recording(10)
            stream.copy_to("/home/pi/Desktop/motion{}.h264".format(i));
            print("Recording Ended");
            i += 1
            if i> 2:
                break
                # Keep recording for 10 seconds and only then write the
                # stream to disk
            
finally:
    camera.stop_recording()
    


