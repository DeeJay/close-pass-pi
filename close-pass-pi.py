from picamera import PiCamera
from time import sleep
camera = PiCamera()

# TODO : start camera
camera.start_preview(alpha=192)
sleep(2)


from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4)

while True:
    print(sensor.distance)
    sleep(1)
    
camera.capture("/home/pi/Desktop/image.jpg")
camera.stop_preview()


# TODO : Sense ultra sound distance.

# TODO : Loop distance sensor

# TODO : trigger something on distance

# TODO : get ring buffer recoirding

# TODO : on trigger write buffer to disk.

