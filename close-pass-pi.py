from picamera import PiCamera
from time import sleep
camera = PiCamera()

# TODO : start camera
camera.start_preview(alpha=192)
sleep(2)
camera.capture("/home/pi/Desktop/image.jpg")
camera.stop_preview()


# TODO : Sense ultra sound distance.

# TODO : Loop distance sensor

# TODO : trigger something on distance

# TODO : get ring buffer recoirding

# TODO : on trigger write buffer to disk.

