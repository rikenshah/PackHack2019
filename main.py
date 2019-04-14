from multiprocessing import Process, Manager
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
from text_recognize_api_call import text_recognize
import sys
import pyttsx3
import time
from gpiozero import Button
from picamera import PiCamera
from signal import pause

class ButtonPressed(Exception): pass

def main():
    global end_result
    global engine
    global pressed
    global camera
    global button_green
    global button_red
    global button_yellow
    button_green.when_pressed = None
    button_red.when_pressed = None
    image_path = "images/buttonrpi-yellow.jpg"
    
    camera.start_preview(alpha=200)
    
    button_yellow.wait_for_press()
    camera.capture(image_path)
    camera.stop_preview()

    p_face_detect = Process(target=face_detect, args = [end_result, image_path])
    p_image_analyze = Process(target=image_analyze, args = [end_result, image_path])
    p_text_recognize = Process(target=text_recognize, args = [end_result, image_path])
    p_face_detect.start()
    p_image_analyze.start()
    p_text_recognize.start()
    p_face_detect.join()
    p_image_analyze.join()
    p_text_recognize.join()
    
    print(end_result)

    if end_result["description"]:
        engine.say(end_result["description"])
        engine.runAndWait()

    if end_result["emotion"]:
        engine.say("A face is detected, do you want to know the emotion?")
        engine.runAndWait()
        pressed = False
        while True:
            button_green.when_pressed = emotion_yes_pressed
            button_red.when_pressed = no_pressed
            #print("GREEN EMOTION" + str(green_pressed))
            if pressed:
                break

    if end_result["text"]:
        engine.say("Image has some text, do you want to listen?")
        engine.runAndWait()
        pressed = False
        while True:
            button_green.when_pressed = text_yes_pressed
            button_red.when_pressed = no_pressed
            #print("GREEN TEXT" + str(green_pressed))
            if pressed:
                break
        

def emotion_yes_pressed():
    print("Bakchodi1")
    global engine
    global pressed
    pressed = True
    engine.say(end_result["emotion"])
    engine.runAndWait()


def text_yes_pressed():
    global engine
    global pressed
    pressed = True
    engine.say(end_result["text"])
    engine.runAndWait()


def no_pressed():
    global pressed
    pressed = True


def cb(name):
    pass
    
    
if __name__=='__main__':
    manager = Manager()
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 1)
    engine.setProperty('voice', 'english+f1')
    camera = PiCamera()
    button_green = Button(17)
    button_red = Button(15)
    button_yellow = Button(18)
    engine.connect('started-utterance', cb)
    pressed = False
    while True:
        end_result = manager.dict()
        end_result['description'] = ''
        end_result['text'] = ''
        end_result['emotion'] = ''

        main()
