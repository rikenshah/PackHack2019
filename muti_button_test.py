import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
#    GPIO.output(23, True)
   if(GPIO.input(17) == GPIO.HIGH):
      print ("Pin 17 / Green Button is true")
      # do stuff based on pin 25 here
   elif(GPIO.input(18) == GPIO.HIGH):
      print ("Pin 18 / Yellow Button is true")
      # do stuff based on pin 18 here
   elif(GPIO.input(15) == GPIO.HIGH):
      print ("Pin 15 / Red Button is true")
      # and again for pin 22