from gpiozero import Button
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(alpha=200)

buttongreen = Button(17)
buttongreen.wait_for_press()
camera.capture('images/buttonrpi-green.jpg')

buttonyellow = Button(18)
buttonyellow.wait_for_press()
camera.capture('images/buttonrpi-yellow.jpg')

buttonred = Button(1)
buttonred.wait_for_press()
camera.capture('images/buttonrpi-red.jpg')

camera.stop_preview()
