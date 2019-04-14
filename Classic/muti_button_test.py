from gpiozero import Button

def green_pressed():
    print("LOLOLO")

button_green = Button(17)

while True:
    button_green.when_pressed = green_pressed


