from gpiozero import Button
from picamera import PiCamera
from time import sleep

camera = PiCamera()

button = Button(2)

camera.start_preview()
button.wait_for_press()
camera.capture('/images/buttonrpi.jpg')
camera.stop_preview()
