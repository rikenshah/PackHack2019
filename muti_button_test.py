import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(15, GPIO.IN)

while True:
    print(".", end='')
#    GPIO.output(23, True)
   if(GPIO.input(17) == True):
      print ("Pin 17 / Green Button is true")
      # do stuff based on pin 25 here
   elif(GPIO.input(18) == True):
      print ("Pin 18 / Yellow Button is true")
      # do stuff based on pin 18 here
   elif(GPIO.input(15) == True):
      print ("Pin 15 / Red Button is true")
      # and again for pin 22