import RPi.GPIO as GPIO

while True:
#    GPIO.output(23, True)
   if(GPIO.input(17) == True):
      print ("Pin 17 / Green Button is true")
      # do stuff based on pin 25 here
   else if(GPIO.input(18) == True):
      print ("Pin 18 / Yellow Button is true")
      # do stuff based on pin 18 here
   else if(GPIO.input(15) == True):
      print ("Pin 15 / Red Button is true")
      # and again for pin 22