from gpiozero import Button
from picamera import PiCamera
from time import sleep

camera = PiCamera()

button = Button(17)

camera.start_preview(alpha=200)

button.wait_for_press()

camera.capture('images/buttonrpi.jpg')
camera.stop_preview()
